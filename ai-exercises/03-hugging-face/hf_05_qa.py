"""
What is document question and answering?
    - Answers questions from document content
    - Requires a document and a question
    - Provides direct or paraphrased answers

    Use cases:
        - Legal: Identify contract clauses
        - Finance: Extract key figures
        - Support: Retrieve answers from manuals
"""
# Extracting text with pypdf
from pypdf import PdfReader
from transformers import pipeline


# Load the PDF file
reader = PdfReader("US-Employee_Policy.pdf")

# Extract text from all pages
document_text = ""
for page in reader.pages:
    document_text += page.extract_text()

# Load the question-answering pipeline
qa_pipeline = pipeline(
    task="question-answering",
    model="distilbert-base-cased-distilled-squad"
)

question = "How many volunteer days are offered annually?"

# Get the answer from the QA pipeline
result = qa_pipeline(question=question, context=document_text)
print(f"Answer: {result['answer']}")