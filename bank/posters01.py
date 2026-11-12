# Poster bank 01. EXAMPLE ONLY: setup replaces it. Layouts: fact | myth | deadline | check (factory/poster.py).
import importlib.util, os
_b1 = importlib.util.spec_from_file_location("b1", os.path.join(os.path.dirname(__file__), "batch01.py")); _m = importlib.util.module_from_spec(_b1); _b1.loader.exec_module(_m)
CTA_START, CTA_NAME, CTA_AFTER, CTA_DOCS = _m.CTA_START, _m.CTA_NAME, _m.CTA_AFTER, _m.CTA_DOCS
P = []
def fact(id, segment, tag, big, text, caption, cta): P.append(dict(id=id, layout="fact", segment=segment, tag=tag, big=big, text=text, caption=caption, cta=cta))
def myth(id, segment, myth, truth, caption, cta, tag="Myth vs truth"): P.append(dict(id=id, layout="myth", segment=segment, tag=tag, myth=myth, truth=truth, caption=caption, cta=cta))
def dead(id, segment, tag, big, text, caption, cta): P.append(dict(id=id, layout="deadline", segment=segment, tag=tag, big=big, text=text, caption=caption, cta=cta))
def check(id, segment, tag, title, items, caption, cta): P.append(dict(id=id, layout="check", segment=segment, tag=tag, title=title, items=items, caption=caption, cta=cta))

check("p001", "solo", "Checklist", "Before you\napply", ["ID for everyone involved", "Address proof", "2-3 name options"], "Save this.", CTA_DOCS)
