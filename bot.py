from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()


@dataclass
class Config:
    bot_token: str


def load_config() -> Config:
    token = os.getenv("BOT_TOKEN", "").strip()
    if not token:
        raise RuntimeError(
            "BOT_TOKEN не задан. Создай файл .env рядом с main.py со строкой "
            "BOT_TOKEN=123456:ABC... (токен из @BotFather) или задай переменную окружения."
        )
    return Config(token)
