import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    BACKEND_HOST = os.getenv('BACKEND_HOST', '127.0.0.1')
    BACKEND_PORT = int(os.getenv('BACKEND_PORT', 5000))
    FRONTEND_HOST = os.getenv('FRONTEND_HOST', '127.0.0.1')
    FRONTEND_PORT = int(os.getenv('FRONTEND_PORT', 3000))