# Carousel bank 01. EXAMPLE ONLY: setup replaces it. Teach in steps, comparisons, myths or checklists.
import importlib.util, os
_b1 = importlib.util.spec_from_file_location("b1", os.path.join(os.path.dirname(__file__), "batch01.py")); _m = importlib.util.module_from_spec(_b1); _b1.loader.exec_module(_m)
CTA_START, CTA_NAME, CTA_AFTER, CTA_DOCS = _m.CTA_START, _m.CTA_NAME, _m.CTA_AFTER, _m.CTA_DOCS
C = []
def car(id, segment, tag, hook, slides, end, cta): C.append(dict(id=id, kind="carousel", segment=segment, tag=tag, hook=hook, slides=slides, end=end, cta=cta))

car("k001", "freelancer", "Step by step", "From idea to\nregistered:\n4 steps", [
 ("1. Pick the structure", "Based on how many people and your plans."),
 ("2. Choose a name", "Keep backups ready."),
 ("3. Collect documents", "ID, address proof, office proof."),
 ("4. File the application", "Then follow the first-year checklist.")],
 "We'll walk you\nthrough it", CTA_START)
