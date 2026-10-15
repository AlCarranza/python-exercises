client = OpenAI(api_key="<OPENAI_API_TOKEN>")

"""
Roles

    - System: Controls assistant's behavior
    - User: Instruct the assistant
    - Assistant: Response to the user instruction
        - The assistant can also be written by the developer
            to provide examples

    We can avoid misuse (using a chabot for soemthing different than what we designed it),
    by:

    - Adding system message: Can include guardrails
        - Restrictions on model outputs
"""
sys_msg = """
You are finance education assistant that helps students study for their exams.

If you are asked for specific, real-world financial advice with risk to their finances, respond with:

I'm sorry, I am not allowed to provide financial advice.
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages = [{"role":"system",
             "content":"You are a Python programming tutor who speaks concisely"},
             {"role":"user",
              "content":"What is the difference between mutable and immutable objects?"}]
)

print(response.choices[0].message.content)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages = [{"role":"system",
             "content":sys_msg},
             {"role":"user",
              "content":"Which stocks should I invest in?"}]
)

print(response.choices[0].message.content)

"""
Assistant role

Specially used to provide examples
    - Steer model in the right direction
    - Providing the assistant messages is a more structured form of shot-prompting
    - Example: Python Programming Tutor
        - Example user questions and answers
"""
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages = [{"role":"system",
                 "content":"You are a Python programming tutor who speaks concisely"},
                 {"role":"user",
                  "content":"How do you define a Python List?"},
                 {"role":"assistant",
                  "content":"Lists are defined by enclosing a comma-separated sequence of objects inside square brackets [ ]."},
                 {"role":"user",
                  "content":"What is the difference between mutable and immutable objects?"}]
)

"""
Summary System vs. assistant vs. user

System -> Important template formatting
    Output the information in this format:
        name | age | occupation

Assistant -> example conversations
User -> Context required for the new input (often single-turn)
    Example:
    Create a job advert for an AI Engineer. Use this job advert as a template:

    Job Title: Data Engineer
"""

"""
Building a conversation

We can store the historical of the system and user messages and in this way build a conversation

"""
messages = [{"role":"system",
             "content":"You are a data science trutor who provides short, simple explanations"}]


user_qs = ["Why is Python so popular?", "Summarize this in one sentence."]

for q in user_qs:
    print("User: ", q)
    user_dic = {"role":"user", "content":q}
    messages.append(user_dic)

    response = client.chat.completion.create(
        model="gpt-4o-mini",
        messages=messages
    )

    assistant_dict = {"role":"assistant", "content":response.choices[0].message.content}
    messages.append(assistant_dict)
    print("Assistant: ", response.choices[0].message.content, "\n")