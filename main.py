import logging

from aiogram import Bot, Dispatcher, executor, types

import config
import commands as cmd


# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s - %(message)s')

# Global obj
botConfig: config.BotConfig = config.BotConfig("bot-config.json")
bot: Bot = Bot(botConfig.token, parse_mode=types.ParseMode.HTML)
dp: Dispatcher = Dispatcher(bot)


# Main
if __name__ == '__main__':
    # Commands
    dp.register_message_handler(cmd.send_welcome, commands=['start', 'help'])
    dp.register_message_handler(cmd.send_tech_text, commands=['techText'])
    dp.register_message_handler(cmd.send_tech_file, commands=['techFile'])
    dp.register_message_handler(cmd.send_random_cat, commands=['meow'])

    executor.start_polling(dp, skip_updates=True)
