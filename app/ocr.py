import easyocr
import os
from dotenv import load_dotenv
from groq import Groq
from absl import logging
import io
import constants
load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

class Model:
    def __init__(self, model="llama-3.3-70b-versatile"):
        self.model = model
        self.client = Groq(api_key=GROQ_API_KEY)
        self.reader = easyocr.Reader(['en']) 
        self.text = ""

    def inference_on_image(self, file, detail: int=0):
        if type(file) == bytes:
            image_bytes = io.BytesIO(file)
            image_data: str = self.reader.readtext(image_bytes, detail = detail)
        elif type(file) == str:
            image_data: str = self.reader.readtext(file, detail = detail)
        
        if type(image_data) == list:
            self.text = " ".join(image_data)
        else:
            logging.error(f"Failed to decode image with error: {image_data}")

    def inference_on_transcript(self, type: str):
        match type:
            case 'ASSESSMENT':
                instruction: str = "Based on this transcript of an assessment schedule, create the assessment entries as a json. Only answer with the JSON. Transcript: " + self.text + ".\n"
                system_prompt_intro: str = """
                        You are a helpful assistant. Provide a response given the example answer format below.

                        Prompt: 
                        I have a datatable of the form:
                        """ + constants.ASSESSMENTS_TABLE + ".\n"

                system_prompt: str = system_prompt_intro + " " + instruction + " Example input: " + constants.ASSESSMENTS_TEXT + " Example answer: " + str(constants.ASSESSMENTS_JSON)
            case _:
                system_prompt: str = ""
            
        completion = self.client.chat.completions.create(
        model=self.model,
        messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                }
            ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stop=None,
        )
        message = completion.choices[0].message.content
        return message

        



