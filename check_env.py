import os
from dotenv import load_dotenv
load_dotenv()
print("Has GOOGLE_API_KEY:", bool(os.getenv("GOOGLE_API_KEY")))
print("Model:", os.getenv("GEMINI_MODEL", "gemini-1.5-flash"))
