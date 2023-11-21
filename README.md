# Serve LLMs via REST API with llama.cpp

This is a simple example of how to serve a LLM via REST API using [llama.cpp](https://github.com/ggerganov/llama.cpp)
, [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) and [FastAPI](https://fastapi.tiangolo.com/).

1. Install `make`
E.g. for macOS: `brew install make`
2. Build `llama.cpp`:
```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp; make -j
```
3. Install `git-lfs`:
```bash
brew install git-lfs
git lfs install
```
4. Find an LLM in GGUF format on HF Hub:
https://huggingface.co/models?sort=trending&search=gguf
5. Clone model's repo:
e.g. 
```bash
git clone https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF
```
6. Create virtual environment and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
7. Set `MODEL_PATH` to the path of the cloned model repo
8. Start the server:
```bash 
uvicorn web_server:app  --host 0.0.0.0 --port 8000
```
Check out the docs: http://0.0.0.0:8000/docs
9. Try an example request:
```bash
$ curl -X 'POST' \
  'http://0.0.0.0:8000/generate/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "inputs": "Translate the following to Spanish: Hello, how are you?",
  "parameters": {
    "max_tokens": 4096,
    "temperature": 0
  }
}'
> {"generated_text":"\n\nHola, ¿cómo estás?"}
```