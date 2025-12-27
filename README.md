# 🏛️ Government Schemes Chatbot (Public Assistance AI)

An AI-powered chatbot that helps Indian citizens discover, understand, and apply for relevant **government welfare schemes** based on eligibility and personal details.  
The system combines **Semantic Search**, **Vector Databases**, and **Large Language Models (LLMs)** to deliver accurate, grounded, and user-friendly responses.

---

## 🎯 Problem Statement

Government welfare schemes are distributed across multiple portals, written in complex language, and difficult to navigate. This leads to low awareness and underutilization.

This project addresses the problem by providing a **single intelligent assistant** that:
- Understands natural language queries
- Matches schemes using semantic similarity
- Validates eligibility
- Explains benefits simply
- Guides users step-by-step through application procedures

---

## 🚀 Key Features

- 🔍 Semantic search over government scheme data
- 🧠 LLM-powered conversational responses
- 📋 Eligibility validation using user inputs
- 🌐 Multilingual query support
- 📄 Document handling with OCR (Google Vision API)
- 🗂️ Fast retrieval using ChromaDB (vector store)
- 🔄 Web-search fallback when no scheme is found
- 🧩 Step-by-step application guidance

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask

### AI / NLP
- OpenAI / Gemini (LLM)
- Sentence Transformers
- ChromaDB (Vector Database)
- Semantic Similarity Search

### Data & Storage
- MongoDB
- JSON-based structured data
- Web-scraped government scheme datasets

### Other Tools
- Google Cloud Vision API (OCR)
- BeautifulSoup (Web Scraping)
- LangChain

---

## 🧠 System Architecture

1. User submits a query
2. Input preprocessing & language handling
3. Embeddings generated using Sentence Transformers
4. Semantic search performed on ChromaDB
5. Eligibility rules applied
6. LLM generates a grounded response using retrieved data
7. Web fallback triggered if no scheme matches
8. Final verified response returned to the user

---

## 📂 Project Structure

