import gradio as gr
import openai
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()

# Function to tell a joke about student and teacher
def tell_joke():
    messages = [
        {"role": "system", "content": "You are a funny assistant. Tell jokes related to students and teachers."},
        {"role": "user", "content": "Tell me a funny joke about a son and a after."}
    ]
    
    completion = openai.chat.completions.create(
        model="gpt-4.1-nano",  # Use "gpt-4o" or another available model if needed
        messages=messages,
        temperature=0.9
    )
    
    return completion.choices[0].message.content

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## 🎓 Student-Teacher Joke Generator 😂")
    
    joke_button = gr.Button("Tell me a Joke")
    joke_output = gr.Textbox(label="Here's your Joke:", lines=4)
    
    joke_button.click(fn=tell_joke, inputs=None, outputs=joke_output)

demo.launch()

