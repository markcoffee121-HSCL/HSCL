Common Issues, Quick fixes.

GOOGLE_API_KEY is missing
→ Check your .env file. Make sure it looks like:

GOOGLE_API_KEY=AIza...yourkey
GEMINI_MODEL=gemini-1.5-flash


(No quotes, no extra spaces!)

OPENAI_API_KEY is missing
→ Same as above but for OpenAI. If you don’t have credits, ignore this error — Gemini will handle requests.

Model not found
→ Use a supported model name. Recommended:

Gemini: gemini-1.5-flash (fast, free) or gemini-1.5-pro (smarter).

OpenAI: gpt-4o-mini (budget-friendly) or gpt-4o.

403 / Permission denied
→ Usually means your API key is wrong or not enabled.
Double-check in Google AI Studio API keys
.

429 / Quota exceeded

Gemini: You hit your free monthly limit (check usage
).

OpenAI: Out of credits — add billing or wait until more credits refresh.

Connection / Timeout
→ Check your internet or firewall. Some corporate networks block these calls.
Try from a personal hotspot if needed.

Local Setup Issues

ModuleNotFoundError: No module named '...'
→ You forgot to install packages. Run:

pip install -r requirements.txt


venv not active
→ Make sure you see (.venv) in your PowerShell prompt.
If not, run:

.\.venv\Scripts\Activate.ps1