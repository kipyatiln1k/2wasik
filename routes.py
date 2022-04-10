from aiohttp.web import Application

from views import HomeView

def setup_routes(app: Application):
    app.router.add_view('/', HomeView)