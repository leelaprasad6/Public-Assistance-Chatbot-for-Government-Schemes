import numpy as np
import json
from langchain_community.vectorstores import Chroma

# Load embeddings and metadata from the files
embeddings = np.load(r'C:\Users\kabra\OneDrive\Desktop\BTECH_FINAL_YEAR_PROJECT\GPT\Docs\embeddings.npy')
with open(r'C:\Users\kabra\OneDrive\Desktop\BTECH_FINAL_YEAR_PROJECT\GPT\Docs\metadata.json', 'r', encoding='utf-8') as file:
    metadata = json.load(file)
    
# Initialize Chroma vector store with persistent storage
persist_directory = r'C:\Users\kabra\OneDrive\Desktop\BTECH_FINAL_YEAR_PROJECT\GPT\Vector_store'
vector_store = Chroma(collection_name='gov_schemes', persist_directory=persist_directory)

# Prepare documents to add
texts = []
metadatas = []
embeddings_list = []

for i, embedding in enumerate(embeddings):
    page_content = (
        f"{metadata[i]['scheme_name']} "
        f"{metadata[i]['details']} "
        f"{metadata[i]['benefits']} "
        f"{metadata[i]['eligibility']} "
        f"{metadata[i]['application_process']} "
        f"{metadata[i]['documents_required']}"
    )
    texts.append(page_content)
    metadatas.append({
        'id': metadata[i]['sr_no'],
        **{k: v for k, v in metadata[i].items() if k != 'embedding'}
    })
    embeddings_list.append(embedding.tolist())  

# Add documents 
for i, text in enumerate(texts):
    vector_store._collection.upsert(
        embeddings=[embeddings_list[i]],
        metadatas=[metadatas[i]],
        documents=[text],
        ids=[metadatas[i]['id']]
    )

vector_store.persist()