"""
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up Azure OpenAI configuration
openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2023-05-15")  # Default API version
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")

def generate_response(user_query: str, context: str) -> str:
    try:
        # Make a chat completion request to Azure OpenAI Service
        response = openai.ChatCompletion.create(
            engine=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),  # Azure-specific deployment name
            messages=[
                {"role": "system", "content": "You are a helpful support assistant specializing in Java. For all user queries, first consult the provided SQLite database. If the database contains relevant information, use it to construct your response. If the database lacks pertinent context but the query pertains to Java, utilize your internal knowledge to answer. For queries unrelated to Java or when the database lacks relevant information, inform the user that the information is not available."},
                {"role": "user", "content": user_query},
                {"role": "assistant", "content": context}
            ]
        )
        # Return the generated response
        return response['choices'][0]['message']['content']
    except Exception as e:
        # Handle and log errors gracefully
        return if"Error generating response: {str(e)}" """


import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up Azure OpenAI configuration
openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2023-05-15")
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")

def generate_response(user_query: str, context: str) -> str:
    try:
        # Make a chat completion request to Azure OpenAI Service
        response = openai.ChatCompletion.create(
            engine=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            messages=[
                {"role": "system", "content": "You are a helpful support assistant specializing in Java. For all user queries, first consult the provided knowledge base. If the knowledge base contains relevant information, use it to construct your response. If the knowledge base lacks pertinent context but the query pertains to Java, utilize your internal knowledge to answer. For queries unrelated to Java or when the knowledge base lacks relevant information, inform the user that the information is not available."},
                {"role": "user", "content": user_query},
                {"role": "assistant", "content": context}
            ]
        )
        # Return the generated response
        return response['choices'][0]['message']['content']
    except Exception as e:
        # Handle and log errors gracefully
        return f"Error generating response: {str(e)}"
