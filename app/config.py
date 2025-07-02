import os

TOP_K = int(os.getenv("TOP_K", "3"))
MODEL_NAME = os.getenv("MODEL_NAME", "distilgpt2")
MAX_NEW_TOKENS = int(os.getenv("MAX_NEW_TOKENS", "128"))
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
TOP_P = float(os.getenv("TOP_P", "0.9"))
REPEAT_PENALTY = float(os.getenv("REPEAT_PENALTY", "1.2"))
INDEX_PATH = os.getenv("INDEX_PATH", "faq.index")
