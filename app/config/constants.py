"""
Application-wide constants.
"""

# -----------------------------
# Transcript Block Settings
# -----------------------------

MAX_BLOCK_CHARS = 1000
MAX_BLOCK_DURATION = 60

# -----------------------------
# Chunk Settings
# -----------------------------

CHUNK_SIZE = 800
CHUNK_OVERLAP = 150

# -----------------------------
# Retrieval
# -----------------------------

TOP_K = 5

# -----------------------------
# ChromaDB
# -----------------------------

COLLECTION_NAME = "youtube_rag"

# -----------------------------
# Gemini Models
# -----------------------------

LLM_MODEL = "gemini-2.5-flash"

# Latest embedding model
EMBEDDING_MODEL = "gemini-embedding-001"