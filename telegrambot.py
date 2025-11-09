from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import re
import openai
import os
TELEGRAM_BOT_TOKEN = os.environ['8006202416:AAFtwdOVjNLZCv15gn39_-E9LtyT1XfydKY']
OPENAI_API_KEY =  os.environ['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']

openai.api_key = OPENAI_API_KEY

updater = Updater("TELEGRAM_BOT_TOKEN",
                  use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "welecom it is my /gmail")

def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text("pwrya6162@gmail.com")

def check_links(update: Update, context: CallbackContext):
    text = update.message.text
    if re.search(r"http[s]?://|www\.", text):
        try:
            context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
            print("لینک حذف شد:", text)
        except Exception as e:
            print("خطا در حذف پیام:", e)
def chatgpt_reply(update: Update, context: CallbackContext):
    user_message = update.message.text
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        bot_answer = response.choices[0].message["content"].strip()
    except Exception as e:
        bot_answer = 'متاسفم، مشکلی پیش آمده است.'
    update.message.reply_text(bot_answer)



updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), check_links))
updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command) & (~Filters.regex(r"http[s]?://|www\.") ), chatgpt_reply))


updater.start_polling()







