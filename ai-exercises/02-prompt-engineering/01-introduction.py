from openai import OpenAI

client = OpenAI(api_key="api_key")
"""
What is prompt engineering?

Crafting prompts or instructions given to LLMs to get desired responses

Recap:

Message Roles
- System message: guides model behavior
- User message: prompt from the user
- Assistant message: response to user promt

Control parameters
- temperature: very from 0 to 2 and controls answer's randomness
- max_tokens: controls response length 
"""
prompt = "What is prompt engineering?"
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{
        "role":"user",
        "content":prompt
    }],
    temperature=0
)

print(response.choices[0].message.content)

"""
Creating get_response() function
"""
def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role":"user",
            "content":prompt
        }],
        temperature=0
    )
    return response.choices[0].message.content

"""
Prompt improvement: Techniques to improve the prompts
"""
prompt = "What is prompt engineering? Explain it in terms that can be understood by a 5-year-old"
response = get_response(prompt)
print(response)

"""
Key principles of prompt engineering

- Create clear and precise prompts
- Appropriate action verbs
- Detailed and precise instructions
- Well-structured delimited prompts

Using action verbs:
    - Guide the model what to do, use verbs like:
        * write
        * complete
        * explain
        * describe
        * evaluate
    - Avoid using ambiguous verbs that confuse the model understanding, like:
        * understand
        * think
        * feel
        * try
        * know

Formulating detailed instructions: Provide specific, descriptive and detailed instructions regarding:
    - Context
    - Output length
    - Format and style
    - Audience

Limiting output length
    - max_tokens:
        * Limit on number of tokens
        * Output cannot bypass it
        * Might lead to incomplete or cut responses
    - prompt:
        * Limit on words, sentences or paragraphs
        * Output may bypass it
        * Complete response

Prompt components
    - Instructions and input data to operate on
    - Example: text summarization
        * Instruction: summarize the given text
        * Input data: text to summarize

Crafting a well-structured prompt with delimiters
    - Start prompt with instructions
    - Use delimiters (parentheses, brackets, backticks, etc.) to specify input parts
    - Mention which delimiters are used

Using formatted strings (f-strings)
    Include defined string into another string
"""
bad_prompt = "Think about the issue of deforestation"
response = get_response(bad_prompt)
print(response)

good_prompt = "Propose strategies to reduce deforestation"
response = get_response(good_prompt)
print(response)

ineffective_prompt = "Tell me about dogs"
effective_prompt = "Write a descriptive paragraph about the behavior and characteristics of Golden Retrievers, highlight their friendly nature, intelligence and suitability as a family pets"
print(get_response(effective_prompt))

prompt="""Summarize the text delimited by triple backticks into bullet points.
    ```TEXT GOES HERE```"""
response=get_response(prompt)

text = "This is a sample text to summarize"
prompt = f"""Summarize the text delimited by triple backticks into buller points.
            ```{text}```"""
print(prompt)

"""
Structured outputs
    - LLMs generate structured outputs only when given explicit instructions
    - Output structures:
        * Table
        * List
        * Structured paragraph
        * Custom format

Tables: Clearly mention expected columns
Lists: Helpful for enumerations, we should mention requirements for numbering, otherwise wont be enumerated
Structured paragraphs: Mention structure requirements in prompt
Custom format:
"""
table_prompt = "Generate a table containing 5 movies I should watch if I am an action lover, with columns for Title and Rating"
list_prompt = "Generate a list containing the names of the top 5 cities to visit."
paragraph_prompt = "Provide a structured paragraph with clear headings and subheadings about the benefits of regular exercise on overall health and well-being."

print(get_response(table_prompt))
# Custom format
text = "Once upon a time in a quaint little village, there lived a curious young boy named David. David was [...]"
instructions = "You will be provided with a text delimited by triple backticks. Generate a suitable title for it."

output_format = """
    Use the following format for the output:
        - Text: <text we want to title>
        - Title: <the generated title>
"""

custom_prompt = instructions + output_format + f"```{text}```"
print(get_response(custom_prompt))

"""
Conditional prompts
    - Incorporate logic or conditions
    - Conditional prompts follow an if-else style
    - Can incorporate multiple conditions
"""
text = "Le printemps est ma saison préférée. Quand les premières fleurs commencent à éclore, et que les arbres se parent de feuilles vertes et tendres, je me sens revivre [...]"
prompt = f""""You will be provided with a text delimited by triple backticks.
            If the text is written in English, suggest a suitable title for it.
            Otherwise, write 'I only understand English'.
            ```{text}```"""

print(get_response(prompt))

text_multiple = "In the heart of the forest, sunlight filters through the lush green canopy, creating a tranquil atmosphere [...]"
prompt_multiple = f"""You will be provided with a text delimited by triple backticks.
            If the text is written in English, check if it contains the keyword 'technology'.
            If it does, suggest a suitable title for it, otherwise, write 'Keyword not found'.
            If the text is not written in English, reply with 'I only understand English'.
            ```{text_multiple}```"""
print(get_response(prompt_multiple))
            