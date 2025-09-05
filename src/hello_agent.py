import os
from dotenv import load_dotenv

# --- Choose provider: Gemini first (free), fallback to OpenAI if configured ---
def use_gemini():
    import google.generativeai as genai
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

    if not api_key:
        raise SystemExit("GOOGLE_API_KEY is missing. Add it to your .env and try again.")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name)

    prompt = "Say a very brief hello and confirm my environment is working."
    try:
        resp = model.generate_content(prompt)
        # Some SDK versions return text at resp.text; others in candidates
        text = getattr(resp, "text", None)
        if not text and getattr(resp, "candidates", None):
            parts = resp.candidates[0].content.parts
            text = "".join(p.text for p in parts if hasattr(p, "text"))
        print(text.strip() if text else "Received a response, but it had no text.")
    except Exception as e:
        print("Gemini API call failed. Details below:")
        raise

def use_openai_fallback():
    from openai import OpenAI
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    if not api_key:
        raise SystemExit("Neither GOOGLE_API_KEY nor OPENAI_API_KEY is set. Add one to .env.")

    client = OpenAI(api_key=api_key)
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a concise, helpful AI agent."},
            {"role": "user", "content": "Say a very brief hello and confirm my environment is working."},
        ],
        temperature=0.2,
    )
    print(resp.choices[0].message.content.strip())

if __name__ == "__main__":
    # Prefer Gemini if GOOGLE_API_KEY exists; otherwise fallback to OpenAI if available
    load_dotenv()
    if os.getenv("GOOGLE_API_KEY"):
        use_gemini()
    else:
        use_openai_fallback()
