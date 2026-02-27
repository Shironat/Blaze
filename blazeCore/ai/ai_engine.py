from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_ai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um assistente doméstico estilo Jarvis."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content