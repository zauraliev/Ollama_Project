import requests
import json

url = "http://localhost:11434/api/generate"

headers = {
  "Content-Type": "application/json"
}

data = {
  "model": "llama3.2",
  "prompt": "Why is the sky blue?",
  "stream": false
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
  print("Generated text:", end="", flush=True)
  # Iterate over the lines of the response
  for line in response.iter_lines():
    if line:
      # Decode the line from bytes to string
      decoded_line = line.decode('utf-8')
      result = json.loads(decoded_line)
      # Extract the generated text
      generated_text = result.get("response", "")
      print(generated_text, end="", flush=True)
else:
  print("Request failed with status code:", response.status_code, response.text)

print(response.json())