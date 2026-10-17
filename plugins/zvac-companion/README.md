# ZVÂC Companion

![ZVÂC Companion](icon.png)

Connect Claude to the existing hosted ZVÂC Companion service and work only
with the context you choose to authorize. AI supports reflection and proposed
actions; you remain the decision-maker.

**Preview package, version 0.1.2.** Prepared for directory validation; actual
installation and OAuth in Claude Plugins have not been verified. This is not
an Anthropic directory listing or a Claude Code certification.

Open this plugin's **Connectors** tab after installation and add/connect
`zvac-companion`. If authentication settings are offered, choose **Use your
own OAuth client**, enter the public ID `zvac-claude`, and leave the secret
blank. The MCP URL is `https://zvac.net/api/companion/mcp`. Automatic use of
the manifest's OAuth client ID in Plugins is not yet verified. If Claude
requires automatic registration or a different identity, stop rather than
adding a token or changing the server.

Sign in to ZVÂC, choose an eligible organization, and retain only the
permissions you need. Installing does not grant access, create a subscription
or enable a module. Current Companion entitlement, organization membership,
license and tool availability still apply.

For a CV, application or job, separately select the exact resource under
https://zvac.net/account/companions for this connection. Reads send the
authorized projection to Claude. Proposed write content goes to ZVÂC only
through the tool you request; preparation stores confirmation metadata, not
the proposed career resource. Review the exact proposal and approve it
separately before a save. Unsaved Plan generation can invoke ZVÂC AI.

To withdraw access, revoke the specific connection in ZVÂC and check its
revoked status. Resetting a resource selection stops future reads of that
selection. Removing this plugin is not proof that the ZVÂC grant was revoked,
and revocation does not erase information already returned to Claude.

There is no local server, executable hook, install script, credential or
automatic profile read in this plugin. Its skill is guidance, not proof of
the host's behavior or a replacement for server-side controls.

## Example requests

Use synthetic information for installation tests. Each example still requires
the corresponding account access, consent and resource selection.

1. "Read only the CV I explicitly selected for this connection. Suggest clearer
   wording here in the conversation; do not edit or save my CV."
2. "Read only the application I selected for this connection and help me draft
   a short follow-up here. Do not submit or send anything."
3. "Prepare a private Mission called 'Compare two learning options'. Show me
   the exact proposal and ask for my separate approval before saving anything."

## Data handling and legal links

This package declares one remote connector, at
`https://zvac.net/api/companion/mcp`. Tool arguments are sent to ZVÂC and
authorized tool results are returned to Claude. A permitted result can contain
personal career information, including explicitly selected CV or application
content. The plugin does not request unrestricted conversation history.

ZVÂC stores connection/consent records, selected-resource references, security
and tool-event metadata, temporary confirmation metadata, and any resources
that a member explicitly confirms saving. The static plugin has no local
database, analytics endpoint or automatic background collection. The hosted
service is not stateless: do not interpret that as "no data is stored."

Requested unsaved Plan generation may send relevant context to ZVÂC's
configured AI services. Provider and processing details depend on the
effective service configuration; this package does not promise a specific
provider, processing country, no training, or zero retention.

Account and saved career data follow the ZVÂC privacy policy. Deletion,
security/legal exceptions and provider retention are not a single fixed
period. Token expiration and confirmation expiration are not data-deletion
deadlines. Revoking access does not delete previously returned Claude content.

- [Privacy policy](https://zvac.net/privacy)
- [Service terms](https://zvac.net/terms)
- [Support and privacy enquiries](https://zvac.net/contact)

## Package license

Technical files and instructions are licensed under [MIT](LICENSE).
The icon, name and trademarks are excluded; see [Brand notice](BRAND-NOTICE.md).
The platform, hosted backend and user data are not distributed or licensed
by this package.
