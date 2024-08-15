import ollama

# model_name = "mistral"
model_name = "llama3"

# Chat function
response = ollama.chat(
    model=model_name, messages=[{"role": "user", "content": "Why is the sky blue?"}]
)
print("Chat response:", response["message"]["content"])
print("------------------------------------------")

# Generate function
generate_response = ollama.generate(model=model_name, prompt="Why is the sky blue?")
print("Generate response:", generate_response["response"])
print("------------------------------------------")


# List function
models_list = ollama.list()
print("List of models:", models_list)
print("------------------------------------------")


# Show function
show_response = ollama.show(model_name)
print("Show model response:", show_response)
print("------------------------------------------")


# Create function
modelfile = """
FROM mistral
SYSTEM You are Mario from Super Mario Bros.
"""
create_response = ollama.create(model="example", modelfile=modelfile)
print("Create model response:", create_response)

print("------------------------------------------")

# Copy function
copy_response = ollama.copy(model_name, "user/mistral")
print("Copy model response:", copy_response)
print("------------------------------------------")


# Delete function
delete_response = ollama.delete("example")
print("Delete model response:", delete_response)
print("------------------------------------------")


# Pull function
pull_response = ollama.pull(model_name)
print("Pull model response:", pull_response)
print("------------------------------------------")

# Push function
push_response = ollama.push("user/mistral")
print("Push model response:", push_response)
print("------------------------------------------")

# Embeddings function
embeddings_response = ollama.embeddings(
    model=model_name, prompt="The sky is blue because of Rayleigh scattering"
)
print("Embeddings response:", embeddings_response)
print("------------------------------------------")
