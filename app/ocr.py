import easyocr
import os
from dotenv import load_dotenv
from groq import Groq
import io
from PIL import Image
load_dotenv()
LLMA_API_KEY = os.getenv('LLMA_API_KEY')

class ModelManager:
    def __init__(self, model="llama-3.3-70b-versatile"):
        self.model = model
        self.client = Groq()
        self.reader = easyocr.Reader(['en']) 

    def inference_on_image(self, file, detail: int=0):
        image_bytes = io.BytesIO(file.read)
        image_data: str = self.reader.readtext(image_bytes, detail = detail)
        return image_data

    def inference_on_transcript(self, type: str, transcript: str):
        match type:
            case 'ASSESSMENT':
                system_prompt_intro: str = ""
                instruction: str = "Based on this transcript of an assessment schedule, create the assessment entries as a json" + transcript
            case _:
                return None
            
        
        completion = self.client.chat.completions.create(
        model=self.model,
        messages=[
                {
                    "role": "system",
                    "content": system_prompt_intro,
                },
                {
                    "role": "user",
                    "content": instruction,
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

        



