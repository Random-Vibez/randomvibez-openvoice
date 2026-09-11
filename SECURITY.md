# OpenVoice Board — public security boundary

This public edition is fixed and static by design.

- No backend, database, API route, account, cookie, local persistence, import, export, or customization.
- No network calls, third-party assets, analytics, service worker, or remote script.
- Vocabulary is compiled into `app.js` as curated board data.
- User-selected board and speech preferences exist only in the active page; there is no user message store or persistent content.
- The hosting `.htaccess` supplies HTTPS-era headers, CSP with `connect-src 'none'`, HSTS, frame denial, no-index listing, and no-store caching.

## Why customization is absent

Public customization would create unnecessary risks: unreviewed vocabulary, accidental sensitive information, misleading emergency phrases, unsafe imported files, and a larger attack surface. The public release therefore offers several reviewed boards instead of user-authored content.

## Safety boundary

This is not a medical device, emergency dispatch service, or substitute for professional AAC assessment. Do not rely on it as the only communication or emergency plan.

## Deployment rule

Serve only this directory as static content. Do not add an API, database, credential flow, analytics snippet, remote font/script, upload route, or shared storage layer without a new security review.
