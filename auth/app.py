from aiohttp.web import Application

from .routes import setup_routes


def init_func():
    app = Application()
    setup_routes(app)

    return app


app = init_func()
