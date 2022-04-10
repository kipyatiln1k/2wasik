from aiohttp.web import Application, run_app

from routes import setup_routes
from database import client


def init_func():
    app = Application()
    setup_routes(app)
    
    run_app(app, host="localhost")


if __name__ == "__main__":
    init_func()
