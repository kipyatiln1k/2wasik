from aiohttp.web import View, json_response


class HomeView(View):
    async def get(self):
        return json_response({"ok": True})
