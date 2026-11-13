# Script bank, batch 01. EXAMPLE ONLY: setup replaces every script here with ones for the real business.
# Facts: scripts may use ONLY the facts listed in business.json content.facts (verified during setup). Never state a service price.
# kinds: duo3d (two people in one of the 3D locations in factory/duo3d.py), chat (message story), list (narrator checklist)
# Each script ends with one CTA tuple: (KEYWORD, one short line). The builder adds a unique per-post keyword automatically.
CTA_START = ("START", "We'll tell you which option suits you")
CTA_NAME = ("NAME", "Get our tips by DM")
CTA_AFTER = ("AFTER", "Get the checklist by DM")
CTA_DOCS = ("CHECKLIST", "Get the list by DM")

S = []
def duo(id, segment, bucket, scene, hook, lines, end, cta, names=None, sound=None):
    d = dict(id=id, kind="duo3d", scene=scene, names=names, segment=segment, bucket=bucket, hook=hook, lines=lines, end=end, cta=cta)
    if sound: d["sound"] = sound
    S.append(d)
def chat(id, segment, bucket, hook, names, lines, end, cta): S.append(dict(id=id, kind="chat", segment=segment, bucket=bucket, hook=hook, names=names, lines=lines, end=end, cta=cta))
def lst(id, segment, bucket, hook, items, end, cta): S.append(dict(id=id, kind="list", segment=segment, bucket=bucket, hook=hook, items=items, end=end, cta=cta))

# duo3d lines: (speaker "A" or "V", camera "wide" / "A" / "V", text). Speaker A/V use the scene's default names.
duo("d001", "freelancer", "A", "cafe", "വലിയ ക്ലയന്റ് ഓക്കെ പറഞ്ഞു.\nപിന്നെ ഒരു ചോദ്യം…", [
 ("A", "wide", "ഒടുവിൽ വലിയ ക്ലയന്റിനെ കിട്ടി!"),
 ("V", "V", "കൊള്ളാം! ഇന്ന് ചായ നിന്റെ വക."),
 ("A", "A", "ഒരു പ്രശ്നം. അവർ കമ്പനി രജിസ്ട്രേഷൻ ചോദിച്ചു."),
 ("V", "V", "അപ്പോ അയച്ചു കൊടുക്ക്."),
 ("A", "A", "ഉണ്ടായിരുന്നെങ്കിൽ അയച്ചേനെ."),
 ("V", "wide", "എന്നാൽ ഇന്നത്തെ പണി അതാ!")],
 "ക്ലയന്റ് ചോദിക്കും മുമ്പ്\nറെഡിയാകൂ", CTA_START)

chat("c001", "solo", "A", "പ്ലാൻ മാറ്റിയ\nഒരു മെസ്സേജ്", ("Riya", "Mom"), [
 (0, "അമ്മേ, ഞാൻ സ്വന്തം ബിസിനസ് തുടങ്ങുന്നു!"),
 (1, "നല്ലത്. രജിസ്റ്റർ ചെയ്തോ?"),
 (0, "ഇല്ല…"),
 (1, "ആദ്യ ദിവസം മുതൽ ശരിയായി ചെയ്യ്.")],
 "ശരിയായ രീതിയിൽ തുടങ്ങൂ", CTA_START)

lst("l001", "proprietor", "B", "ആദ്യം റെഡിയാക്കേണ്ട\n3 കാര്യങ്ങൾ", [
 ("ഐഡി രേഖകൾ", "എല്ലാവരുടെയും."),
 ("അഡ്രസ്സ് പ്രൂഫ്", "പുതിയ കറന്റ് ബിൽ."),
 ("പേരുകൾ", "2-3 ബാക്കപ്പ് പേരുകൾ.")],
 "ഇത് സേവ് ചെയ്യൂ", CTA_DOCS)
