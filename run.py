import gradio as gr
from fastapi import FastAPI

from gradio_ui import demo

app = FastAPI()

@app.get('/gradio')
async def home():
    return 'Gradio UI is running at the route /gradio.', 200

app = gr.mount_gradio_app(app, demo, path='/gradio')
