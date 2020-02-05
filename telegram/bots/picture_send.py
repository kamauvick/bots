from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
from decouple import config
import logging


# Get random dog image

def get_url():
    _url = 'https://random.dog/woof.json'

    contents = requests.get(_url).json()
    print(contents)
    image_url = contents['url']
    return image_url

# Send the image    

def bop(update, context):
    url = get_url()
    if url:
        chat_id = update.effective_chat.id

        context.bot.send_photo(chat_id=chat_id, photo=url)
        context.bot.send_chat_action(
            chat_id=chat_id, action=telegram.ChatAction.TYPING)
    else:
        context.bot.send_message(
            chat_id=chat_id, text="I'm sorry Vick I'm afraid I can't do that.")


# Main runner fx

def main():
    token = config('TOKEN')

    updater = Updater(token=token, use_context=True)
    dp = updater.dispatcher
    start_handler = CommandHandler('bop',bop)
    dp.add_handler(start_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()




