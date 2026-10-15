from pe_01_introduction import get_response

"""
Zero-Shot Prompting
    - Providing a prompt without examples
    - Model generates responses based on it's knowledge
    - Ideal for quick and uncomplicated tasks
"""
zero_shot_prompt = "What is prompt engineering?"
print(get_response(zero_shot_prompt))

"""
One-Shot prompting
    - Provide the model a single example
    - Useful for consistent formatting or style
"""
one_shot_prompt = """
Q: Sum the numbers 3, 5 and 6. A: 3+5+6=14
Q: Sum the numbers 2, 4 and 7. A:
"""
print(get_response(one_shot_prompt))

"""
Few-Shot prompting
    - Provide more than one example
    - Powerful for contextual tasks
"""
few_shot_prompt = """
Text: Today the weather is fantastic -> Classification: positive
Text: The furniture is small -> Classification: neutral
Text: I don't like your attitude -> Classification: negative
Text: That shot selection was awful -> Classification:
"""
print(get_response(few_shot_prompt))

"""
Considerations:
    - Choose number of shots according to task complexity
        - Fewer shots -> basic tasks
        - Diverse shorts -> complex tasks
"""

"""
Multi-step prompting
    - Break down an end goal into series of steps
    - Model goes through each step to give final output
    - Multi-step prompts are used for:
        * Sequential tasks
        * Cognitive tasks
"""
single_step_prompt = "Compose a travel blog"
multi_step_prompt = """Compose a travel blog as follows:
Step 1: Introduce the destination
Step 2: Share personal adventures during the trip
Step 3: Summarize the journey
"""


"""
Analyzing solution correctness

Multi-step vs few-shot prompt

    - Steps: Explicitly tell model what to do
    - Shots: Questions and answers model learns for
"""
calculator = """
def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
"""

single_step_prompt=f"""Determine if the code delimited by
triple backticks is correct ot not.
Answer yes or no.
```{calculator}```
"""

multi_step_prompt=f"""Determine the correctness of the code
delimited by triple backticks as follows:
Step 1: Check the code correctness in each function.
Step 2: Verify if the divide function handles the case when dividing by 0.
Code: ```{calculator}```
"""

"""
Chain of thought and self-consistency prompting
    - Requires LLMs to provide reasoning steps (thoughts) before giving answer
    - Used for coplex reasoning tasks
    - Help reduce model errors
"""
simple_cot_prompt="""Q: You start with 15 books in your collection. At the bookstore, you purchase 8 new books.
Then, you lend 3 to your friend and 2 to your cousin. Later, you visit another bookstore and buy 5 more books.
How many books do you have now?

A: Let's think step by step"""
print(get_response(simple_cot_prompt))

"""
Chain-of-thought prompting with few-shots
"""
example="""
Q: The odd numbers in this group add up to an even number: 9, 10, 13, 4, 2.
A: Adding all the odd numbers (9, 13) gives 22. The answer is True.
"""
question="""
Q: The odd numbers in this group add up an even number: 15, 13, 82, 7.
A:
"""
prompt = example + question
print(get_response(prompt))

"""
Chain-of-thought vs multi-step prompting
    - Multi-step prompts: Incorporate steps inside the prompt
    - Chain-of-thought: Ask model to generate intermediate steps

Chain-of-thought limitations
    - One unsuccessful though -> unsuccessful outcome
    - Self-consistency prompts were introduced

Self-consistency prompting
    - Generates multiple chain-of-thoughts by prompting the model several times
    - Majority vote to obtain final output

    * Can be done by definind multiple prompts or a prompt generating multiple responses.
"""
self_consistency_instruction = "Imagine three completely independant experts who reason differentely are answering this question. The final answer is obtained by majority vote. The question is: "

problem_to_solve = "If there are 10 cars in the parking lot and 3 more cars arrive. Half the original number of cars leave. Then, half of the current number of cars arrive. How many cars are in there in the parking?"

prompt = self_consistency_instruction + problem_to_solve

print(get_response(prompt))

"""
Iterative prompt engineering
    - No prompt can be perfect at the beginning
    - Prompt Engineering is an iterative process where we:
        * Build a prompt
        * Feed it to the model
        * Observe and analyze the output
        * Reiterate to make the prompt better
    - Prompt refinement is used for various prompt types:
        * Few-shot promps: refine examples
        * Multi-step prompts: refine guiding steps
        * Chain-of-thought and self-consistency prompts: refine problem description

Steps for iterative prompt engineering
    1. Craft a prompt
    2. Send the prompt to the model
    3. Observe and analyze the output
    4. Identify potential issues with the prompt
    5. Refine the prompt
"""
# Refine the following prompt
not_refined_prompt = "Give me the top 10 pre-trained language models"
prompt = """
Create a table listing the top 10 pre-trained language models.

The table should have exactly three columns: model name, release year, and owning company.

Requirements:
- Include exactly 10 rows, one per model.
- Use the year the model was first publicly released.
- Use the name of the company or organization that developed the model.
- Output only the table, with no introduction or explanation.
"""

response = get_response(prompt)
print(response)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Refine the following prompt
prompt = """
Receiving a promotion at work made me feel on top of the world -> Happiness
The movie's ending left me with a heavy feeling in my chest -> Sadness
Walking alone in the dark alley sent shivers down my spine -> Fear
He walked to the store to buy some bread -> No explicit emotion
She opened the window and looked outside -> No explicit emotion
They sat and ate their meal ->
"""

response = get_response(prompt)
print(response)