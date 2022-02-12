from os import environ

from discogs_client import Client as DiscogsClient
from discord import Embed, Message
from dotenv import load_dotenv


load_dotenv()
discogs_client = DiscogsClient('ExampleApplication/0.1', user_token=environ.get('DISCOGS_TOKEN'))


async def run_command(command_name: str, command_arguments: str, message: Message):
    pass


async def run_echo_command(command_arguments: str, message: Message):
    pass


async def run_search_command(command_arguments, message):
    pass
