from aiohttp.web import Application
from auth.views import LoginView, RegisterView

from views import HomeView

def setup_routes(app: Application):
    app.router.add_view('/login', LoginView)
    app.router.add_view('/logout', HomeView)
    app.router.add_view('/register', RegisterView)