from fastapi import FastAPI,Form,Request
from typing import Union
from fastapi.responses import FileResponse,HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing_extensions import Annotated
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import re
import os
import gradio as gr


############################################  Code for Email Subject Generation ############################################ 

model_s = GPT2LMHeadModel.from_pretrained(
    "SilentLearner/model_save_subgen"
)
tokenizer_s = GPT2Tokenizer.from_pretrained(
    "SilentLearner/model_save_subgen"
)
tokenizer_s.padding_side = "left"


def eval_encoding_s(body):
    encode_body = '<|startoftext|>' + '<body>'+ body
    encode_subject = '<subject>'
    return encode_body, encode_subject

def return_first_match_s(string):
    try:
        result = re.search("(?<=<subject>).*",string).group()
        # result = re.search(".*?(?=:)",string).group()
        # result = re.search("(?=<:).*",string).group()
    except Exception or IndexError:
        result = ''
    return result

def subgen(body):
    encodings_dict = tokenizer_s(eval_encoding_s(body)[0],
                           eval_encoding_s(body)[1],
                           truncation=True, max_length=512,
                           padding="max_length",
                           return_tensors = 'pt')
    prediction = model_s.generate(**encodings_dict,
                                max_new_tokens=10,
                                penalty_alpha=0.27,
                                top_k=27,
                                pad_token_id = tokenizer_s.pad_token_id,
    )
    decoded_preds = tokenizer_s.decode(prediction[0], skip_special_tokens=True)
    decoded_preds = return_first_match_s(decoded_preds).strip()
    # decoded_preds = ''.join(letter for letter in decoded_preds if letter.isalnum() or letter.isspace()).strip()
    return decoded_preds


############################################ Code for AIML QA ############################################ 


model = GPT2LMHeadModel.from_pretrained(
    "SilentLearner/model_save_qa"
)
tokenizer = GPT2Tokenizer.from_pretrained(
    "SilentLearner/model_save_qa"
)
tokenizer.padding_side = "left"

def eval_encoding(question):
  encode_body = '<|startoftext|>' + '<question> '+ question
  encode_subject = '<answer>'
  return encode_body, encode_subject

def return_first_match(string):
    try:
        result = re.search("(?<=<answer>).*",string).group()
    except Exception or IndexError:
        result = ''
    return result

def qaaiml(question):
    encodings_dict = tokenizer(eval_encoding(question)[0],
                           eval_encoding(question)[1],
                           truncation=True, max_length=512,
                           padding="max_length",
                           return_tensors = 'pt')

    prediction = model.generate(**encodings_dict,
                                max_new_tokens=60,
                                penalty_alpha=0.10,
                                top_k=5,
                                pad_token_id = tokenizer.pad_token_id,
    )
    decoded_preds = tokenizer.decode(prediction[0], skip_special_tokens=True)
    decoded_preds = return_first_match(decoded_preds).strip().split(".")[0]
    return decoded_preds

############################################ Gradio frontend part ############################################ 

theme = gr.themes.Soft()

with gr.Blocks(theme = theme) as demo:
    gr.Markdown("AIML Project")
    with gr.Row():
        with gr.Column(scale = 2):
            with gr.Tab("Subject Generation",scale = 2):
                text_input = gr.Textbox(
                    label="Email",
                    lines=3,
                )
                text_output = gr.Textbox(label="Subject",)
                sub_button = gr.Button("Generate")
            with gr.Tab("AIML QA"):
                text_input_q = gr.Textbox(label="Question",)
                text_output_q = gr.Textbox(label="Answer",)
                qa_button = gr.Button("Answer")
                
        with gr.Column(scale = 1):
            gr.Textbox(label="Team members",
                       interactive = False,
                       container = True,
                       value = """
Rupesh
Sreeram
Iqbal
                       """
                      )


    sub_button.click(subgen, inputs=text_input, outputs=text_output)
    qa_button.click(qaaiml, inputs=text_input_q, outputs=text_output_q)

    
if __name__ == "__main__":
    demo.launch()
