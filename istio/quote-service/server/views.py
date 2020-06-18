import typing
import os
import random

from aiohttp import web
from aiohttp_requests import requests


QUOTE_SERVER_URL = os.getenv('QUOTE_SERVER_URL', 'https://type.fit/api/quotes')
SEARCH_IMAGE_SERVER_URL = os.getenv('SEARCH_SERVER_URL', 'https://api.qwant.com/api/search/images')


async def get_authors_image(author: str) -> typing.Union[str, None]:
    def get_first_image_url(resp: dict) -> typing.Union[str, None]:
        if not resp.get('status') == 'success':
            return None
        items = resp.get('data', {}).get('result', {}).get('items', [])
        for item in items:
            media = item.get('media')
            if media:
                return media
        return None

    if not author:
        return None
    params = {'count': 5, 't': 'images', 'safesearch': 1, 'locale': 'en_GB', 'uiv': 4, 'q': author}
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
    response = await requests.get(SEARCH_IMAGE_SERVER_URL, params=params, headers=headers)
    response.raise_for_status()
    return get_first_image_url(await response.json())


async def get_random_quote(request):
    response = await requests.get(QUOTE_SERVER_URL)
    response.raise_for_status()
    quotes = await response.json(content_type='text/plain')
    rand_quote_idx = random.randrange(len(quotes))
    quote = quotes[rand_quote_idx]
    image = await get_authors_image(quote['author'])
    return web.json_response({'quote': quote['text'], 'author': quote['author'], 'image': image})
