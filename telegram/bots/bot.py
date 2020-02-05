import telegram
from decouple import config

bot = telegram.Bot(config('TOKEN'))

print(bot.get_me())