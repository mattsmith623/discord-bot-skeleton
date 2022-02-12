from re import match

from discord import Client, Message


def is_bot_message(client: Client, message: Message) -> bool:
    pass


def is_command(message: Message) -> bool:
    pass


def parse_command(message: Message) -> list[str]:
    pass
