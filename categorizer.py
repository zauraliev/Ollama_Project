import ollama
import os

model="llama3.2"

input_file="./data/grocery_list.txt"
output_file="./data/categorized_grocery_list.txt"

if not os.path.exists(input_file):
  print("Input file not found:", input_file)
  exit(1)

with open(input_file, "r") as f:
  items = f.read().strip()

# Prepare the prompt for the model
prompt = f"""
You are an assistant that categorizes and sorts grocery items.

Here is a list of grocery items:

{items}

Please:

1. Categorize these items into appropriate categories such as Produce, Dairy, Meat, Bakery, Beverages, etc.
2. Sort the items alphabetically within each category.
3. Present the categorized list in a clear and organized manner, using bullet points or numbering.

"""
try:
  res = ollama.generate(model=model,prompt=prompt)
  generated_text = res.get("response", "")
  print("==== Categorized List: ===== \n")
  print(generated_text)

  with open(output_file, "w") as f:
    f.write(generated_text.strip())
  print(f"Categorized grocery list has been saved to '{output_file}'.")
except Exception as e:
  print("Error:", str(e))
