import json
from aiogram import Bot, types


async def get_all_info(bot: Bot, msg: types.Message) -> dict[str, object]:
    botInfo: types.User = await bot.get_me()
    return {
        "bot": json.loads(botInfo.as_json()),
        "user": json.loads(msg.from_user.as_json()),
        "chat": json.loads(msg.chat.as_json())
    }