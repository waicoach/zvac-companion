# ZVÂC Companion marketplace for Claude Plugins

![ZVÂC Companion](plugins/zvac-companion/icon.png)

An independent distribution package for **Customize → Plugins → Add marketplace
→ Add from a repository**. Some current interfaces label the same entry
**Add → Add marketplace**. It contains one plugin pointing to the existing
hosted ZVÂC Companion; it contains no platform backend.

**Status: prepared for a controlled installation test, not vendor-certified.**
Local checks do not prove installation, OAuth, tool execution or availability
on a live ZVÂC deployment. See [compatibility evidence](COMPATIBILITY.md) and
the [Claude test checklist](CLAUDE-TEST.md). The owner published the initial
package at https://github.com/waicoach/zvac-companion. Check the repository's
actual version before assuming this newer archive has been uploaded.

Version **0.1.2** adds the approved MIT license for technical files, separate
brand terms and canonical privacy/support links. See the
[directory preparation guide](SUBMISSION.md); preparation is not submission
or approval. The package includes the official 1024px ZVÂC icon, the display name
**ZVÂC Companion**, and the icon reference in the plugin manifest. No separate
icon upload is required to include the branding in this repository. Claude's
documentation specifies the icon field for directory listings; its display
in a repository-added marketplace remains unverified.

## Requirements

- A Claude account with **Customize → Plugins** and permission to add a
  repository marketplace. Use claude.ai or the current Claude desktop app for
  setup; this guide does not promise mobile installation or Claude Code support.
- Anthropic documents directory discovery for Pro, Max, Team and Enterprise.
  Custom remote connectors are separately documented for Free, Pro, Max, Team
  and Enterprise, with one custom connector on Free. These facts do **not**
  establish that every account can add this marketplace. Verify the actual
  Plugins controls; do not upgrade solely on this package's assurance.
- Team/Enterprise policies may block self-added marketplaces. An Owner (or an
  eligible Enterprise custom role for connectors) may need to add the
  connector before members individually sign in.
- Your own signed-in ZVÂC account with Companion premium entitlement and
  membership in an active organization with an unexpired license. Each tool
  remains subject to current module/product access; some actions require
  a member role and a suitable saved career, active Goal or Plan.
  Installing this package never buys a subscription, enables modules, grants
  permissions, changes a role or upgrades an existing connection.

## Install from an approved repository

1. Obtain the URL of the **separate repository containing this package only**.
   Do not use the platform repository or a link to a folder within it.
2. Open **Customize → Plugins → Add marketplace → Add from a repository**
   (or **Add → Add marketplace**). Paste that repository URL.
   For a private GitHub repository, Claude may ask you to connect GitHub and
   grant the Claude GitHub App access to that repository. That access is
   separate from ZVÂC consent; review it independently.
3. Find `zvac-companion` in `zvac-companion-marketplace` and add it.
4. Open the plugin's **Connectors** tab. Add/connect `zvac-companion`.
   Installation alone does not connect it. An existing connection may appear
   as connected: inspect its actual ZVÂC scopes rather than assuming fresh consent.
5. If Claude offers authentication settings, use **Sign in now** and
   **Use your own OAuth client** (or the older **Advanced settings**):

   | Setting | Exact value |
   |---|---|
   | MCP server URL | `https://zvac.net/api/companion/mcp` |
   | Public OAuth client ID | `zvac-claude` |
   | Client secret | Leave empty |

   Do not choose automatic registration or Claude's published identity:
   the existing ZVÂC server uses a fixed public client, not DCR or CIMD.
   Do not paste bearer tokens, request headers or an authorization URL.
   Claude owns PKCE and must use `https://claude.ai/api/mcp/auth_callback`.
   If Plugins ignores `oauth.clientId` and does not offer an own-client setting,
   **stop and record the blocker**. A separately added custom connector using
   these values is a documented diagnostic path, not proof that repository
   plugin authentication worked.
6. In the ZVÂC browser flow, complete sign-in/MFA as required, choose the
   organization and review **every** requested permission. Uncheck anything
   you do not want. You can deny the request. At least one eligible permission
   must be retained to connect. Installation does not choose these for you.
7. Under **ZVÂC → account → companions**
   (`https://zvac.net/account/companions`), inspect this connection. For selected
   CV, application or job access, separately choose exactly one current resource
   of each kind you intend to share. OAuth consent alone is not that selection.
   Changing a resource can invalidate its selection and require selection again.
8. Enable only the tools needed in your Claude conversation. Start with a
   synthetic read-only test from [CLAUDE-TEST.md](CLAUDE-TEST.md), not a real
   person's private data.

## Usage and limits

Ask for a specific task, rather than automatic profile collection. For example,
on a synthetic test account: “Read only the CV I selected for this connection.
Do not read my applications or save anything.” If no CV is selected, stop and
select it in ZVÂC; never ask Claude to guess.

The existing server implements permission-bound professional summaries,
assessment progress (not raw answers), development milestones, active Missions,
application metadata, saved careers and explicitly selected CV/application/job
projections. The actual tool list depends on granted scopes, and execution
rechecks access. A scope can expose more than one tool. Some canonical
summaries, milestones and career/CV projections are user-global, authorized
through the selected organization; not every read is organization-local.
No AI Readiness snapshot tool is advertised by this package.

