import json
from typing import Any
from dataclasses import dataclass


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

        # Default locale is "ru"
        self.locale = "ru"

        with open(configPath, "r") as file:
            self.token = json.load(file)["token"]

        with open(f"locales/{self.locale}.json", "r", encoding="utf8") as file:
            self.resources = json.load(file)


@dataclass
class Config:
    bot: BotConfig
