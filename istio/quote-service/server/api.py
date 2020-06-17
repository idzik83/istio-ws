from aiohttp import web

from .routes import routes


async def web_app():
    app = web.Application()
    app.add_routes(routes)
    return app
