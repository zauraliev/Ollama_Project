import ollama

# res = ollama.chat(
#   model="llama3.2",
#   messages=[{"role": "user", "content": "Tell me a fun fact about Baku"}]
# )

res = ollama.chat(
  model="llama3.2",
  messages=[{"role": "user", "content": "Why is the ocean so salty?"}],
  stream=True
)

for chunk in res:
  print(chunk["message"]["content"], end="", flush=True)