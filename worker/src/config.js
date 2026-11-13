// generated from business.json by setup/gen-config.mjs; do not edit
export default {
 "_readme": "Everything business-specific lives here. Setup fills it from the owner interview; nothing else in the repo names the business. After editing run: node setup/gen-config.mjs",
 "brand": {
  "handle": "your.instagram.handle",
  "display_name": "Your Business Name",
  "what_we_do": "<one line: what the business does and where>",
  "topic_phrase": "<topic, e.g. home loans>",
  "hashtags": "#niche #city #smallbusiness"
 },
 "timezone_offset_hours": 5.5,
 "quiet_hours": [
  22,
  8
 ],
 "language": {
  "name": "Malayalam",
  "font_prefix": "anek-malayalam",
  "font_script": "malayalam",
  "unicode_range": [
   "ഀ",
   "ൿ"
  ],
  "tts_female": "Anjali",
  "tts_male": "Harish",
  "female_names": [
   "Anu",
   "Meera",
   "Riya",
   "Mom",
   "Sister"
  ],
  "default_names": {
   "F": [
    "Anu",
    "Meera"
   ],
   "M": [
    "Vishnu",
    "Rahul"
   ]
  },
  "comment_word": "comment",
  "letter_names": {
   "A": "എ",
   "B": "ബി",
   "C": "സി",
   "D": "ഡി",
   "E": "ഇ",
   "F": "എഫ്",
   "G": "ജി",
   "H": "എച്ച്",
   "I": "ഐ",
   "J": "ജെ",
   "K": "കെ",
   "L": "എൽ",
   "M": "എം",
   "N": "എൻ",
   "O": "ഒ",
   "P": "പി",
   "Q": "ക്യു",
   "R": "ആർ",
   "S": "എസ്",
   "T": "ടി",
   "U": "യു",
   "V": "വി",
   "W": "ഡബ്ല്യു",
   "X": "എക്സ്",
   "Y": "വൈ",
   "Z": "സെഡ്"
  },
  "read_as_words": [
   "START",
   "AFTER",
   "NAME",
   "CHECKLIST",
   "DONE",
   "STOP"
  ],
  "_letters_note": "How the voice says each capital letter of an acronym (NRI -> N R I). Write the letter names in the content language; leave empty to use plain Latin letters.",
  "male_names": [
   "Vishnu",
   "Rahul",
   "Arjun",
   "Dad",
   "Brother"
  ],
  "address_words": {
   "_note": "Words that only make sense said TO a woman / TO a man (e.g. Malayalam ചേച്ചി / ചേട്ടാ). check_bank.py flags a mismatch.",
   "to_female": [],
   "to_male": []
  },
  "_note": "font_script must match assets/fonts/<font_prefix>-<font_script>-600/800.ttf (setup/fonts.py). Every person name used anywhere must be in female_names or male_names (voice gender is never guessed)."
 },
 "segments": [
  "freelancer",
  "cofounders",
  "proprietor",
  "salaried",
  "solo",
  "nri"
 ],
 "keywords": [
  {
   "word": "START",
   "aliases": [],
   "opener": "Hi! Thanks for your comment. Want our quick guide? Tap the button below.",
   "reply": "Here you go!\n\n<the resource promised by posts that use START>\n\nWhat does your business do?",
   "cta_line": "We'll tell you which option suits you"
  },
  {
   "word": "NAME",
   "aliases": [],
   "opener": "Hi! Thanks for your comment. Want our tips? Tap the button below.",
   "reply": "Here you go!\n\n<resource for NAME>\n\nWhat name do you have in mind?",
   "cta_line": "Get our tips by DM"
  },
  {
   "word": "AFTER",
   "aliases": [],
   "opener": "Hi! Thanks for your comment. Want the checklist? Tap the button below.",
   "reply": "Here you go!\n\n<resource for AFTER>\n\nHow far along are you?",
   "cta_line": "Get the checklist by DM"
  },
  {
   "word": "CHECKLIST",
   "aliases": [],
   "opener": "Hi! Thanks for your comment. Want the list? Tap the button below.",
   "reply": "Here you go!\n\n<resource for CHECKLIST>\n\nHow many people are starting it?",
   "cta_line": "Get the list by DM"
  }
 ],
 "keyword_stopwords": [
  "star",
  "stars",
  "stat",
  "stats",
  "smart",
  "same",
  "came",
  "game",
  "name",
  "alter",
  "hater"
 ],
 "long_comment_exact_only": [
  "AFTER"
 ],
 "dm": {
  "public_reply": "Thanks! Message us \"Hi\" (tap Message on our profile) and we'll send it right away.",
  "public_done": [
   "Sent you a DM. Not in your inbox? Check message requests, including hidden requests.",
   "Just messaged you! If you can't see it, look in message requests or hidden requests.",
   "Check your DMs. Instagram sometimes puts it under requests or hidden requests."
  ],
  "follow_gate": true,
  "follow_ask": "Almost there! Please follow us (we share a useful tip every day), then tap the button below and we'll send it right away.",
  "follow_recheck": "Hmm, we can't see your follow yet. Open our profile, tap Follow, then tap the button again.",
  "followed_button": "I've followed ✅",
  "next_buttons": [
   "Talk to our team",
   "Which suits me?",
   "What's needed?"
  ],
  "delete_done": "Done. We have deleted your conversation and details from our system.",
  "opt_out_reply": "No problem. We won't send you any more reminders. If you need us later, just message here.",
  "nudge_open": [
   "Hey, just checking in 👋 We were halfway through our chat and didn't want to leave you hanging.",
   "Hi again 🙂 No rush at all. One quick answer and we can take this forward for you.",
   "Last check from our side 🙏 If you'd still like our team to call you, just reply here and we'll pick up where we stopped."
  ],
  "nudge_public": [
   "just checking 👋 did our DM reach you? It may be in message requests (or hidden requests). Reply there and we'll take it forward.",
   "quick check 🙂 we sent what you asked for by DM. If you can't see it, look in message requests, then reply there."
  ]
 },
 "bot": {
  "reply_language": "simple, friendly English",
  "never_say": "any price, fee, cost, discount or government fee",
  "price_reply": "Our team will share the exact quote on a call once they understand your needs.",
  "price_words": "price|fee|cost|charge|rate|how much",
  "extra_rules": "Never give legal advice beyond general facts.",
  "questions": [
   {
    "key": "business",
    "ask": "What does your business do? Tell us in a line or two."
   },
   {
    "key": "team",
    "ask": "How many people are starting it? Is anyone living abroad?"
   },
   {
    "key": "traction",
    "ask": "Does the business already have income, clients or funding?"
   },
   {
    "key": "timeline",
    "ask": "How soon do you want to get started?"
   },
   {
    "key": "phone",
    "ask": "Could you share a phone number so our team can call you?"
   },
   {
    "key": "language",
    "ask": "Would you prefer the call in Malayalam or English?"
   }
  ],
  "done": "Thank you! 🙏 Our team will call you shortly.",
  "call_languages": [
   "Malayalam",
   "English"
  ],
  "phone_regex": "(?:\\+?91)?[6-9]\\d{9}",
  "flag": {
   "label": "NRI",
   "regex": "nri|abroad|gulf|dubai|saudi|qatar|uae|oman|kuwait"
  },
  "negative_regex": "^(no|not|nothing|none|illa)",
  "soon_regex": "asap|soon|immediately|this (week|month)|now|urgent"
 },
 "schedule": {
  "stages": [
   {
    "from": "2026-01-01",
    "reel": 5,
    "carousel": 5,
    "story": 5,
    "poster": 2
   }
  ],
  "story_times": [
   [
    8,
    10
   ],
   [
    13,
    5
   ],
   [
    18,
    10
   ],
   [
    20,
    15
   ],
   [
    22,
    10
   ]
  ],
  "window": [
   [
    7,
    5
   ],
   [
    22,
    45
   ]
  ]
 },
 "content": {
  "facts": [
   "List only facts you have verified from official sources, one per line. Scripts may use nothing else."
  ],
  "forbidden_words": [
   "price",
   "fee",
   "cheap",
   "affordable",
   "discount"
  ],
  "rules": "Never state a service price. Only statutory numbers (penalties, deadlines) may appear.",
  "amount_regex": "(\\S+) (?:rupees|Rs\\.?)",
  "allowed_amounts": [],
  "_amounts_note": "Every money amount in a script must be listed in allowed_amounts (statutory penalties etc.); anything else is treated as a forbidden price."
 },
 "ui": {
  "_note": "All on-screen words the factory draws. Translate into the content language during setup.",
  "or": "or",
  "comment_cta": "comment",
  "reply_cta": "reply",
  "swipe": "Swipe  >>",
  "default_tag": "Good to know",
  "badge_story": "A short story",
  "badge_chat": "Chat story",
  "badge_list": "Checklist",
  "story_new_reel": "New reel",
  "story_go_profile": "Watch it on our profile 👆",
  "story_tip": "Today's tip",
  "story_quiz": "Quiz",
  "story_answer": "Answer",
  "story_contact": "Ask us",
  "follow_for_more": "Follow for more tips like this",
  "quiz_foot": "Answer in the next story. Reply with yours",
  "dm_foot": "We'll reply in your messages",
  "myth_label": "What people say",
  "truth_label": "The truth",
  "numbers": [
   "One",
   "Two",
   "Three",
   "Four",
   "Five"
  ]
 },
 "kw_pool_extra": [],
 "engagement": {
  "comment_reply_cap_per_day": 150,
  "per_person_per_day": 2,
  "emoji_replies": [
   "🙌",
   "❤️ Thank you!",
   "😊🙏",
   "Thank you! 🙌"
  ],
  "fallback_replies": [
   "Thank you! 🙌",
   "Glad this helped 😊 Comment START if you want our free guide.",
   "Thanks a lot! 🙏 DM us anytime if you need help.",
   "Appreciate it 😊 More tips coming every day!"
  ],
  "story_thanks": "Thanks a lot for sharing us in your story! 🙌 If you or a friend need help, just reply here."
 }
};
