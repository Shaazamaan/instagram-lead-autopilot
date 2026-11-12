# Content languages

On-screen text uses the Anek font family (Google Fonts, OFL). Voice uses AI4Bharat Indic Parler-TTS.

| Language | `python3 setup/fonts.py <arg>` | unicode_range | TTS speakers (female, male) to try first |
|---|---|---|---|
| Malayalam | malayalam | ["ഀ","ൿ"] | Anjali, Harish (bundled fonts) |
| Tamil | tamil | ["஀","௿"] | Jaya, Prakash |
| Telugu | telugu | ["ఀ","౿"] | Lalitha, Prakash |
| Kannada | kannada | ["ಀ","೿"] | Anu, Suresh |
| Hindi / Marathi | devanagari | ["ऀ","ॿ"] | Divya, Rohit (Hindi); Sunita, Sanjay (Marathi) |
| Bengali | bangla | ["ঀ","৿"] | Aditi, Arjun |
| Gujarati | gujarati | ["઀","૿"] | Neha, Yash |
| Punjabi | gurmukhi | ["਀","੿"] | Divjot, Gurpreet |
| Odia | odia | ["଀","୿"] | Debjani, Manas |
| English only | latin | ["￿","￿"] | Mary, Thoma |

Speaker names come from the model card (huggingface.co/ai4bharat/indic-parler-tts); check it during setup, render one test line per voice and listen before bulk builds. Set `language.tts_female` / `tts_male`, and list typical female first names in `female_names` so dialogue gets the right voice.
