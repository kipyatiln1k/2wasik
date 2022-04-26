from aiohttp.web import View, json_response
from supabase import create_client, Client
import os
import jwt

class ShowTeams(View):
    async def get(self):
        params = await self.request.json()
        token = params["token"]
        decode = jwt.decode(token, os.environ.get("SUPABASE_SECRET"), algorithms="HS256", options={"verify_signature": False})
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")
        supabase: Client = create_client(url, key)
        data = supabase.table("teams").select("*").eq("user_id", decode["sub"]).execute() 
        return data

class InsertTeams(View):
    async def post(self):
        params = await self.request.json()
        token = params["token"]
        decode = jwt.decode(token, os.environ.get("SUPABASE_SECRET"), algorithms="HS256", options={"verify_signature": False})
        server_name = params["server_name"]
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")
        supabase: Client = create_client(url, key)
        supabase.table("teams").insert({"server_name": server_name, "user_id": decode["sub"]}).execute()