---
name: instagram-lead-autopilot
description: Set up a fully automated faceless Instagram lead engine for a business: daily reels, carousels, posters and stories, keyword-comment DMs that qualify leads, check-ins, Discord alerts, monitoring and audience-led script tuning.
---

# Instagram lead autopilot

The owner only creates the accounts in the template's `setup/SETUP.md`, stays logged in, and says "start". You do everything else from the ready-made template. The engineering, the Meta workarounds and the pitfalls below are already solved, so spend research only on the owner's niche and facts.

Template: **Shaazamaan/instagram-lead-autopilot** (public template: https://github.com/Shaazamaan/instagram-lead-autopilot). All business specifics live in `business.json`; nothing else in the repo names a business. Proven in production on a Malayalam company-registration account.

## What gets built
- **Factory** (GitHub Actions, free on a public repo, 01:00 and 13:00 local): scripts in `bank/` become 3D two-person reels (50 locations), chat reels, list reels, carousels, 4:5 posters and 9:16 stories, with TTS voice, covers and a never-reused comment keyword per post (`build.py with_kw()` -> `manifest.kwmap`). Served by GitHub Pages (`manifest.json` + `media/`).
- **Autopilot** (Cloudflare Worker, cron every minute, KV, free Workers AI): staged posting schedule, keyword comment -> private DM + public reply, qualifying DM chat, check-ins for people who go quiet, lead alerts to Discord (@everyone so the phone notifies), daily insights + optimiser, `/public/insights` for the script writer, privacy/terms/data-deletion pages, "delete" in DM erases the person's data.
- **Two Claude scheduled tasks**: refill writer and monitor (step 6).

## Run order after "start"
Use a task list. Ask only where the answer is the owner's (business facts, preferences) or a screen needs their click or password. Use the browser for account steps; the owner is already logged in.

### 1. Short interview (one message)
Business and offer; city/region; content language and call language(s); 4-6 customer types and the real situations they are in; what must never be said (default: prices/fees; price is shared only on the owner's call); what each of 4 comment keywords delivers in DM (a guide, checklist, tips); qualifying questions and what makes a lead complete (default: need, team, traction, timeline, phone, call language); target posts/day (recommend a staged ramp from ~15 to the target over 3-4 weeks, max ~45/day); time zone.

### 2. Niche research (the only research)
Official sources for the facts content may use (list them in `business.json content.facts`, sources in the commit message; never invent). What the audience searches and worries about, competitor hooks, local places and names for scenes.

### 3. Repo and config
Create the owner's repo from the template (`gh repo create <owner>/<name> --template Shaazamaan/instagram-lead-autopilot --public`, or "Use this template"; public = free Actions minutes and Pages). Enable Pages with the GitHub Actions source.
- Fill `business.json`: brand, timezone, quiet hours, language (fonts: `python3 setup/fonts.py <script>`, then check every glyph renders with RAQM; symbols like currency signs or emoji may not; voices: `setup/LANGUAGES.md`, render one line per voice and listen), segments, keywords (aliases = regexes for native-script spellings and typos), dm texts, bot questions, call_languages, phone_regex for the country, flag (e.g. NRI / abroad), schedule.stages with real dates, ui strings translated, facts, forbidden_words. Optional `scene_names` per location with local names. Colours live in `factory/carousel.py` / `poster.py`.
- Locations: `factory/duo3d.py` SCENES; the `render-scenes` workflow renders stills with Blender (bpy). Add or swap locations so they fit the audience's daily life.
- Secrets: `CLOUDFLARE_API_TOKEN` (Workers + KV edit), `IG_TOKEN`, `DISCORD_WEBHOOK`, `HF_TOKEN`. Variables after step 4: `WORKER_URL`, `IG_USER_ID`.

### 4. Meta + Cloudflare (solved steps; follow exactly)
1. Publisher app on developers.facebook.com (Business type) with the Instagram Graph API: content publish, comments, insights, messaging. Long-lived Page token -> `IG_TOKEN`. IG user id from `/me/accounts?fields=instagram_business_account`. Make the app Live.
2. `node setup/configure.mjs <owner>/<repo> <IG_USER_ID> <workers-subdomain>` (fills `wrangler.toml`, writes the ops key to `~/.autopilot_ops_key`; only its SHA-256 is stored; never print or commit the key). Commit, set the two repo variables, push: `deploy-autopilot` creates KV, bundles business.json (`setup/gen-config.mjs`) and deploys.
3. DMs: Meta only delivers message webhooks to a **Published** app with messaging access. Route without App Review: a second app with **Instagram login**, add the IG account as **Instagram Tester** (not admin), the owner accepts it in the Instagram app (Settings > Website permissions > Apps and websites > Tester invites), generate that app's token and store it with `POST /ops/settoken` (header `x-ops-key`; refreshed weekly by the worker). Keep this app Published.
4. Webhooks on both apps: callback `<WORKER_URL>/webhook`, verify token from `wrangler.toml`, fields `comments` and `messages`; call `subscribed_apps` for the account. Backup route: inbox polling every 10 s, `POST /ops/flag {"k":"poll_inbox","v":true}`.
5. Privacy, terms and data-deletion URLs for Meta's forms: `<WORKER_URL>/privacy`, `/terms`, `/data-deletion`.
6. Owner: Instagram allows message requests; optionally turns off "Call on Instagram" (the bot cannot control it).

### 5. First content
Replace every example bank with real ones: `bank/batch*.py` (reels: duo3d / chat / list), `carousels*.py` (C), `posters*.py` (P: fact / myth / deadline / check), `stories*.py` (T: tip / quiz / contact). Aim for 2 weeks at stage 1. ICP-first, verified facts only, no forbidden words, location fits the person, never the same location twice in a row, every item ends with a general keyword CTA. Validate with `load_bank()`, `load_carousels()`, `load_posters()`, `load_stories()` in `factory/build.py`; render 3 of each still format and look at them. Run `render-scenes` if locations changed, then `reel-factory` (workflow_dispatch; one run builds ~60 reels in ~5 h). Watch the first reel and listen to the voice before the first post.

### 6. Scheduled tasks (owner's time zone)
- **Refill writer** (Opus, every 4 h): keep a 2-week backup at the current stage (built + unbuilt; full-volume targets = 14 x daily counts; built reel stock capped ~250 because Pages is ~1 GB at ~2.5 MB/reel); up to 40 reels/15 carousels/10 posters/10 stories per run; same content rules; validate and push. Audience-led: read `<WORKER_URL>/public/insights`; act only after 14 days and 40 posts judged at 2+ days; rank by leads (high-intent first) per 1,000 reach, then keyword comments/DMs, then shares/saves; give clear winners (>= 1.5x median on 5+ posts) up to 60% of new writing, keep >= 25% exploration, never drop a segment, reverse shifts the data stops supporting, log decisions with counts in `bank/INSIGHTS.md`, notify the owner on each shift.
- **Monitor** (Opus, every 3 h during the ramp, 6 h when stable): posts vs `/ops/run {"what":"slots"}`, workflow failures, worker log (`/ops/status`) errors and NO STOCK, lead alerts, reach after each stage step (hold with `/ops/flag stage_hold` if reach/post falls > 40% or spam/limit errors), stock runway per type (hold the next step if < 2 days), fix real problems via an Opus subagent, push only the fix, notify only on failure.

### 7. Verify, then hand over
Before deploying worker changes, simulate the DM and check-in flows in Node (mock `fetch`, KV and `Date`, and await `ctx.waitUntil` work). Once live, from a second Instagram account: comment a keyword on a live post and check the DM, public reply, follow gate, full question flow, lead alert on the owner's phone, and a check-in after going quiet. Tell the owner plainly what was verified live and what only in simulation. Their job from now: call each lead from Discord and tell Claude `lead <id>: <outcome>` within 24 h; keep the Instagram-login app Published; re-login if Meta asks; decide later on Meta App Review for more reliable DMs from strangers.

## Known pitfalls (already handled in the template; do not undo)
- Both apps can deliver the same comment: dedupe by comment id and message id, never by message text (it swallows a second button tap).
- One private reply per comment; DMs only within 24 h of the person's last message; quick-reply titles <= 20 chars; ~100 API posts/24 h per account (some docs say 50; check `content_publishing_limit`).
- Lead alert waits for the call language and fires once per Instagram account; a partial lead with a phone number alerts at its first check-in.
- Check-ins: 2 h / 9 h / 22 h of silence, restating the exact question they stopped on; none in quiet hours; "stop" opts out; comment-only people get one public nudge.
- Free Workers AI covers ~8-9 full DM chats a day; the fixed-question fallback still collects the phone number.
- Media publishes when a factory run ends (~5 h): keep stock ahead; `/ops/extra` can post stop-gap carousels.
- Claude usage is spent on script writing and monitoring only; building, posting and DMs run free. If usage runs out, posting continues from backup.
