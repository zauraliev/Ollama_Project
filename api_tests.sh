curl http://localhost:11434/api/generate -d '{
  "model": "olio",
  "prompt": "Why is the sky blue?",
  "stream":false
}'

curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [{"role":"user","content":"Tell me a fun fact about Baku"}],
  "stream":false
}'

curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "What color is the sky at different times of the day? Respond using JSON",
  "format": "json",
  "stream": false
}'