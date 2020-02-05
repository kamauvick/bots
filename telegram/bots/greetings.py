from telegram.ext import Updater, CommandHandler
from decouple import config

def hello(update, context):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

token = config('TOKEN')
updater = Updater(token = token, use_context=True)
# bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
updater.dispatcher.add_handler(CommandHandler(('hello', 'hi', 'howdy',), hello))

updater.start_polling()
updater.idle()
