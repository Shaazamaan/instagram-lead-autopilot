"""Fetch the Anek font for the content language from Google Fonts (OFL) and cut 600/800 weights.
Usage: python3 setup/fonts.py <language>   e.g. malayalam, tamil, telugu, kannada, devanagari (Hindi/Marathi), bangla, gujarati, gurmukhi (Punjabi), odia, latin (English only)
Writes assets/fonts/anek-<language>-<script>-600/800.ttf and anek-<language>-latin-600/800.ttf, then set business.json language.font_prefix = "anek-<language>", font_script = "<language>"."""
import sys, os, io, urllib.request
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
lang = sys.argv[1].lower(); root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
name = "Anek" + ("Latin" if lang == "latin" else lang.capitalize())
url = f"https://raw.githubusercontent.com/google/fonts/main/ofl/{name.lower()}/{name}%5Bwdth,wght%5D.ttf"
data = urllib.request.urlopen(url, timeout=60).read()
for wt in (600, 800):
    f = instancer.instantiateVariableFont(TTFont(io.BytesIO(data)), {"wght": wt, "wdth": 100})
    for script in {lang, "latin"}:
        out = f"{root}/assets/fonts/anek-{lang}-{script}-{wt}.ttf"; f.save(out); print("wrote", out)
