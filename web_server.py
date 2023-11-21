from typing import Any
import os
from pathlib import Path
from fastapi import FastAPI, HTTPException
from llama_cpp import Llama
from pydantic import BaseModel, Field

model_file_path = os.getenv('MODEL_FILE_PATH')

llama2_model = Llama(model_path=model_file_path, seed=42)

app = FastAPI()


class TextInput(BaseModel):
    inputs: str = Field(..., example="Translate the following to Spanish: Hello, how are you?")
    parameters: dict[str, Any] = Field(..., example={"max_tokens": 4096, "temperature": 0.0})


SYSTEM_PROMPT = """
You are a helpful assistant.
"""


@app.post("/generate/")
async def generate_text(data: TextInput) -> dict[str, str]:
    try:
        params = data.parameters or {}
        response = llama2_model(prompt=data.inputs, **params)
        model_out = response['choices'][0]['text']
        return {"generated_text": model_out}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
