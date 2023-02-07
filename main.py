import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command

import config
import commands as cmd


# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s - %(message)s')

# Global obj
botConfig: config.BotConfig = config.BotConfig("bot-config.json")
bot: Bot = Bot(botConfig.token, parse_mode="HTML")


# Main
if __name__ == '__main__':
    dp: Dispatcher = Dispatcher()

    # Commands
    dp.message.register(cmd.send_welcome, Command(commands=['start', 'help']))
    dp.message.register(cmd.send_tech_text, Command(commands=['techText']))
    dp.message.register(cmd.send_tech_file, Command(commands=['techFile']))
    dp.message.register(cmd.send_random_cat, Command(commands=['meow']))

    dp.run_polling(bot)
