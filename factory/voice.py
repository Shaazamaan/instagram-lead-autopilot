"""Voices (language from business.json) with AI4Bharat Indic Parler-TTS (Apache-2.0). Caches every line by content hash."""
import os, hashlib
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.environ.get("VOICE_CACHE", f"{ROOT}/.voice_cache")
os.makedirs(CACHE, exist_ok=True)

import json
_C = json.load(open(f"{ROOT}/business.json", encoding="utf-8"))["language"]
FEMALE = set(_C.get("female_names", []))
_F, _M = _C["tts_female"], _C["tts_male"]
STYLE = "speaks in a very lively, animated and expressive way at a fast pace, with natural rises and falls in pitch, like excitedly chatting with a close friend. The audio is very clear and close-sounding with no background noise."
VOICES = {
    "F1": f"{_F} {STYLE} Her pitch is moderate.",
    "F2": f"{_F} {STYLE} Her pitch is slightly high and her tone is bright.",
    "M1": f"{_M} {STYLE} His tone is friendly and teasing, with a moderate pitch.",
    "M2": f"{_M} {STYLE} His pitch is slightly low and his tone is calm.",
    "NARRATOR": f"{_F} speaks clearly and confidently at a moderate pace, like explaining something useful to a friend. The recording is close-sounding with very little background noise.",
}

def voice_for(name, slot):
    g = "F" if name in FEMALE else "M"
    return f"{g}{1 + slot % 2}"

_model = None
def _load():
    global _model
    if _model is None:
        import torch
        from parler_tts import ParlerTTSForConditionalGeneration
        from transformers import AutoTokenizer
        torch.set_num_threads(int(os.environ.get("TTS_THREADS", "2")))
        m = "ai4bharat/indic-parler-tts"
        model = ParlerTTSForConditionalGeneration.from_pretrained(m)
        _model = (model, AutoTokenizer.from_pretrained(m), AutoTokenizer.from_pretrained(model.config.text_encoder._name_or_path))
    return _model

def say(text, voice):
    key = hashlib.sha1(f"{voice}|{VOICES[voice]}|{text}".encode()).hexdigest()[:16]
    out = f"{CACHE}/{key}.wav"
    if os.path.exists(out): return out
    import torch, soundfile as sf
    model, tok, dtok = _load()
    d = dtok(VOICES[voice], return_tensors="pt"); p = tok(text, return_tensors="pt")
    for tryno in range(4):   # the model now and then returns (almost) no audio: try other seeds
        torch.manual_seed(int(key[:6], 16) + tryno * 7919)
        a = model.generate(input_ids=d.input_ids, attention_mask=d.attention_mask, prompt_input_ids=p.input_ids, prompt_attention_mask=p.attention_mask)
        a = a.cpu().numpy().reshape(-1)
        if a.size > 0.3 * model.config.sampling_rate: break
    else:
        raise RuntimeError(f"no audio for line: {text[:40]}")
    sf.write(out + ".tmp.wav", a, model.config.sampling_rate); os.replace(out + ".tmp.wav", out)
    return out
