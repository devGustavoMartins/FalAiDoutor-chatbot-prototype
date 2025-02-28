import ollama
from config import Config

system_prompt = Config.SYSTEM_PROMPT

def chat(user_prompt, model):
    stream = ollama.chat(
        model=model,
        messages=[{'role': 'assistant', 'content': system_prompt},
                  {'role': 'user', 'content': f"Modelo em uso é {model}.{user_prompt}"}],
        stream=True,
    )

    return stream

# handles stream response back from LLM
def stream_parser(stream):
    for chunk in stream:
        yield chunk['message']['content']