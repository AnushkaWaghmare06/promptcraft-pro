import openai

OPENAI_API_KEY = "YOUR_OPENAI_KEY"
openai.api_key = OPENAI_API_KEY

def generate_app_code(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content
