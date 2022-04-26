from aiohttp.web import Application
from auth.views import LoginView, RegisterView
from api.teams.teams import InsertTeams, ShowTeams

from views import HomeView

def setup_routes(app: Application):
    app.router.add_view('/', HomeView)
    app.router.add_view('/api/teams', InsertTeams)
    app.router.add_view('/api/teams/show', ShowTeams)