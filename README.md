# Instagram lead autopilot (template)

A faceless Instagram system that posts every day and turns comments into qualified leads, with no daily human work except calling leads.

- `business.json` – everything about the business: brand, language, audience segments, comment keywords and what each delivers, DM questions, posting stages, on-screen words, verified facts. Nothing else names the business.
- `bank/` – scripts for reels, carousels, posters and stories (the examples are placeholders).
- `factory/` – turns scripts into 3D dialogue reels, chat reels, list reels, carousels, posters and stories (`factory.yml`, 01:00 and 13:00).
- `worker/` – Cloudflare autopilot: staged posting, keyword-comment DMs, qualifying chat, check-ins, lead alerts to Discord, insights.
- `setup/` – `configure.mjs`, `gen-config.mjs`, `fonts.py`, `SETUP.md` (accounts the owner creates), `LANGUAGES.md`.

Set up with the `instagram-lead-autopilot` skill: the owner creates the accounts in `setup/SETUP.md`, stays logged in, and says "start".
