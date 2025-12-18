import os
import difflib
import logging
import pandas as pd

try:
    import openai
except Exception:
    openai = None

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

DATA_PATH = "sample_faq.csv"

def load_faq(path=DATA_PATH):
    return pd.read_csv(path)

def find_best_answer(faq_df, query, cutoff=0.6):
    questions = faq_df['question'].astype(str).tolist()
    matches = difflib.get_close_matches(query, questions, n=1, cutoff=cutoff)
    if matches:
        matched = matches[0]
        row = faq_df[faq_df['question'] == matched].iloc[0]
        return row['answer']
    return None

def openai_fallback(query):
    key = os.environ.get('OPENAI_API_KEY')
    if not key or openai is None:
        return "(No OpenAI API key set; enable OPENAI_API_KEY for fallback.)"
    openai.api_key = key
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful customer support assistant."},
                      {"role": "user", "content": query}],
            max_tokens=200,
            temperature=0.2,
        )
        return resp['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"(OpenAI request failed: {e})"

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello — I am a sample FAQ bot. Ask me about orders, returns, or shipping.')

def handle_message(update: Update, context: CallbackContext):
    faq = context.bot_data.get('faq')
    txt = update.message.text.strip()
    ans = find_best_answer(faq, txt)
    if ans:
        update.message.reply_text(ans)
    else:
        update.message.reply_text('(No FAQ match; trying fallback)')
        fb = openai_fallback(txt)
        update.message.reply_text(fb)

def main():
    token = os.environ.get('TELEGRAM_BOT_TOKEN')
    if not token:
        print('Set TELEGRAM_BOT_TOKEN environment variable.')
        return
    logging.basicConfig(level=logging.INFO)
    updater = Updater(token)
    dp = updater.dispatcher

    faq = load_faq()
    dp.bot_data['faq'] = faq

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    print('Starting bot (polling). Press Ctrl-C to stop.')
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
