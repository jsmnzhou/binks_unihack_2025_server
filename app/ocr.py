import easyocr
import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()
LLMA_API_KEY = os.getenv('LLMA_API_KEY')
reader = easyocr.Reader(['en']) 
result = reader.readtext('test_data/assessment-plan.png', detail = 0)


client = Groq()
completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": "Explain the importance of low latency LLMs",
            },
        ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
