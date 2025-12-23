import openai
import os

class NLGModel:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def summarize_text(self, text):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Please summarize the following text:\n\n{text}",
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5
        )
        summary = response.choices[0].text.strip()
        return summary

    def generate_script(self, summary):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Create a video script based on the following summary:\n\n{summary}",
            max_tokens=300,
            n=1,
            stop=None,
            temperature=0.7
        )
        script = response.choices[0].text.strip()
        return script