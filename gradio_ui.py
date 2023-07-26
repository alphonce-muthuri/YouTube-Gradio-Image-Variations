import os
import uuid
import tempfile
from urllib import request

import gradio as gr
from PIL import Image
import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_variations(image: Image) -> list[str]:
    image_id = uuid.uuid1()
    image_path = f'{tempfile.gettempdir()}/{image_id}.png'
    image.save(image_path)
    response = openai.Image.create_variation(
        image=open(image_path, 'rb'),
        n=2,
        size='1024x1024'
    )
    image_variations = []
    for data in response['data']:
        image_id = uuid.uuid1()
        image_path = f'{tempfile.gettempdir()}/{image_id}.png'
        request.urlretrieve(data['url'], image_path)
        image_variations.append(image_path)
    return image_variations


demo = gr.Interface(
    fn=generate_variations,
    inputs=gr.components.Image(label='Input', type='pil'),
    outputs=gr.components.Gallery(label='Variations'),
    allow_flagging='never'
)
