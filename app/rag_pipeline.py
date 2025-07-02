import faiss, time, pandas as pd
from transformers import pipeline
from sentence_transformers import SentenceTransformer
from app.config import *

generator = pipeline("text-generation", model=MODEL_NAME, device=-1)
embedder = SentenceTransformer("all-MiniLM-L6-v2")
faq_df = pd.DataFrame({
    "id": [0,1,2],
    "text": ["Wash hands.", "Get vaccinated.", "Exercise regularly."]
})

def build_index(texts):
    embs = embedder.encode(texts, normalize_embeddings=True).astype('float32')
    idx = faiss.IndexFlatL2(embs.shape[1])
    idx.add(embs)
    return idx

index = build_index(faq_df.text.tolist())


def generate_answer(query: str):
    # This is a stub — replace with LangChain + Pinecone logic
    sources = [
        {"id": 0, "text": "Example source 1", "score": 1.0},
        {"id": 1, "text": "Example source 2", "score": 0.9},
    ]
    return {
        "query": query,
        "answer": f"Stubbed answer for query: {query}",
        "sources": sources,
    }
