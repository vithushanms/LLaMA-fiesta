import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from flask import Flask, request

app = Flask(__name__)

@app.route("/generate_text", methods=["POST"])
def generate_text():
    prompt = request.json["prompt"]
    
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("./models/ggml-vicuna-13b-4bit.bin")
    
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    generated_ids = model.generate(input_ids, max_length=100, num_return_sequences=1)
    generated_text = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    
    return {"response": generated_text}

if __name__ == "__main__":
    app.run()


# import torch
# from transformers import GPT2LMHeadModel
# from flask import Flask, request

# app = Flask(__name__)

# @app.route("/generate_text", methods=["POST"])
# def generate_text():
#     prompt = request.json["prompt"]
#     model = GPT2LMHeadModel.from_pretrained("models/ggml-vicuna-13b-4bit.bin")
#     generated_text = model.generate(prompt, max_length=100, num_return_sequences=1)
#     return {"response": generated_text}

# if __name__ == "__main__":
#     app.run()
