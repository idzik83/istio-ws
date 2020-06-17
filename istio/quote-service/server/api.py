from aiohttp import web

from .routes import routes


async def web_app(argv):
    app = web.Application()
    app.add_routes(routes)
    return app
