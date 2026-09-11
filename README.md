# OpenVoice Board — fixed public edition

OpenVoice Board is a standalone static communication aid with curated boards for everyday needs, feelings and comfort, conversation and choices, and care and health words.

## Public behavior

- Tap a card to show the phrase and use browser speech playback when supported.
- Adjust speech speed, use high contrast, or print the current board.
- No message composition box, undo/clear controls, add-card, edit, delete, rename, copy, import, or export features.
- No browser persistence for messages or board data; every visitor receives the same curated boards.

The fixed vocabulary and no-upload design are intentional. They make the public tool predictable, reduce accidental disclosure, and prevent visitors from changing shared content or introducing files/scripts through customization controls.

## Deliberate boundary

There is no server, API, fetch, cookie, localStorage, IndexedDB, analytics, external asset, login, database, or shared-board feature. The site can be served as static files only. The board is not customized per user and message contents disappear when the page is left or refreshed.

This is a general communication aid, not a medical device, emergency service, or replacement for an individualized AAC assessment or established communication plan. Speech playback depends on browser support. Test the curated cards with the intended user before relying on them.
