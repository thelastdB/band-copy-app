import os
import asyncio
from openai import OpenAI
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Initialize the client — OpenAI SDK will automatically find the env var
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def generate_copy():
    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Write a short, funny Instagram caption for a rock band playing a secret show in Brooklyn."}
        ],
        max_tokens=100,
        temperature=0.8
    )
    print("\n🧠 GPT-3.5 Response:\n")
    print(response.choices[0].message.content)

asyncio.run(generate_copy())
