from aiohttp.web import run_app

from app import app
from settings import APP_HOST

if __name__ == "__main__":
    run_app(app, host=APP_HOST)
