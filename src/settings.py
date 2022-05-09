import os
import dotenv

SRC_DIR = os.path.dirname(__file__)

dotenv.load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

APP_HOST = os.environ.get("APP_HOST")