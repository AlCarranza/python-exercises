from pe_01_introduction import get_response

"""
Text summarization
    - Condenses text into shorter format
    - Streamlines business processes
        - Finance: summarizes lengthy reports
        - Marketing: transforms customer feedback into actionable insights
    - LLMs can summarize texts with effective prompts

Keys to improve the prompt
    - Output limits: by the number of sentences, words or characters
    - Output structure
    - Summarization focus: ask the model to focus on some specific parts of the text
"""
ineffective_prompt = f"""Summarize the text delimited by triple backticks:
```{text}```"""

effective_prompt = f"""Summarize the smartwatch review in three sentences, focusing on key features and user experience."""

"""
Text expansion
    - Generates text from ideas or bullet points
    - Improves efficiency and productivity
    - LLMs can expand text with well-crafted prompts

Keys of text expansion
    - Ask model to expand delimited text
    - Highlight aspects to focus on
    - Provide output requirements (tone, length, structure, audience)
"""
expansion_prompt=f"""Expand the description for the Social XYZ service delimited by triple
backticks to provide an overiew of its features and benefits, without bypassing the limit of
two sentences. Use professional tone.
```{service_description}```"""

print(get_response(expansion_prompt))

"""
Text transformations
    - Transforms given text to create a new text
    - Has many applications:
        * Language translation
        * Tone adjustments
        * Writing improvement

Language translation
    - Specify the input and output language in prompt
"""
translate_language = f"""Translate the English text delimited by triple backticks to French:
```{text}```"""
request_language = f"""Tell me which language is the text delimited by triple backticks:
```{text}```"""
multilingual_translation = f"""Translate the English text delimited by triple backticks to French, Spanish and German
```{text}```"""

"""
Tone adjustments
    - Rewrite the text in a different tone.
    - You can also specify an audience

Grammar and writing improvements
    - Correct spelling, grammar, and punctuation mistakes without modifying other aspects.
    - Enhance clarity by modifying text structure
    - Ask for multiple transformations at once -> multi-step prompts
"""
other_tone = f"""Write the text delimited by triple backticks using a formal and persuasive tone:
```{text}```"""
specify_audience = f"""Write the text delimited by triple backticks to be suitable for a non-technical audience:
```{text}```"""
grammar_improvements = f"""Proofread the text delimited by triple backticks while keeping the original text structure intact:
```{text}```"""
grammar_improvements_structure = f"""Proofread and restructure the text delimited by triple backticks for enhanced readability, flow and coherence
```{text}```"""
multiple_transformations = f"""Transform the text delimited by triple backticks with the following two steps:
Step 1 - Proofread it without changing its structure
Step 2 - Change the tone to be professional
"""

"""
Text analysis
    - Examining text to extract information
        * Text classification
        * Entity extraction
    - Companies should seek legal advice when using customer data

Text classification
    - Assign a cathegory to text
    - Example: sentiment analysis

    Specify categories
        - Specify classification categories when known
        - Mention output requirements
    Unspecified categories
        - Model uses it's own knowledge when categories are not specified
        - For some open-ended problems this might not work well.
    
    Multiple classes
        - Text can fit into multiple classes
        - Define a maximum number of clases if they are not known
"""
specified_categories = f"""Classify the sentiment of the text delimited by backticks as positive, negative, or neutral. Give your answer as single word.
```{text}```"""
multiple_classes = f"""Identify emotions used in this text. Don't use more than 3 emotions.
Format your answer as a list of words separated by commas:
```{text}```"""

"""
Entity extraction
    - Extracting specific entities from text.
    - Example: names, places, organizations, dates.
"""
entity_extraction = f"""Identify the following entities from the text delimited by triple backticks.
                        - Product Name
                        - Dispplay Size
                        - Camera Resolution
                        Format the answer as an unordered list.
                        ```{text}```"""
"""
Entity extraction with few-shot prompts
    - Used for complex structures
"""
prompt = f"""Text: {ticket_1} -> Entities: {entities_1}
             Text: {ticket_2} -> Entities: {entities_2}
             Text: {ticket_3} -> Entities: """

"""
Code generation and explanation
    - Creating source code to solve a given problem
    - Essential in any domain using software solutions
    - Understanding generated code is essential for efective use

    Code generation prompts should include:
        * Problem description
        * Programming language
        * Format (script, function, class)

    We can provide input-output examples to generate a program that maps them
"""
prompt = "Write a Python function that accepts a list of quarterly sales, and outputs the average sales per quarter."

examples = """
Input: [150000, 180000, 200000, 170000] -> Output: 175000.0
Input: [10000, 25000, 30000, 15000] -> Output: 20000.0
Input: [50000, 75000, 60000, 45000] -> Output: 57500.0
"""

prompt_io_examples = f"""You are provided with input-output examples delimited by triple backtips for a python program that receives
a list of quarterly sales data.
Write code for this program.
```{examples}```"""

print(get_response(prompt_io_examples))

"""
Code modification
    - Ask the model to modify code according to requirements
"""
script = """
quarterly_sales = [150, 180, 200, 170]
total_sales = sum(quarterly_sales)
print("Total sales: ", total_sales)
"""
prompt_modify = f"""Modify the script delimited by triple backticks to a function that we can call to compute the total sales given quarterly sales
```{script}```"""
multiple_modifs = f"""Modify the script delimited by triple backticks as follows:
    - Let user input parameters interactively.
    - Make sure to verify inputs are positive, otherwise, display a message for the user, and ask them to provide their input again.
    ```{script}```"""

"""
Code explanation
    - Code can be difficult to interpret
    - LLMs can be used to explain code
"""
explain_code_prompt = f"""Explain in one sentence what the code delimited by triple backticks does
```{code}```"""

detailed_explain_code_prompt = f"""Explain what the code delimited by triple backticks does
Let's think step by step
```{code}```"""