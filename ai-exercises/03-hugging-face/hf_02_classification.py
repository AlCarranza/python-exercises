"""
Text classification: Sentiment analysis
    - Labels text based on its emotional tone
    - Applications: Analysis reviews, tracking social media sentiment
"""
from tansformers import pipeline

my_pipeline = pipeline(
    task="text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

print(my_pipeline("Wi-Fi is sliwe than a snail today!"))

"""
Text classification: Grammatical correctness
    - Evaluates text grammar for correctness
    - Applications: Grammar checkers, language learning tools
"""
grammar_checker = pipeline(
    task="text-classification",
    model="abdulmatinomotoso/English_Grammar_Checker"
)

print(grammar_checker("He eat pizza every day."))

"""
Text classification: QNLI
    - Checks if a premise answers a question
    - Applications: Q&A systems, fact-checking
"""
classifier = pipeline(
    task="text-classification",
    model="cross-encoder/qnli-electra-base"
)
classifier("Where is Seattle located?, Seattle is located in Washington state.")

"""
Text classification: Dynamic category assignment
    - Dynamically assigns categories based on content
    - Content moderation, recommendation systems
"""
classifier = pipeline(
    task="zero-shot-classification",
    model="facebook/bart-large-mnli"
)

text = "Hey, DataCamp; we would like to feature youir courses in out newsletter!"
categories = ["marketing", "sales", "support"]

output = classifier(text, categories)

print(f"Top Label: {output['labels'][0]} with score: {output['scores'][0]}")

"""
Challenges of text classification:
    - Ambiguity
    - Sarcasm, Irony
    - Multilingual
"""

