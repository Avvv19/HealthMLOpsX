# tests/test_pipeline.py

import os
import tempfile
import faiss
import pytest

from app import config
from app.rag_pipeline import (
    build_faiss_index,
    save_faiss_index,
    load_faiss_index,
    retrieve_top_k,
    format_answer,
    generate_answer,
)

# Sample texts for index tests
SAMPLE_TEXTS = [
    "Hello world",
    "FastAPI is great",
    "Unit tests are important"
]

def test_build_and_save_load_index(tmp_path):
    # Build
    idx = build_faiss_index(SAMPLE_TEXTS)
    assert isinstance(idx, faiss.IndexFlatL2)
    assert idx.ntotal == len(SAMPLE_TEXTS)

    # Save to a temp file
    idx_file = tmp_path / "test.index"
    save_faiss_index(idx, str(idx_file))
    assert idx_file.exists()

    # Load and verify
    loaded = load_faiss_index(str(idx_file))
    assert isinstance(loaded, faiss.IndexFlatL2)
    assert loaded.ntotal == idx.ntotal

def test_retrieve_top_k():
    # Using the real FAQ index from rag_pipeline, but with k=1 on a known query
    results = retrieve_top_k("health", k=1)
    assert isinstance(results, list)
    assert len(results) == 1
    assert "text" in results[0] and "score" in results[0]

def test_format_answer():
    raw = "Context: foo\nAnswer: bar\nQuestion: baz?"
    cleaned = format_answer(raw)
    assert "Context:" not in cleaned
    assert "Question:" not in cleaned
    assert cleaned.startswith("Answer:")

def test_generate_answer_structure_and_speed():
    resp = generate_answer("How can I stay healthy?", top_k=2)
    # Check keys
    assert set(resp.keys()) == {"query", "answer", "sources", "duration_ms"}
    assert isinstance(resp["query"], str)
    assert isinstance(resp["answer"], str) and len(resp["answer"]) > 0
    assert isinstance(resp["sources"], list) and len(resp["sources"]) == 2
    assert isinstance(resp["duration_ms"], int)
    # Ensure duration is reasonable (< 5000 ms for a small test)
    assert resp["duration_ms"] < 5000
