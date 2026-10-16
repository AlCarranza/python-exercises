"""
Why build with Hugging Face?
Hugging Face is a powerful platform that provides many benefits for building AI solutions, simplifying workflows and making advanced models accessible.

Interference with Hugging Face
    - Local interference
        * Free
        * Convenient
        * Slow and resource-intensive
    - Interference Providers
        * Fast
        * Free to get started

Introduction to the Transformers Library
    - Simplifies working with pre-trained models
"""
from transformers import pipeline

gpt2_pipeline = pipeline(task="text-generation", model="openai-community/gpt2")

print(gpt2_pipeline("What if AI"))

"""
Adjusting Pipeline Parameters
"""

results = gpt2_pipeline("What if AI", max_new_tokens=10, num_returned_sequences=2)
for result in results:
    print(result['generated_text'])

"""
Using inference providers
"""
import os
from huggingface_hub import InterferenceClient

client = InterferenceClient(
    provider="together",
    api_key=os.environ["HF_TOKEN"],
)

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ],
)

print(completion.choices[0].message)

"""
Installing Datasets package

pip install datasets
    - Access
    - Download
    - Use
    - Share
"""
from datasets import load_dataset

data = load_dataset("IVN-RIN/BioBERT_Italian")

"""
Split parameter
"""

data = load_dataset("IVN-RIN/BioBERT_Italian", split="train")

"""
Data manipulation
"""
data = load_dataset("IVN-RIN/BioBERT_Italian", split="train")

# Filter for pattern " bella "
filtered = data.filter(lambda row: " bella " in row['text'])
print(filtered)

# Select the first two rows
sliced = filtered.select(range(2))
print(sliced)
#Extract the text for the first row
print(sliced[0]['text'])