Separately consented actions can prepare and confirm a development milestone,
private Mission, saved career direction, reviewed Plan draft, or start of an
already accepted Plan Mission suggestion. Show the exact normalized proposal
and ask for separate approval before confirmation. Prepare creates no career
resource, but stores temporary confirmation metadata. Unsaved Plan previews
may invoke ZVÂC AI and limits apply. Neither a preview nor a draft activates
a Plan, edits a Goal, completes a Mission, awards XP, submits an application
or schedules an external calendar event.

Only a successful confirmed server receipt is evidence of a save. Do not
blindly retry an ambiguous write with a new idempotency key. Skill instructions
are behavioral guidance, not independently enforced host confirmation.

## Withdraw access

In ZVÂC at `https://zvac.net/account/companions`, open the relevant Claude
connection, choose revoke and confirm. Verify its revoked status. Revoke each
connection you no longer want; revoking one does not revoke another.
You can also reset an individual CV/application/job selection to stop its
future reads without revoking the whole connection.

Then disconnect the connector or remove the plugin in Claude if desired.
**Uninstalling a plugin is not proof of revocation in ZVÂC.** Previously
returned data may remain in Claude conversations under Claude's retention
settings. Revocation does not erase those conversations or undo confirmed saves.
To change scopes, explicitly reconnect and review consent; old grants are
not silently expanded.

## Troubleshooting

| Symptom | Safe next step |
|---|---|
| Marketplace absent or repository denied | Check Plugins availability, organization policy and access to the separate repository. Do not expose the platform repository. |
| Plugin loads but no connected tools | Inspect its Connectors tab and add/connect the remote connector. Loading a skill proves no authorization. |
| Unknown client/redirect, DCR registration failure | Verify the own-client ID and exact hosted callback. If the UI cannot use them, stop. No new client identity, wildcard callbacks or protocol changes are authorized. |
| `invalid_target` | The host must send the exact MCP resource in authorization, code exchange and refresh. Do not weaken resource binding. |
| `invalid_scope` / access denied | Review retained permissions and eligible organization. A denied consent is not a connection. |
| HTTP 401 | Missing/expired/revoked authentication; inspect ZVÂC status and reconnect only if you choose. Never paste a token. |
| HTTP 403 or tool access error | Check scope, membership, license, entitlement, module/product and role. Broader read tools are not a workaround. |
| Selected resource missing/stale | Choose it again explicitly in ZVÂC. Do not infer another resource. |
| HTTP 409 or stale/expired confirmation | Stop. Reconcile an uncertain previous save first; otherwise prepare anew and ask for fresh approval. |
| HTTP 429 | Wait for retry guidance; do not loop. |
| HTTP 503 / temporarily disabled | Stop; service access may be suspended. Installing again does not fix it. |

Some tool failures arrive as JSON-RPC errors inside an HTTP response; check
the tool result, not just the HTTP status. Share only sanitized error names
and the failing step, never tokens, query strings, personal data or raw traces.

## Verify and publish only this package

Requires Python 3.10+ standard library for maintainer checks, **not** for
installation. There are no runtime package dependencies.

Before initializing Git, from this directory run:

```sh
python3 tools/validate.py
```

It checks the exact file allowlist (including dotfiles), JSON keys, local paths,
the fixed MCP connection and common secret/private-data indicators. This is a
bounded local validator, not Anthropic's validator or exhaustive secret detection.
Human inspection of all files remains necessary before distribution.

Extract the marketplace archive into a new empty directory outside any existing
checkout. Keep `.claude-plugin/` at that directory's root. Do not use a shell
`*` copy that omits hidden files. Validate there, create a new empty GitHub
repository in an **explicitly approved owner/name and visibility**, and only
then initialize new history from that directory:

```sh
git init -b main
git add -- .claude-plugin README.md COMPATIBILITY.md CLAUDE-TEST.md SUBMISSION.md LICENSE RIGHTS.md plugins tools
git commit -m "Add ZVAC Companion plugin preview"
```

Add the exact approved repository as `origin` and push `main`. No remote is
preconfigured. Never push from the platform checkout, import its Git history,
or choose a public destination implicitly. A private marketplace is not an
Anthropic catalog submission. This package grants no open-source license to
the platform; see [RIGHTS.md](RIGHTS.md).

### Browser uploads

GitHub's browser uploader can omit dot-prefixed files even when Windows
Hidden items is enabled. Verify the repository includes all three:

- `.claude-plugin/marketplace.json`
- `plugins/zvac-companion/.claude-plugin/plugin.json`
- `plugins/zvac-companion/.mcp.json`

If one is missing, use **Add file → Create new file**, enter the complete
nested path, paste the exact reviewed content, and commit. Do not rename a
dotfile to make upload accept it. For an existing repository, updating visible
files does not update a skipped hidden manifest: edit the plugin manifest
separately to include this version's legal links and version number.

The marketplace archive is for a **repository root**, not **Upload plugin**.
An upload diagnostic must instead zip only `plugins/zvac-companion` (including
its dotfiles). An upload test still does not certify repository installation.
