client = OpenAI(api_key="<OPENAI_API_TOKEN>")

"""
Text summarization:

One really common use case for using OpenAI models is summarizing text. 
This has a ton of applications in business settings, including summarizing 
reports into concise one-pagers or a handful of bullet points, or extracting 
the next steps and timelines for different stakeholders.
"""
# Use an f-string to format the prompt
prompt = f"""Summarize the following text into two concise bullet points:
{finance_text}"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}],
  max_completion_tokens=400
)

print(response.choices[0].message.content)

"""
Non determinism: When the model lacks of context, it is likely to have randomness. 
Meaning it could generate different answers.

Controlling response randomness

One way to control the randomness of a response is controlling the temperature parameter.
By default is 1, but ranges from 0 (highly deterministic) to 2 (very random)
"""

"""
We also can use the model to create brand new text, for example, for marketing
"""
prompt = "Generate a powerful tagline for a new electric vehicle that highlights innovation and sustainability"
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user", "content":prompt}]
)

print(response.choices[0].message.content)

"""
Another application is to generate product descriptions
"""
prompt = """
Write a compelling product description for the UltraFit Smartwatch.
Highligth its key features: 10-day battery life, 24/7 heart rate and sleep tracking,
built-in GPS, water resustance up to 50 meters and lightweight design.

Use a persuasive and engaging tone to appeal to fitness enthusiasts and busy profesionals
"""
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user", "content":prompt}]
)

print(response.choices[0].message.content)

"""
Shot prompting: Providing examples to the LLM helps to give context of what we expect as a desirable output,
in other words including examples to guide AI responses

We have 3 types:
    - Zero-shot: no exmaples, just instructions
    - One-shot: one example guides the response
    - Few-shot: multiple examples provide more context

Some cases where shot prompting shines:
    - Text classification
    - Sentiment analysis
    - Data extraction
    - many more
"""
# Zero-shot prompting
zero_shot_prompt = """Classify sentiment as 1-5 (bad-good) in the following statements:
1. Meal was decent, but I've had better ->
2. My food was delayed, but drinks were good ->
"""

# One-shot prompt
one_shot_prompt = """Classify sentiment as 1-5 (bad-good) in the following statements:
1. The service was very slow -> 1
2. Meal was decent, but I've had better ->
3. My food was delayed, but drinks were good ->
"""

# Few-shot promt
few-shot-prompt="""Classify sentiment as 1-5 (bad-good) in the following statements:
1. The service was very slow -> 1
2. The steak was awfully good! -> 5
3. It was ok, no massive complaints -> 3
4. Meal was decent, but I've had better ->
5. My food was delayed, but drinks were good -> 
"""