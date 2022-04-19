from aiohttp.web import View, json_response

from database import client


class RegisterView(View):
    async def post(self):
        params = await self.request.json()
        email = params["email"]
        password = params["password"]
        
        client.auth.sign_up(email=email, password=password)
        user = await client.auth.sign_in(email=email, password=password)
        return json_response({"access_token": user.access_token})


class LoginView(View):
    async def post(self):
        params = await self.request.json()
        email = params["email"]
        password = params["password"]
        
        user = client.auth.sign_in(email=email, password=password)
        return json_response({"access_token": user.access_token})