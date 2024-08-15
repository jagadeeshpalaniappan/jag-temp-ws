# ollama pull llava
import ollama

with open("sample.jpg", "rb") as file:
    response = ollama.chat(
        model="llava",
        messages=[
            {
                "role": "user",
                "content": "What is in this image?",
                "images": [file.read()],
            },
        ],
    )
print(response["message"]["content"])
