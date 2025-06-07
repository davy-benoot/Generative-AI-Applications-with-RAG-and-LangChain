# Import the necessary packages
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai import Credentials
from langchain_ibm import WatsonxLLM
import gradio as gr
import os
import json

# Define constants for api key retrieval
api_key_file = 'apikey.json'
api_key = None
url = "https://eu-de.ml.cloud.ibm.com",
project_id = "9c860b6d-90e6-4160-be4d-115366e6eb5f"

# Check if the api file exists before trying to open it
if os.path.exists(api_key_file):
    try:
        with open(api_key_file, 'r') as f:
            api_keys_data = json.load(f)
            apikey = api_keys_data.get("apikey") # Get the API key from the JSON
    except json.JSONDecodeError:
        print(f"Error: '{api_key_file}' is not a valid JSON file.")
    except Exception as e:
        print(f"An error occurred while reading '{api_key_file}': {e}")
else:
    print(f"Warning: '{api_key_file}' not found. Please ensure your API key file is in the correct location.")

if not apikey:
    print("Error: API key not found in 'apikey.json' or file is missing/corrupted. Please check your setup.")
    # You might want to raise an exception or handle this case more robustly

# Specify the model and project settings 
# Model and project settings
model_id = 'mistralai/mixtral-8x7b-instruct-v01' # Specify the Mixtral 8x7B model
#model_id = 'ibm/granite-3-3-8b-instruct' # Specify IBM's Granite 3.3 8B model
# Set necessary parameters
parameters = {
    GenParams.MAX_NEW_TOKENS: 256,  # Specify the max tokens you want to generate
    GenParams.TEMPERATURE: 0.5, # This randomness or creativity of the model's responses
}

# Wrap up the model into WatsonxLLM inference
watsonx_llm = WatsonxLLM(
    model_id=model_id,
        project_id=project_id,
        params=parameters,
        url="https://eu-de.ml.cloud.ibm.com",
        apikey=apikey
)

# Function to generate a response from the model
def generate_response(prompt_txt):
    generated_response = watsonx_llm.invoke(prompt_txt)
    return generated_response
# Create Gradio interface
chat_application = gr.Interface(
    fn=generate_response,
    allow_flagging="never",
    inputs=gr.Textbox(label="Input", lines=2, placeholder="Type your question here..."),
    outputs=gr.Textbox(label="Output"),
    title="Watsonx.ai Chatbot",
    description="Ask any question and the chatbot will try to answer."
)
# Launch the app
chat_application.launch(server_name="127.0.0.1", server_port= 7860)