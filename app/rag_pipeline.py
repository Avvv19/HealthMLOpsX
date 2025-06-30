import time
import faiss
import numpy as np
import pandas as pd
from transformers import pipeline
from sentence_transformers import SentenceTransformer
from typing import List, Dict, Any

from app import config

# ————————————————
# 1) Initialize components
# ————————————————

generator = pipeline(
    "text-generation",
    model=config.MODEL_NAME,
    device=0,                   # set to -1 if you want CPU-only
    framework="pt"
)

embedder = SentenceTransformer('all-MiniLM-L6-v2')

# Example FAQ data; replace with your real source (CSV, DB, etc.)
faq_df = pd.DataFrame({
    "id":   [0, 1, 2],
    "text": [
        "Wash your hands regularly to prevent infection.",
        "Get vaccinated against common diseases.",
        "Exercise regularly for good heart health."
    ]
})

# ————————————————
# 2) Index build / load / save
# ————————————————

def build_faiss_index(texts: List[str]) -> faiss.IndexFlatL2:
    embs = embedder.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True
    ).astype('float32')
    idx = faiss.IndexFlatL2(embs.shape[1])
    idx.add(embs)
    return idx

def save_faiss_index(idx: faiss.IndexFlatL2, path: str) -> None:
    faiss.write_index(idx, path)

def load_faiss_index(path: str) -> faiss.IndexFlatL2:
    return faiss.read_index(path)

# Attempt to load on startup, else build & persist
try:
    index = load_faiss_index(config.INDEX_PATH)
except (OSError, IOError):
    index = build_faiss_index(faq_df["text"].tolist())
    save_faiss_index(index, config.INDEX_PATH)

# ————————————————
# 3) Retrieval + generation
# ————————————————

def retrieve_top_k(query: str, k: int = None) -> List[Dict[str, Any]]:
    k = k or config.TOP_K
    q_emb = embedder.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True
    ).astype('float32')
    distances, indices = index.search(q_emb, k)
    results = []
    for dist, idx in zip(distances[0], indices[0]):
        results.append({
            "id":    int(faq_df.at[idx, "id"]),
            "text":  faq_df.at[idx, "text"],
            "score": float(dist)
        })
    return results

def format_answer(raw: str) -> str:
    lines = [l for l in raw.splitlines() if not l.lower().startswith("context:")]
    cleaned = " ".join(lines).strip()
    if "Question:" in cleaned:
        cleaned = cleaned.split("Question:")[0].strip()
    return cleaned

def generate_answer(query: str, top_k: int = None) -> Dict[str, Any]:
    start = time.time()
    sources = retrieve_top_k(query, top_k)
    context = " ".join([s["text"] for s in sources])

    prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
    raw = generator(
        prompt,
        max_new_tokens=config.MAX_NEW_TOKENS,
        do_sample=True,
        temperature=config.TEMPERATURE,
        top_p=config.TOP_P,
        repetition_penalty=config.REPEAT_PENALTY
    )[0]["generated_text"]

    answer = format_answer(raw)
    duration_ms = int((time.time() - start) * 1000)

    return {
        "query":       query,
        "answer":      answer,
        "sources":     sources,
        "duration_ms": duration_ms
    }
