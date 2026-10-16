from openai import OpenAI

client = OpenAI(api_key="api_key")
"""
The need for prompt engineering for chatbots
    - Difficult to predict user questions
    - Challenge to guarantee effective responses
    - Prompt engineering guides chatbot behavior

    Chatbot prompt engineering with OpenAI API
        - Each message has designated role
        - Focus has been on user prompts
        - System prompts guide chatbot's behavior
"""
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"system",
               "content":"You are an expert data scientist that explains complex concepts in simple terms."},
               {"role":"user",
                "content":"What is prompt engineering?"}]
)

print(response.choices[0].message.content)

"""
Changing get_response() for chatbot
"""
# Sending one prompt
def get_response(prompt):
    messages = [
        {"role":"user", "content":prompt}
    ]
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content

prompt = "<PROMPT>"
print(get_response(prompt))

# Sending two prompts
def get_response(system_prompt, user_prompt):
    messages = [
            {"role":"system", "content":system_prompt},
            {"role":"user", "content":user_prompt}
        ]
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content
system_prompt = "<SYSTEM_PROMPT>"
user_prompt = "<USER_PROMPT>"
print(get_response(system_prompt,user_prompt))

"""
System message: define purpose

    - Allow chatbot to offer domain-accurate assistance
    - Not defining purpose might lead to contextually irrelevant answers
"""
system_prompt = "Your are a chatbot that answers financial questions."
user_prompt = "Who are you?"

print(get_response(system_prompt,user_prompt))

"""
System message: response guidelines

    - Specify audience, tone, length, structure
    - Conditional prompts to respond to questions
"""
system_prompt = """Your are a chatbot that answers financial questions.
your answers should be precise, formal and objective."""
user_prompt = "What do you think about cryptocurrencies?"

print(get_response(system_prompt,user_prompt))

system_prompt_conditional = """Your are a chatbot that answers financial questions.
your answers should be precise, formal and objective.
If the question you receive is within the financial field, answer it to the best of your knowledge.
Otherwise, answer with 'Sorry, I only know about finance'
"""

"""
Role-playing prompts
    - Tell chatbot to play a specific role
    - Chatbot -> actor in a play
    - Chatbot adjusts to match role
    - Tailored language and content to fit the persona
    - More effective interactions

    More effective role-playing
        - Specify requirements within the role
        - Incorporate traits like personality and expertise

    We can still specify response guidelines and behavior guidance in role-playing prompts
"""
system_prompt = "Act as an expert financial analyst"
user_prompt = "Offer insights into retirement planning for individuals approaching retirement age."

improved_system_prompt = "Act as a seasoned technology journalist covering the latest trends in the tech industry. You're known for your thorough research and insightful analysis."

improved_sp_guidelines = "Act as a seasoned technology journalist covering the latest trends in the tech industry. You're known for your thorough research and insightful analysis. If the question is related to tech, you answer to the be best of your knowledge. Otherwise, you respond with 'I am trained to only discuss techonology topics'"

"""
Incorporating external context
    - Pre-trained language models recognize information they are trained on
    - Need to provide more context
    - More accuracy and effectiveness

    Lack of information in LLMs
        - Knowledge cut-off: "I apologize for the inconvenience but my last knowledge update is Sept 2021"
        - Requested non-public information: "I don't have personal information about you"

How to provide extra information?
    - Sample previous conversations
        - Disadvantage: might need a lot of samples
    - System's prompt
        - Includes required context for chatbot answers

IMPORTANT: These methods work well for small contexts, larger contexts require more sophisticated techniques
"""
sample_conversations = [
    {"role": "system",
     "content": "You are a customer service chatbot that responds to user queries in a gentle way"},
    {"role": "user",
     "content": "What services do you offer?"},
    {"role": "assistant",
     "content": "We provide services for web application development, mobile app development, and custom software solutions"},
    {"role": "user",
     "content": "How many services do you have?"},
]
systems_prompt = f"""You are a customer service chatbot that responds to user queries in a gentle way. Some information about our services are delimited by triple backticks (```)
```{more_info}```
"""
