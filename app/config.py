import os

# Retrieval
TOP_K = int(os.getenv("TOP_K", "3"))

# Generation
MODEL_NAME     = os.getenv("MODEL_NAME", "distilgpt2")
MAX_NEW_TOKENS = int(os.getenv("MAX_NEW_TOKENS", "128"))
TEMPERATURE    = float(os.getenv("TEMPERATURE", "0.7"))
TOP_P          = float(os.getenv("TOP_P", "0.9"))
REPEAT_PENALTY = float(os.getenv("REPEAT_PENALTY", "1.2"))

# FAISS index persistence
INDEX_PATH = os.getenv("INDEX_PATH", "faq.index")

# Server
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))
