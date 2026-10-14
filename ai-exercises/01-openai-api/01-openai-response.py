from openai import OpenAI

"""
Template for a request to the OpenAI API

There are different services with different endpoints. Each service is an entry.
Some endpoints may require authentication (most popular: unique key)
"""
client = OpenAI(api_key="ENTER_OPEN_AI_KEY")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_completion_tokens=100,

    # Enter the prompt
    messages=[{"role": "user", "content":"What is OpenAI?"}]
)

print(response.choices[0].message.content)

"""
Text Editing Example
"""
prompt = """
    Update the name to Alan, pronouns to he/him, and job title to Senior Marketing Manager in the
    following text:

    Sarah is a Content Media Manager. Her favorite movie is Titanic and she enjoys to fast track.
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user", "content":prompt}]
)

print(response.choices[0].message.content)

"""
max_completion_tokens importance: Controlls response length
"""
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user",
               "content": "Write a haiku about AI"}],
    max_completion_tokens=5
)
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user",
               "content": "Write a haiku about AI"}],
    max_completion_tokens=30
)

# Tokens: is the unit of text that help the AI understand and interpret text

"""
Cost

The cost depends on the model and the number of tokens
    - Models are priced by cost/tokens
    - Input and output tokens may have different costs

Increasing the max_completion_tokens likely increase cost
"""
# Calculating the cost

# Define price per token (meassured cost by million tokens)
input_token_price = 0.15 / 1000000
output_token_price = 0.6 / 1000000
# Extract the token usage
input_tokens = response.usage.prompt_tokens
output_tokens = max_completion_tokens
# Calculate the cost
cost = (input_token_price * input_tokens + output_token_price * output_tokens)
print(f"Estimated cost: ${cost}")