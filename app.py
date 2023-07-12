import subprocess
import sys
from urllib.parse import urlencode
import requests
from dotenv import dotenv_values

def main():
    config = dotenv_values(".env")

    LLAMA_MAIN = config.get("LLAMA_MAIN")
    LLAMA_MODEL_PATH = config.get("LLAMA_MODEL_PATH")
    LLAMA_NUM_THREADS = config.get("LLAMA_NUM_THREADS")
    MAX_OUTPUT_LENGTH = int(config.get("MAX_OUTPUT_LENGTH", 256))

    def handle_request(request):
        model_input = request.args.get("text", b"").decode()
        cmd = [
            LLAMA_MAIN,
            "-m", LLAMA_MODEL_PATH,
            "-t", LLAMA_NUM_THREADS,
            "-n", str(MAX_OUTPUT_LENGTH),
            "-p", model_input
        ]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        return process.stdout

    def generate_response(stream):
        try:
            for line in stream:
                try:
                    sys.stdout.buffer.write(line)
                    sys.stdout.buffer.flush()
                except KeyboardInterrupt:
                    break
        except:
            pass

    query = input("\nPlease type the inputs for the model, then press Enter:\n\n")
    params = urlencode({"text": query})
