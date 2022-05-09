from aiohttp.web import Application

from routes import setup_routes
from auth import app as auth_app


def init_func():
    app = Application()
    setup_routes(app)
    
    app.add_subapp('/auth/', auth_app)

    return app


app = init_func()
