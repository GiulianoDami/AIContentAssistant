import os
from dotenv import load_dotenv

class APIKeyManager:
    def __init__(self, env_file_path='.env'):
        self.env_file_path = env_file_path
        load_dotenv(self.env_file_path)

    def get_openai_api_key(self):
        return os.getenv('OPENAI_API_KEY')

    def set_openai_api_key(self, api_key):
        with open(self.env_file_path, 'a') as env_file:
            env_file.write(f'OPENAI_API_KEY={api_key}\n')
        load_dotenv(self.env_file_path)