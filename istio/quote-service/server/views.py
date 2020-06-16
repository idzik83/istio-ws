import os

from aiohttp import web
from aiohttp_requests import requests


QUOTE_SERVER_URL = os.getenv('QUOTE_SERVER_URL', 'https://type.fit/api/quotes')


async def get_random_quote(request):
    response = await requests.get(QUOTE_SERVER_URL)
