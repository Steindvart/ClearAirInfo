import json
from typing import Any
from dataclasses import dataclass

from aiogram.types import User, Message

import default_val as df


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


def get_all_info(botInfo: User, msg: Message) -> dict[str, object]:
    return {
        "bot": json.loads(botInfo.json()),
        "user": json.loads(msg.from_user.json()),
        "chat": json.loads(msg.chat.json())
    }


def get_log_str(source: str, usr: User) -> str:
    return f"{source} - User_id: {usr.id}, " \
            f"first_name: {usr.first_name}, " \
            f"language_code: {usr.language_code}"
