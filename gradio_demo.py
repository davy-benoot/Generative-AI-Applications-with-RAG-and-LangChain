#!/home/davy/Documents/jupyter/bin/python3
# -*- coding: utf-8 -*-
import re
import sys
import gradio as gr

def concat_str(Str1, Str2):
    return Str1 + Str2

# Define the interface
demo = gr.Interface(
    fn=concat_str, 
inputs=[gr.Textbox(), gr.Textbox()], # Create two text input fields where users can enter numbers
    outputs=gr.Textbox() # Create text output fields
)

# Launch the interface
demo.launch(server_name="127.0.0.1", server_port= 7860)