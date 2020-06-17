import os
import random

from aiohttp import web
from aiohttp_requests import requests


QUOTE_SERVER_URL = os.getenv('QUOTE_SERVER_URL', 'https://type.fit/api/quotes')


async def get_random_quote(request):
    response = await requests.get(QUOTE_SERVER_URL)
    quotes = await response.json()
    rand_quote_idx = random.randrange(len(quotes))
    return web.json_response({'quote': quotes[rand_quote_idx]['text']})
