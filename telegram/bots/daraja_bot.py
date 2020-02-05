from telegram.ext import Updater, CommandHandler
from decouple import config


# Send the image

def bop(update, context):
    chat_id = update.effective_chat.id
    
    # Logic to get the username and password


# Send data to daraja-test --LNM api

def makePayment():
    # return payment data
    pass

# Main runner fx

def main():
    token = config('TOKEN')

    updater = Updater(token=token, use_context=True)
    dp = updater.dispatcher

    # Return payment data on telegram
    start_handler = CommandHandler('login', bop)
    dp.add_handler(start_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
