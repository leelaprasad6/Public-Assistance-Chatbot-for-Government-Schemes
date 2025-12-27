import os
import requests
from bs4 import BeautifulSoup
from langchain_community.vectorstores import Chroma
from sentence_transformers import SentenceTransformer
import openai

# Set the OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Load the SentenceTransformer model
model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')

# Define the embedding function
class EmbeddingFunction:
    def __init__(self, model):
        self.model = model

    def embed_documents(self, texts):
        return [self.model.encode(text).tolist() for text in texts]

    def embed_query(self, text):
        return self.model.encode(text).tolist()

embedding_function = EmbeddingFunction(model)

# Initialize Chroma vector store with the embedding function
persist_directory = r'C:\Users\kabra\OneDrive\Desktop\BTECH_FINAL_YEAR_PROJECT\GPT\Vector_store'
vector_store = Chroma(
    collection_name='gov_schemes',
    embedding_function=embedding_function,
    persist_directory=persist_directory
)

# Simple web retrieval function
def web_retrieve(query):
    url = "https://www.google.com/search?q=" + query
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    snippets = []
    for g in soup.find_all(class_='BVG0Nb'):
        snippet = g.text
        snippets.append(snippet)
    
    return snippets

# Function to integrate query results with an LLM
def generate_response(query, retrieved_docs):
    context = ""
    source_info = ""

    if retrieved_docs:
        context = "\n\n".join([f"Source: {doc.metadata.get('scheme_name', 'Unknown')}\n{doc.page_content}" for doc in retrieved_docs if doc.page_content.strip()])
        source_info = "The information is retrieved from the local vector store containing scraped government scheme data."
    else:
        web_results = web_retrieve(query)
        if not web_results:
            context = "I couldn't find relevant information in the provided documents or on the web."
            source_info = "No relevant information was found in the local data or on the web."
        else:
            context = "\n\n".join(web_results)
            source_info = "The information is retrieved from web search results."

    # Ensure context is not empty
    if not context.strip():
        context = "No relevant information found."

    prompt = f"Query: {query}\n\nContext: {context}\n\nAnswer strictly based on the provided context. Do not generate any information outside the given context.\n\nAnswer (Source: {source_info}):"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI assistant for answering questions only about government schemes of India. Use the provided context to answer the question. Always indicate your sources clearly in the response. Do not generate information that is not in the context. For any other question you will say that query was not about any government scheme."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.7
    )

    return response['choices'][0]['message']['content'].strip()
