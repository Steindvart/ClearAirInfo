import asyncio
from aiogram import Bot

from config import BotConfig


async def main() -> None:
    botConfig: BotConfig = BotConfig("bot-config.json")
    bot: Bot = Bot(botConfig.token)

    try:
        aboutBot = await bot.get_me()
        print(f"Hello! I'm {aboutBot.first_name} bot")
    finally:
        await bot.close()


asyncio.run(main())
