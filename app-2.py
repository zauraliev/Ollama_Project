from typing import Dict
import ollama

# res = ollama.chat(
#   model="llama3.2",
#   messages=[{"role": "user", "content": "Tell me a fun fact about Baku"}]
# )

# res = ollama.chat(
#   model="llama3.2",
#   messages=[{"role": "user", "content": "Why is the ocean so salty?"}],
#   stream=True
# )

# for chunk in res:
#   print(chunk["message"]["content"], end="", flush=True)

ollama.create(
    model='wiseolio',
    from_='llama3.2',
    system="You are Wise Olio, very smart assistant which answers questions intuitively",
    parameters={
        'temperature': 0.1
    }
)
res = ollama.generate(
  model="wiseolio",
  prompt="Why is the ocean so salty?",
)
print(res['response'])
