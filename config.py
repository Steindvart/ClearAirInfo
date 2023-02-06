import json
from typing import Any
from dataclasses import dataclass

from aiogram import Bot, types


@dataclass
class BotConfig:
    # Data
    token: str
    supportedLocales = ("ru")
    resources: dict[str, Any]

    @property
    def locale(self):
        return self._locale

    @locale.setter
    def locale(self, newVal):
        if newVal not in self.supportedLocales:
            raise f"{newVal} locale is not supported."
        self._locale = newVal

    # Methods
    def __init__(self, configPath: str) -> None:

        # NOTE - Default locale is "ru"
        # DEFECT - Get first locale from supported, no hard-code
        self.locale = "ru"

        with open(configPath, "r") as file:
            self.token = json.load(file)["token"]

        with open(f"locales/{self.locale}.json", "r", encoding="utf8") as file:
            self.resources = json.load(file)


async def get_all_info(bot: Bot, msg: types.Message) -> dict[str, object]:
    botInfo: types.User = await bot.get_me()
    return {
        "bot": json.loads(botInfo.as_json()),
        "user": json.loads(msg.from_user.as_json()),
        "chat": json.loads(msg.chat.as_json())
    }
