"""
Summarization text
    - Can be Extractive vs. Abstractive
        * Extractive
            - Selects key sentences from the text
            - Efficient, needs fewer resources
            - Lacks flexibility; may be less cohesive
            - Ideal for legal documents (highlights key clauses) and financial research (extract insights)
        * Abstractive
            - Generates new, rephrased text
            - Clearer and more readable
            - Requires more resources and processing
            - Ideal for news articles (creates concise summaries) and content recommendations (generates compelling descriptions)
"""
from transformers import pipeline

# Extractive
summarizer = pipeline(
    "summarization",
    model="nyamuda/extractive-summarization"
)

text = "This is my really large text about Data Science..."
summary_text = summarizer(text)

print(summary_text[0]['summary_text'])

# Abstractive
summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

text = "This is my really large text about Data Science..."
summary_text = summarizer(text)

print(summary_text[0]['summary_text'])

"""
Parameters for summarization
    - min_new_tokens & max_new_tokens: Control summary length
"""
summarizer = pipeline("summarization", min_new_tokens=10, max_new_tokens=150)