from aiohttp import web

from . import views


routes = (
    web.get('/api/quote/', views.get_random_quote),
)
