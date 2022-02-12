from os import environ

from discord import Client as DiscordClient
from dotenv import load_dotenv

from message_parser import is_bot_message, is_command, parse_command
from command_runner import run_command


class DiscordBot(DiscordClient):
    async def on_ready(self):
        pass

    async def on_message(self, message):
        pass


load_dotenv()

discord_client = DiscordBot()
discord_client.run(environ.get('DISCORD_TOKEN'))
