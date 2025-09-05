# HSCL – Day 0 (Environment & AI Fundamentals)

## Setup
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

Create a .env:

GOOGLE_API_KEY=AIza...yourkey
GEMINI_MODEL=gemini-1.5-flash

Test
python src\hello_agent.py

Troubleshooting

See troubleshooting.md.