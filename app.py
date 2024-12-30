from transformers import pipeline
import gradio as gr

model = pipeline("summarization")

def predict(prompt):
    summary = model(prompt)[1]["summary_text"]
    return summary

with gr.Blocks() as demo:
    textbox = gr.Textbox(placeholder = "enter text block to summarize", lines=1)
    gr.Interface(fn=predict, inputs=textbox, outputs="text")

demo.launch()    