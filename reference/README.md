# Reference: multi-topic + reel-max mode (from the rejectionlist.kerala build, 19 Nov 2026)

These are working files from a live deployment where 5 services share one Instagram account. They are for reference only; the template's own files are single-topic.
- worker_index_multitopic.js: see TOPICS, planDay, reelMaxPlan (REEL_RAMP / REEL_SHARE), slotsFor (multi-topic), quotaLeft, KW_TOPIC, BOT / FALLBACK / LEAD_SCHEMA / NEXT per topic, snapshot (day 2 + 7, judged index)
- topics.py: per-topic folders, stock share, keywords, CTAs, segments and fact lists
- build.py / captions.py / check_bank.py: topic-tagged loaders, per-topic stock, captions and checks
- OPS_RULES.md: the standing rules the scheduled tasks read first
Business-specific wording is the original client's; adapt it per business.json. No keys, tokens or client data are included.
