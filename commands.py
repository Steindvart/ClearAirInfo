import logging
import json

import requests
from aiogram import types
from aiogram.utils import markdown

# DEFECT - using global objects, not good
from main import bot, botConfig
import config
import default_val as df

# Alliaces
res = botConfig.resources


async def send_welcome(message: types.Message) -> None:

    logging.info(config.get_log_str("send_welcome", message.from_user))

    await message.answer(res["welcome"])

    allCommands = "\n".join(res["mainCommands"].values())
    allCommands += "\n\n" + "\n".join(res["funCommands"].values())

    await message.answer(allCommands)


async def send_tech_text(message: types.Message) -> None:

    logging.info(config.get_log_str("send_tech_text", message.from_user))

    botInfo: types.User = await bot.get_me()
    replyText = markdown.hcode(
        json.dumps(
            config.get_all_info(botInfo, message),
            indent=df.INDENT
        )
    )

    await message.reply(replyText)


async def send_tech_file(message: types.Message) -> None:

    logging.info(config.get_log_str("send_tech_file", message.from_user))

    filename = df.TMP_PATH + f"{message.from_id}.json"
    with open(filename, "w") as file:
        json.dump(
            config.get_all_info(bot, message),
            file, indent=df.INDENT
        )

    with open(filename, "rb") as file:
        await message.reply_document(document=types.InputFile(file))


async def send_random_cat(message: types.Message) -> None:

    logging.info(config.get_log_str("send_random_cat", message.from_user))

    response = requests.get("https://aws.random.cat/meow")
    catLink = response.json()["file"]

    await message.answer_photo(catLink)
