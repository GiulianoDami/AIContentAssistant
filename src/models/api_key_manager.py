import os
from dotenv import load_dotenv

class APIKeyManager:
    def __init__(self, env_path='.env'):
        self.env_path = env_path
        load_dotenv(self.env_path)

    def get_openai_api_key(self):
        return os.getenv('OPENAI_API_KEY')

    def set_openai_api_key(self, api_key):
        with open(self.env_path, 'a') as env_file:
            env_file.write(f'OPENAI_API_KEY={api_key}\n')
        load_dotenv(self.env_path)  # Reload to ensure the new key is available

    def delete_openai_api_key(self):
        if os.path.exists(self.env_path):
            with open(self.env_path, 'r') as env_file:
                lines = env_file.readlines()
            with open(self.env_path, 'w') as env_file:
                for line in lines:
                    if not line.startswith('OPENAI_API_KEY='):
                        env_file.write(line)
        load_dotenv(self.env_path)  # Reload to ensure the key is removed