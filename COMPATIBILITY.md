# Compatibility evidence — 17 October 2026

## What is supported by documentation

Sources were consulted on this date; they can change. Documentation is evidence
of an intended contract, not evidence of this package running in an account.

| Source | Evidence and limit |
|---|---|
| [Plugin manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference#directory-listing-fields) | `displayName` provides the UI name; `icon` references a packaged image. The icon is documented for directory listings, not guaranteed to display in repository marketplaces. Version 0.1.1 includes the official ZVÂC PNG and this reference. |
| [Plugins overview](https://claude.com/docs/plugins/overview) | Customize → Plugins accepts repository marketplaces. Bundled connectors are separately added/connected. Organization policy can restrict both. |
| [Plugin structure and testing](https://claude.com/docs/plugins/build) | `.claude-plugin/plugin.json`, plugin-root `.mcp.json`, `skills/<name>/SKILL.md`. Remote connectors appear on the Connectors tab. Requires tests on each intended surface. |
| [Platform support](https://claude.com/docs/plugins/platform-support) | Fixed-URL HTTP remote MCP is supported in chat and Cowork; components differ across surfaces. This package does not certify Claude Code. |
| [Marketplace reference](https://code.claude.com/docs/en/plugins/marketplace-reference) | Root marketplace name/owner/plugins and repository-relative plugin source. Used for file syntax only, not as a Claude Code runtime test. |
| [Anthropic productivity MCP example](https://github.com/anthropics/knowledge-work-plugins/blob/181c4f6ff5a246f776027dcd79e2b330b68bf3be/productivity/.mcp.json) | A public example includes `oauth.clientId`. It also has a provider-specific callback port, which is deliberately NOT copied. The example does not certify propagation of that field into Plugins' hosted OAuth. |
| [Anthropic marketplace example](https://github.com/anthropics/knowledge-work-plugins/blob/181c4f6ff5a246f776027dcd79e2b330b68bf3be/.claude-plugin/marketplace.json) | One catalog can reference plugin folders by relative paths. |
| [Add a custom connector](https://claude.com/docs/connectors/custom/add-unlisted#choose-authentication-settings) | Own OAuth client ID can be entered and secret left blank for a public client. This is a documented manual setup path, not automatic manifest propagation. |
| [Connector authentication](https://claude.com/docs/connectors/building/authentication) | S256 PKCE on authorization, public-client behavior with blank secret, hosted callback `https://claude.ai/api/mcp/auth_callback`, protected-resource discovery and refresh. |
| [Custom remote MCP account requirements](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) | Free/Pro/Max/Team/Enterprise remote connectors; Free has one. This is not an unconditional claim about marketplace eligibility. |

## Reconciled existing service contract

This package was checked against current implementation, not only an older
connection guide. No server code, consent, entitlement or production setting
was changed for it.

- Fixed public client `zvac-claude`, no client secret; exact hosted callback
  above. No Dynamic Client Registration and no Client ID Metadata Document
  registration support in the existing client allowlist.
- S256 PKCE; exact `resource=https://zvac.net/api/companion/mcp` is required on
  authorization, code exchange **and refresh**. Resource propagation through
  a real Plugins connection remains unverified.
- Metadata discovery and HTTP MCP are implemented. The package URL matches
  the existing ZVÂC setup configuration; this is not a live deployment probe.
- Tokens: 10-minute access tokens, rotating 30-day refresh tokens, plus a
  90-day absolute family limit. A generic “30-day connection” statement would
  omit the rotation/family distinction.
- Explicit organization and consent, scope narrowing, fresh eligibility
  checks, selected-resource authorization and five-minute prepare/confirm
  intents remain server-owned.
- The older guide mentions `readiness:read` / `get_career_readiness_snapshot`;
  neither is in the current route registry. They are deliberately excluded.
- Plan preview generation can use AI. “All tools are read-only” or “tools
  never call AI” would be incorrect. No new tool or scope is added here.

## Validation and external status

| Layer | Status |
|---|---|
| File syntax, strict package shape, relative paths, bounded safety scan | Repeatable local checks supplied in `tools/validate.py`; exporter also checks an isolated extracted copy. See delivery evidence for the actual run. |
| Current backend/config agreement | Local source reconciliation only; no live availability claim. |
| Anthropic manifest validator | Not run; local checks are not a substitute for it. |
| GitHub hosting | Not performed: no approved destination supplied. Clean archive is the deliverable. |
| Plugins repository installation | Not run: no authorized hosted repository and no authenticated Claude Plugins session available for this task. |
| Automatic `oauth.clientId` use | Unverified in Plugins. The manifest follows a public example, not a certified hosted OAuth contract. |
| OAuth consent, code exchange, refresh and tool discovery in Plugins | Not run. PKCE and callback are documentation-compatible; actual request behavior needs vendor evidence. |
| Allowed read, denied read, revoke, prepare/refuse/confirm | Checklist provided; no real Claude result claimed. |

## Stop conditions

If Plugins ignores the fixed ID, requires DCR/CIMD, insists on a secret,
uses another callback, omits `resource` during any exchange, or cannot
complete the connector setup, record the precise failing stage and stop.
Do not add a registration endpoint, new client, wildcard/loopback callback,
transport proxy or copied-token workflow. Any such change needs a separately
approved protocol/identity decision. A successful custom connector or CLI
test must be recorded as such, never substituted for the requested Plugins test.
