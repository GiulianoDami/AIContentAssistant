import os

class Settings:
    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.backend_host = os.getenv('BACKEND_HOST', 'localhost')
        self.backend_port = int(os.getenv('BACKEND_PORT', 5000))
        self.frontend_host = os.getenv('FRONTEND_HOST', 'localhost')
        self.frontend_port = int(os.getenv('FRONTEND_PORT', 3000))

    def validate(self):
        if not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")