"""
Auto Classes: flexible and powerful
    - Auto classes: Flexible access to models and tokenizers
    - More control: over model behavior and outputs
    - Perfect for advanced tasks
    - Pipelines = quick; Auto Classes = flexible
"""

"""
AutoModels: Choose an AutoModel class to directly download a model
"""
from transformers import AutoModelForSequenceClassification

# Download a pre-trained text classification model
model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english"
)

"""
AutoTokenizers
    - Prepare text input data
    - Recommended to use the tokenizer paired with the model

    - Tokenizers clean input and split text into tokens
    - Different models, different tokenizers

    Use cases for AutoModels and AutoTokenizers
        - Use for more control and customization
        - Text Processing: Clean and tokenize for specific use cases
        - Thresholding: Prioritize key categories in classification tasks
        - Complex Workflows: Control multi-stage processing and integration
"""
from transformers import AutoTokenizer

# Retrieve the tokenizer paired with the model
tokenizer = AutoTokenizer.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english"
)

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

# Tokenize input text
tokens = tokenizer.tokenize("AI: Helping robots think and humans overthink :)")
print(tokens)

"""
Building a Pipeline with Auto Classes
"""
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

# Download the model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

# Create the custom pipeline
my_pipeline = pipeline(
    task="sentiment-analysis",
    model=model,
    tokenizer=tokenizer
)