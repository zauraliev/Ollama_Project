import ollama

res = ollama.chat(
  model="llama3.2",
  messages=[{"role": "user", "content": "Tell me a fun fact about Baku"}]
)

print(res)