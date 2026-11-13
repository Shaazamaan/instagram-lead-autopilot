"""Captions for every feed post (reels, carousels, posters), written for Instagram search, from business.json "captions".
Hook line, then one paragraph per language (topic or the script's own cap_<lang>, plus the audience line, plus the keyword
call to action), then at most 5 hashtags (Instagram's limit since Dec 2025). No prices: the text comes from business.json
and the scripts, both checked during setup."""
import zlib
from common import CFG
C = CFG["captions"]; H = C["hashtags"]

def _pick(xs, key): return xs[zlib.crc32(key.encode()) % len(xs)] if xs else None

def hashtags(item_id, base, segment):
    tags = [H["core"], _pick(H.get("local", []), item_id + "l"), _pick(H.get("topic", {}).get(base, []), item_id + "t"), H.get("segment", {}).get(segment)]
    tags = [t for t in tags if t]
    for x in [_pick(H.get("extra", []), item_id + "x")] + H.get("extra", []):
        if len(tags) >= 5: break
        if x and x not in tags: tags.append(x)
    return " ".join(dict.fromkeys(tags[:5]))

def caption(s, head):
    """s: script with id, segment, base, kw (optional cap_<lang>); head: first line people see."""
    base, kw, seg = s["base"], s["kw"], s.get("segment", "")
    t = C["topic"].get(base) or next(iter(C["topic"].values())); g = C["segment"].get(seg, {})
    parts = [head.strip()]
    for lang in C["languages"]:
        own = s.get("cap_" + lang)
        body = own or t.get(lang, "")
        para = body + (" " + g[lang] if g.get(lang) and not own else "")
        parts.append((para + "\n" + C["cta"][lang].format(base=base, kw=kw)).strip())
    parts.append(hashtags(s["id"], base, seg))
    out = "\n\n".join(p for p in parts if p)[:2200]
    assert out.count("#") <= 5, s["id"]
    return out
