# Anthropic directory preparation

Prepared 17 October 2026. This is a publisher worksheet, not a completed
submission, a legal opinion, an approval, or a claim that live OAuth works.
Keep an existing portal draft; do not create a duplicate submission.

## Source and listing

| Field | Prepared value |
|---|---|
| Repository | https://github.com/waicoach/zvac-companion |
| Plugin path | `plugins/zvac-companion` |
| Branch | `main` |
| Display name | ZVÂC Companion |
| Version | 0.1.2 |
| Short description | Use explicitly authorized ZVÂC context and review proposed career actions before confirming them. |
| Listing description | The plugin's [README](plugins/zvac-companion/README.md), including examples, requirements, data handling and known verification limits. |
| Icon | The bundled official icon, already referenced by the manifest. |
| Privacy | https://zvac.net/privacy |
| Terms | https://zvac.net/terms |
| Support | https://zvac.net/contact |

The public ZVÂC policies identify WAIHEKE SRL as the operator. The publishing
account must have authority to represent that entity and control the endpoint,
domain, repository and brand. Confirm the Claude organization that should own
the listing long term before submitting.

The technical files and instructions have an owner-approved MIT license.
The plugin folder includes its own [LICENSE](plugins/zvac-companion/LICENSE)
and [brand notice](plugins/zvac-companion/BRAND-NOTICE.md). No package-wide
SPDX field is used to imply that the brand asset is MIT-licensed. Anthropic's
checklist accepts a LICENSE file instead of a manifest license field.

Upload the new archive contents without deleting the existing repository.
The browser uploader may skip dotfiles: separately edit the existing
`plugins/zvac-companion/.claude-plugin/plugin.json` to match this release.
The marketplace manifest and MCP configuration are unchanged. Then click
**Re-validate** in the existing portal draft. Validation applies only to the
commit it read. The icon-field warning explicitly needs no action.

## Data handling: evidence-based answers

Do not answer every question "No" because the package is a small static
bundle. The remote service reads and stores personal data.

| Portal topic | Prepared factual answer / boundary |
|---|---|
| Reads personal data | Yes. Authorized career/profile projections and explicitly selected CV/application content may contain personal data. Scope, membership, entitlement and resource-selection controls still apply. |
| Stores personal data | Yes at the ZVÂC service: connection/consent records, selected-resource references, operational/security metadata and explicitly confirmed saved resources. The plugin itself has no local database. |
| Sends data outside declared connectors | The package declares only the ZVÂC MCP endpoint, sends tool arguments there and returns results to Claude. It declares no separate analytics endpoint or local executable. Requested Plan preview generation can invoke ZVÂC AI providers on the server. Do not answer a broad "no third-party processing" question without that qualification. |
| Retention | Account and saved career data follow the ZVÂC privacy policy. Account deletion removes or de-identifies active-system data subject to security, legal, billing, processor and backup exceptions. The policy does not supply one universal day count. If the form requires exact periods, obtain verified service-specific values rather than inventing them. |
| Training / processing location | Do not promise no training, zero retention, a particular region, or a fixed AI provider from the package alone. Verify the active service and provider terms before such an attestation. |
| Under-18 audience | Publisher decision still required. ZVÂC's public service terms allow accounts from 16; this is not evidence that this Claude plugin is intended for under-18s or that Claude permits that audience. Check Anthropic's current eligibility rules and the intended Companion audience before answering. Do not change the platform age policy through this submission. |

Revocation stops future authorized access; it is not deletion of information
already returned to Claude or undoing a confirmed save. Token lifetimes
(10-minute access, rotating 30-day refresh, 90-day family maximum) and
five-minute confirmation validity are not retention/deletion guarantees.

## Compliance and review

- Use a monitored, verified contact address in the private portal. Do not
  add private contact details or reviewer credentials to this repository.
- Read the current Directory Terms and Policy and personally confirm only
  acknowledgements supported by evidence. No acknowledgement is accepted by
  this worksheet or by installing the plugin.
- Provide a dedicated, appropriately entitled account populated with fictional
  data to reviewers through the private portal, never through GitHub or chat.
  Such an account has not been created by this package.
- Run the [synthetic Claude checklist](CLAUDE-TEST.md) before attesting that
  tools, permissions, revocation and prepare/confirm work. No such result is
  available yet. Compare behavior with/without the skill as requested by
  Anthropic; manifest validation is not a behavioral evaluation.
- Keep automatic publishing off while the first version and authentication
  behavior are being verified. Preparation does not authorize submission,
  acceptance of legal terms or publication.

## The hosted MCP connector is a separate submission

Anthropic's current documentation says to submit an owned remote MCP server
as an **MCP connector** even when a plugin bundle references it, preferably
before the plugin submission and from the same Claude organization.

Prepared connection facts:

- Server URL: `https://zvac.net/api/companion/mcp`
- First-party ZVÂC service; not an arbitrary third-party API proxy.
- Existing public client: `zvac-claude`; no client secret.
- Existing exact callback: `https://claude.ai/api/mcp/auth_callback`
- S256 PKCE and exact resource binding; no DCR or CIMD registration.
- Read tools plus separately authorized prepare/confirm writes and optional
  unsaved AI Plan generation. Do not advertise it as read-only.
- Documentation: https://github.com/waicoach/zvac-companion/blob/main/plugins/zvac-companion/README.md
- The plugin README supplies three synthetic prompts and setup prerequisites.

**Known connector readiness gaps, not fixed by this archive:**

1. Current server source emits tool names, descriptions and annotations, but
   does not emit tool `title` fields in `tools/list`. Anthropic's connector
   checklist requires titles. A separately reviewed backend change and later
   deployment are needed; this package does neither and does not assert the
   deployed response was inspected.
2. Hosted Plugins propagation of the fixed public OAuth client and resource
   is unverified. Do not select a directory authentication mode that implies
   DCR, CIMD or a secret this service does not have. Confirm a compatible mode
   with the portal/reviewer; protocol or identity changes require approval.
3. Actual Claude installation, login, tool discovery, allowed/denied reads,
   revocation, refresh and prepare/confirm behavior remain untested here.
4. A fully populated synthetic reviewer account, intended-age decision,
   effective provider details where requested, verified contact and owner
   compliance acknowledgements are not supplied by an archive.

These are reasons not to claim the connector is ready to submit. They do not
prevent uploading this package and re-running plugin source validation.

## Evidence and sources

The owner's earlier source-validation screenshot reported 6/7 checks passed
for 0.1.1, with a missing-license blocker and icon/privacy warnings. That
report does not apply to 0.1.2 until it is uploaded and validated again.
The public repository inventory was read; no authenticated GitHub write,
Claude session, backend change, production configuration change or deployment
was performed in this preparation.

Sources consulted on 17 October 2026:

- https://claude.com/docs/plugins/pre-submission-checklist
- https://claude.com/docs/plugins/submit
- https://claude.com/docs/directory/publish
- https://claude.com/docs/connectors/building/submission
- https://claude.com/docs/connectors/building/authentication
- https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy
- https://support.claude.com/en/articles/13145338-anthropic-software-directory-terms
- https://opensource.org/license/mit
- https://zvac.net/privacy
- https://zvac.net/terms
