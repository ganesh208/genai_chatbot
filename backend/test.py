import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API key and endpoint
openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-08-01-preview")
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")

def generate_embedding(text):
    response = openai.Embedding.create(
        engine=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),  # Use the correct deployment name
        input=text
    )
    return response['data'][0]['embedding']

# Sample text
sample_text = "This is a test sentence for embedding generation."

# Generate embedding
embedding = generate_embedding(sample_text)
print(f"Generated embedding: {embedding[:5]}...")  # Print first 5 elements for brevity
