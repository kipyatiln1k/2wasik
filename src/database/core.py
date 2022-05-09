from supabase import create_client

from settings import SUPABASE_KEY, SUPABASE_URL


client = create_client(supabase_url=SUPABASE_URL, supabase_key=SUPABASE_KEY)
