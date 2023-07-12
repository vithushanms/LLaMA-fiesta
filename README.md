# LLaMA-fiesta
A client application that helps to run open source LLaMA LLMs locally

# 01. Python Streaming API

This is a Python streaming API that interacts with a [llama.cpp](https://github.com/vithushanms/llama.cpp) program to process text prompts. It provides a server implementation in Python and a client script for streaming the response.

please build the lamma.cpp project before running this app 

## Requirements

- please build the [llama.cpp](https://github.com/vithushanms/llama.cpp) project before running this app 
- Python 3.x
- Other dependencies specified in `requirements.txt`

## Installation

1. Clone the repository:
`git clone <repository-url> cd python-streaming-ap`

2. Install the required dependencies: `pip install -r requirements.txt`

3. Create a `.env` file in the root directory of the project and add the following environment variables (replace with your actual values):
</br>
LLAMA_MAIN=/path/to/llama.cpp/main</br>
LLAMA_MODEL_PATH=/path/to/7B/ggml-model-f16.bin</br>
LLAMA_NUM_THREADS=16</br>
MAX_OUTPUT_LENGTH=256</br>

## Usage

1. Run the python file: `python app.py`

2. Enjoy the streaming API

## License

This project is licensed under the [MIT License](LICENSE).

