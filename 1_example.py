import ollama
import time

MODEL = "llama3.2:1b"

start = time.perf_counter()


# Create a new Ollama client
response = ollama.chat(
    model = MODEL,
    messages = [
        {"role":"system" , "content" : "You are a helpful assistant."},
        {"role":"user" , "content" : "Explain what a vector database is."}
    ],
)

print(response["message"]["content"])
# elapsed = time.perf_counter() - start

# print(response["message"]["content"])
# print(f"Elapsed time: {elapsed:.2f} seconds")