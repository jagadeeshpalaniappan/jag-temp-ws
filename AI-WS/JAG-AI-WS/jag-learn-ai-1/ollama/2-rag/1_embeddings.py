import ollama

model_name = "llama3"

stream = ollama.chat(
    model=model_name,
    messages=[{"role": "user", "content": "Why is the sky blue?"}],
    stream=True,
)

for chunk in stream:
    print(chunk["message"]["content"], end="", flush=True)


print(
    ollama.embeddings(
        model=model_name, prompt="They sky is blue because of rayleigh scattering"
    )
)
