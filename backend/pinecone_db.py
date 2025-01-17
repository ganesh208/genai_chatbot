import os
import openai
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

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

# Check if the index exists; if not, create it
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1536,  # Ensure this matches your embedding model's output dimension
        metric='cosine',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-west-2'  # Adjust based on your requirements
        )
    )

# Connect to the index
index = pc.Index(index_name)

def generate_embedding(text: str):
    response = openai.Embedding.create(
        input=text,
        deployment_id=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME1")
    )
    return response['data'][0]['embedding']

def get_relevant_context(user_query: str, top_k: int = 3) -> str:
    # Generate the embedding for the user query
    query_embedding = generate_embedding(user_query)
    
    # Query the index for the most similar contexts
    results = index.query(vector=query_embedding, top_k=top_k)
    
    # Extract and return the relevant contexts, checking for 'metadata'
    contexts = []
    for match in results['matches']:
        if 'metadata' in match and 'text' in match['metadata']:
            contexts.append(match['metadata']['text'])
    return "\n\n".join(contexts)
