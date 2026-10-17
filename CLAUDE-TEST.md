# Controlled Claude Plugins test

**Initial status: NOT RUN.** Use only an authorized synthetic ZVÂC account,
organization and fabricated career data. Do not create a real-user test or
make a production configuration change to make this pass. A permission or
platform blocker is a valid recorded outcome, not a reason to weaken access.

## Evidence record

Record date, Claude surface/app version when available, plan type, package
version and archive checksum, approved repository revision, step, expected
result, observed sanitized result, and PASS / FAIL / BLOCKED / NOT RUN.
Keep actual account names, emails, organization/resource identifiers,
cookies, OAuth state/codes/tokens, private content and raw HAR/network traces
out of the record. Screenshots must be redacted before sharing.

## Sequence

1. **Repository install.** Add the approved standalone repository through
   Customize → Plugins → Add marketplace → Add from a repository. Confirm
   exactly one ZVÂC plugin appears and its skill and remote connector are
   listed. Record plugin installation separately from connector connection.
   Do not use Claude Code or a direct ZIP upload as substitute evidence.
2. **No implicit access.** Before connecting, verify the test account has no
   new active ZVÂC grant. Merely loading the skill must not fetch a profile
   or create career data. Note any preexisting connection instead of calling
   its access a new grant.
3. **Deny consent first.** Start connect, sign in as the synthetic account,
   and deny on ZVÂC's consent screen. Verify no active grant is created.
   Do not record full authorization URLs.
4. **Minimal successful consent.** Retry intentionally. Retain only
   `cv:selected:read`; deselect all others and all writes. Record whether the
   manifest ID was honored or an own-client field was needed. If neither
   works, mark OAuth BLOCKED and stop dependent tests. Inspect the resulting
   grant in ZVÂC: correct organization, only the retained scope.
   Successful login alone is not proof of token exchange or MCP discovery.
5. **Tool discovery and no selection.** In a new conversation, inspect the
   available ZVÂC tools without collecting private content. The retained
   scope should expose `get_selected_cv_profile`, not application reads or
   writes. Request the selected CV before making a ZVÂC selection: expect
   selection-required denial, not an automatically chosen CV.
6. **Permitted read.** In ZVÂC, explicitly select a fabricated uploaded CV
   for this connection. Ask Claude to read only that CV. Verify the bounded
   result corresponds to the chosen synthetic CV; do not include it in the
   evidence record. Tool presence alone is not a successful read.
7. **Refusal/reset/revocation.** Ask for an application read without its
   permission: no data should be returned. If no tool is exposed, record
   “not exposed”, not a claimed server-call denial. Reset the CV selection
   in ZVÂC; a subsequent CV call must fail. Revoke the connection and verify
   subsequent tool use is denied. Cached conversation text is not a fresh
   authorized read.
8. **Prepare with no career-resource effect.** Intentionally create a new
   consent granting only `directions:write`, if the synthetic account's
   existing eligibility permits it. Ask Claude to prepare a manual Saved
   Career titled “Synthetic practice direction” with intent “Explore a
   fictional career for this test only.” Inspect Saved Careers before and
   after prepare: no new career should exist. Temporary confirmation
   metadata is expected; “prepare made no database writes” is not the claim.
9. **Explicit refusal.** Say no to that exact prepared proposal. No confirm
   call should occur and no career should appear.
10. **Separate approved save.** Request a new preparation for a new intent,
    see the exact normalized proposal and effect/source disclosure, then
    explicitly approve it within the confirmation window. Verify one
    confirmed receipt and one corresponding manual Saved Career. No Plan,
    Goal change, Mission, XP, application submission or calendar event is
    expected. An uncertain response means stop and reconcile, not a new
    idempotency key and repeated save.
11. **Final withdrawal.** Revoke all test connections in ZVÂC, verify revoked
    status and fresh-call denial, then disconnect/remove the plugin in
    Claude. Only remove synthetic test content through authorized first-party
    controls. Revocation does not undo a save or erase Claude conversations.

Do not mark dependent steps PASS when an earlier step was blocked. Long-running
refresh, marketplace updates and other Claude surfaces are separate tests,
not implied by this first installation sequence.
