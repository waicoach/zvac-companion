# ZVÂC Companion

![ZVÂC Companion](icon.png)

Connect Claude to the existing hosted ZVÂC Companion service and work only
with the context you choose to authorize. AI supports reflection and proposed
actions; you remain the decision-maker.

**Preview package, version 0.1.1.** The format has local checks; actual
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
