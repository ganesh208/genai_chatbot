import os
from dotenv import load_dotenv 
from pypdf import PdfReader 
import openai 
from pinecone import Pinecone

# Load environment variables from .env file
load_dotenv()

# Initialize Pinecone
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# Set up OpenAI API key and endpoint
openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT1")
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION1", "2023-05-15")
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")

# Define the index name
index_name = 'chatbot-index'

# Connect to the index
index = pc.Index(index_name)

def extract_text_from_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"The file {pdf_path} does not exist.")
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def generate_embedding(text):
    response = openai.Embedding.create(
        engine=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME1"),  # Use the correct deployment name
        input=text
    )
    return response['data'][0]['embedding']

def upsert_text_to_pinecone(text, doc_id):
    embedding = generate_embedding(text)
    print(f"Generated embedding: {embedding[:5]}...")
    index.upsert([(doc_id, embedding, {'text': text})])

if __name__ == "__main__":
    pdf_path = r"C:\Users\DELL\Desktop\Projects\genai_chatbots\backend\java_doc.pdf"  # Update this if the file path is incorrect
    try:
        extracted_text = extract_text_from_pdf(pdf_path)
        upsert_text_to_pinecone(extracted_text, "java_doc_1")
        print("Text extracted and upserted to Pinecone successfully.")
    except FileNotFoundError as e:
        print(e)
