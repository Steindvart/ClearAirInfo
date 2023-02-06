import logging
import json
import requests
from aiogram import Bot, Dispatcher, executor, types, utils

import config

# Constans
TMP_PATH = "tmp/"

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s - %(message)s')

# Global obj
botConfig: config.BotConfig = config.BotConfig("bot-config.json")
bot: Bot = Bot(botConfig.token, parse_mode=types.ParseMode.HTML)
dp: Dispatcher = Dispatcher(bot)


# Commands
@dp.message_handler(commands=['start', 'help', 'welcome'])
async def cmd_send_welcome(message: types.Message) -> None:

    usr: types.User = message.from_user
    logging.info(f"cmd_send_welcome -- User_id: {usr.id}, first_name: {usr.first_name}, locale: {usr.locale}")

    await message.answer(text=botConfig.resources["welcome"])

    allCommands = "Список доступных команд:\n"
    for i in botConfig.resources["commands"].values():
        allCommands += i + "\n"

    await message.answer(text=allCommands)


@dp.message_handler(commands=['techText', 'getTechText'])
async def cmd_send_tech_text(message: types.Message) -> None:

    usr: types.User = message.from_user
    logging.info(f"cmd_send_tech_text -- User_id: {usr.id}, first_name: {usr.first_name}, locale: {usr.locale}")

    replyText = utils.markdown.hcode(
        json.dumps(await config.get_all_info(bot, message), indent=4)
    )

    await message.reply(replyText)


@dp.message_handler(commands=['techFile', 'getTechFile'])
async def cmd_send_tech_file(message: types.Message) -> None:

    usr: types.User = message.from_user
    logging.info(f"cmd_send_tech_file -- User_id: {usr.id}, first_name: {usr.first_name}, locale: {usr.locale}")

    filename = TMP_PATH + f"{message.from_id}.json"
    with open(filename, "w") as file:
        json.dump(
            await utils.get_all_info(bot, message),
            file, indent=4
        )

    with open(filename, "rb") as file:
        await message.reply_document(document=types.InputFile(file))


@dp.message_handler(commands=['getCat', 'meow'])
async def cmd_send_random_cat(message: types.Message) -> None:

    usr: types.User = message.from_user
    logging.info(f"cmd_send_random_cat -- User_id: {usr.id}, first_name: {usr.first_name}, locale: {usr.locale}")

    response = requests.get("https://aws.random.cat/meow")
    catLink = response.json()["file"]

    await message.answer_photo(catLink)


# Main
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
