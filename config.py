import os

from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GEMINI_MODEL = "gemini-2.5-flash"

CACHE_DIR = "cache"

EXPORT_DIR = "exports"

CHUNK_SIZE = 900

CHUNK_OVERLAP = 200

TOP_K = 5