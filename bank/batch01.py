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
duo("d001", "freelancer", "A", "cafe", "Big client said yes.\nThen one question…", [
 ("A", "wide", "I finally got the big client!"),
 ("V", "V", "Great! Coffee is on you today."),
 ("A", "A", "One problem. They asked for my business registration."),
 ("V", "V", "So send it."),
 ("A", "A", "I would, if I had one."),
 ("V", "wide", "Then that's today's job!")],
 "Get ready before the\nbig client asks", CTA_START)

chat("c001", "solo", "A", "One message that\nchanged the plan", ("Riya", "Mom"), [
 (0, "Mom, I'm starting my own thing!"),
 (1, "Wonderful. Is it registered?"),
 (0, "Not yet…"),
 (1, "Do it properly from day one.")],
 "Start it the right way", CTA_START)

lst("l001", "proprietor", "B", "3 things to have\nready first", [
 ("ID documents", "For everyone involved."),
 ("Address proof", "A recent utility bill."),
 ("Name options", "Keep 2-3 backups.")],
 "Save this list", CTA_DOCS)
