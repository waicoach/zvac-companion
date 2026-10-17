"""Offline, standard-library-only checks for this bounded distribution.

Not an Anthropic schema validator, live OAuth test or exhaustive secret scanner.
Run before git init; unknown files (including Git history) fail closed.
"""

import hashlib
import json
from pathlib import Path
import re
import stat
import sys
from urllib.parse import urlsplit


FILES = (
    ".claude-plugin/marketplace.json",
    "CLAUDE-TEST.md",
    "COMPATIBILITY.md",
    "README.md",
    "RIGHTS.md",
    "plugins/zvac-companion/.claude-plugin/plugin.json",
    "plugins/zvac-companion/.mcp.json",
    "plugins/zvac-companion/README.md",
    "plugins/zvac-companion/icon.png",
    "plugins/zvac-companion/skills/zvac-companion/SKILL.md",
    "tools/validate.py",
)
PUBLIC_HOSTS = {"zvac.net", "claude.ai", "claude.com", "code.claude.com",
                "support.claude.com", "github.com"}
SENSITIVE_PATTERNS = (
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b",
    r"\bgh[pousr]_[A-Za-z0-9]{20,}\b",
    r"\bgithub_pat_[A-Za-z0-9_]{20,}\b",
    r"\bsk-[A-Za-z0-9_-]{20,}\b",
    r"\b(?:zac|zat|zrt|zar)_[A-Za-z0-9_-]{20,}\b",
    r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b",
    r"(?i)\bBearer\s+[A-Za-z0-9._~-]{20,}",
    r"(?i)(?:postgres(?:ql)?|mongodb(?:\+srv)?|redis)://",
    r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
    r"(?i)(?:client_secret|api_key|password|access_token|refresh_token)\s*[=:]\s*[\"'][^\"'\s]{8,}[\"']",
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def keys(value, expected, label):
    require(isinstance(value, dict) and set(value) == set(expected),
            f"{label}: unexpected or missing fields")


def validate(root):
    root = Path(root)
    require(not root.is_symlink(), "Package root must not be a symlink")
    root = root.resolve()
    require(root.is_dir(), "Missing package directory")
    allowed_dirs = {str(parent) for name in FILES
                    for parent in Path(name).parents if str(parent) != "."}
    found = set()
    for path in root.rglob("*"):
        name = path.relative_to(root).as_posix()
        mode = path.lstat().st_mode
        require(not stat.S_ISLNK(mode), f"Symlink rejected: {name}")
        if stat.S_ISDIR(mode):
            require(name in allowed_dirs, f"Unapproved directory: {name}")
        else:
            require(stat.S_ISREG(mode), f"Non-regular file rejected: {name}")
            require(name in FILES, f"Unapproved file: {name}")
            require(not mode & 0o111, f"Executable file rejected: {name}")
            found.add(name)
    require(found == set(FILES), "Package file inventory differs from the approved allowlist")

    contents = {}
    hashes = {}
    for name in FILES:
        raw = (root / name).read_bytes()
        hashes[name] = hashlib.sha256(raw).hexdigest()
        if name == "plugins/zvac-companion/icon.png":
            # Exact inspected official 1024px PNG. Reject altered metadata,
            # appended payloads or an arbitrary binary disguised as artwork.
            require(hashes[name] == "ad37dca40211dca4ea71a79e3855b98a90622bc307f8e4f7b65a52d18f2222dc",
                    "Icon differs from the approved official asset")
            continue
        require(0 < len(raw) <= 60000 and b"\0" not in raw,
                f"Empty, binary or oversized file: {name}")
        text = raw.decode("utf-8")
        contents[name] = text
        hashes[name] = hashlib.sha256(raw).hexdigest()
        for pattern in SENSITIVE_PATTERNS:
            require(not re.search(pattern, text),
                    f"Potential sensitive material: {name} (value withheld)")
        for match in re.finditer(r"https?://[^\s<>`\"')]+", text):
            parsed = urlsplit(match.group().rstrip(".,;"))
            require(parsed.scheme == "https" and parsed.hostname in PUBLIC_HOSTS
                    and not parsed.username and not parsed.password and not parsed.port
                    and not parsed.query,
                    f"Unapproved URL: {name} (value withheld)")
        if name.endswith(".md"):
            for target in re.findall(r"\]\(([^)]+)\)", text):
                if target.startswith("https://"):
                    continue
                local = target.split("#", 1)[0]
                resolved = (root / name).parent.joinpath(local).resolve()
                require(resolved.is_relative_to(root) and resolved.is_file(),
                        f"Broken or escaping documentation link: {name}")

    def load(name):
        return json.loads(contents[name], object_pairs_hook=unique_object)

    marketplace = load(".claude-plugin/marketplace.json")
    keys(marketplace, ("name", "owner", "plugins"), "Marketplace")
    require(marketplace["name"] == "zvac-companion-marketplace", "Unexpected marketplace name")
    require(marketplace["owner"] == {"name": "ZVÂC"}, "Unexpected marketplace owner")
    require(isinstance(marketplace["plugins"], list) and len(marketplace["plugins"]) == 1,
            "Exactly one plugin required")
    entry = marketplace["plugins"][0]
    keys(entry, ("name", "displayName", "source", "description"), "Marketplace plugin")
    require(entry["name"] == "zvac-companion"
            and entry["source"] == "./plugins/zvac-companion", "Unapproved plugin path/name")
    plugin_root = (root / entry["source"]).resolve()
    require(plugin_root.is_relative_to(root)
            and (plugin_root / ".claude-plugin/plugin.json").is_file(),
            "Plugin source does not resolve inside the exported marketplace")

    plugin = load("plugins/zvac-companion/.claude-plugin/plugin.json")
    keys(plugin, ("name", "displayName", "version", "icon", "description", "author"), "Plugin manifest")
    require(plugin["displayName"] == entry["displayName"] == "ZVÂC Companion",
            "Display name mismatch")
    require(plugin["icon"] == "./icon.png" and (plugin_root / "icon.png").is_file(),
            "Icon must resolve within the plugin")
    require(plugin["name"] == entry["name"] and plugin["author"] == marketplace["owner"],
            "Plugin identity mismatch")
    require(isinstance(plugin["version"], str)
            and re.fullmatch(r"\d+\.\d+\.\d+", plugin["version"]), "Invalid release version")
    require(isinstance(plugin["description"], str) and 20 <= len(plugin["description"]) <= 500
            and plugin["description"] == entry["description"], "Description mismatch")
    mcp = load("plugins/zvac-companion/.mcp.json")
    require(mcp == {"mcpServers": {"zvac-companion": {
        "type": "http", "url": "https://zvac.net/api/companion/mcp",
        "oauth": {"clientId": "zvac-claude"},
    }}}, "MCP config must be exactly the approved remote public-client connection")
    skill = contents["plugins/zvac-companion/skills/zvac-companion/SKILL.md"]
    require(re.match(r"\A---\nname: zvac-companion\ndescription: [^\n]+\n---\n", skill),
            "Invalid skill frontmatter")
    require('phase: "prepare"' in skill and 'phase: "confirm"' in skill
            and "explicit approval" in skill, "Missing bounded write instructions")
    return hashes


if __name__ == "__main__":
    try:
        inventory = validate(Path(__file__).resolve().parents[1])
        print(f"PASS: {len(inventory)} approved files; local shape, paths and bounded safety checks.")
        print("NOT VERIFIED: Anthropic validation, GitHub hosting, Claude Plugins installation or OAuth.")
    except (ValueError, OSError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
