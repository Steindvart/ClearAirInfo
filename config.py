import json
from dataclasses import dataclass


@dataclass
class BotConfig:
    token: str

    def __init__(self, path: str) -> None:
        with open(path, "r") as file:
            self.token = json.load(file)["token"]


@dataclass
class Config:
    bot: BotConfig
