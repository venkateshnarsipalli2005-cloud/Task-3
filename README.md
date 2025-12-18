# Task-3

This workspace contains a simple chatbot project with sample FAQ data, a Dialogflow setup guide, a Streamlit demo that serves the bot locally (with OpenAI fallback), and a Telegram example integration.

Files added:
- `sample_faq.csv` - sample questions/answers used by the bot
- `dialogflow_instructions.md` - step-by-step Dialogflow setup and testing notes
- `streamlit_app.py` - a small Streamlit demo using FAQ matching + OpenAI fallback
- `telegram_example.py` - an example Telegram polling bot using the same FAQ + fallback
- `requirements.txt` - Python dependencies for the demo

See the `dialogflow_instructions.md` for instructions about creating a Dialogflow agent and importing training phrases. To run the local Streamlit demo, install dependencies and run:

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Set `OPENAI_API_KEY` in your environment for OpenAI fallback responses. For Telegram testing, set `TELEGRAM_BOT_TOKEN` and run `telegram_example.py`.
# Task-3