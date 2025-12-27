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
Public-Assistance-Chatbot-for-Government-Schemes/
│
├── app.py # Flask application entry point
├── scraper/ # Government website scraping scripts
├── embeddings/ # Text embedding & vector logic
├── database/ # MongoDB & ChromaDB handlers
├── models/ # LLM & NLP integration
├── utils/ # Helper utilities
├── templates/ # HTML templates
├── static/ # CSS / JS assets
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/leelaprasad6/Public-Assistance-Chatbot-for-Government-Schemes.git
cd Public-Assistance-Chatbot-for-Government-Schemes

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate    # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file:

OPENAI_API_KEY=your_openai_api_key
MONGODB_URI=your_mongodb_connection_string
GOOGLE_APPLICATION_CREDENTIALS=path_to_gcp_credentials.json

5️⃣ Run the Application
python app.py

🧪 Sample Queries

“Schemes for farmers with low income”

“Scholarships for engineering students in India”

“Government benefits for disabled persons”

“Housing schemes for SC/ST families”

📊 Evaluation & Reliability

Cosine similarity thresholding for semantic accuracy

Manual evaluation using test queries

Eligibility-rule validation

Grounded LLM responses using retrieved documents

Fallback logic for missing data

⚠️ Limitations

Depends on the accuracy and freshness of scraped data

Internet connectivity required for LLM APIs

State-specific scheme variations may exist

OCR accuracy depends on document quality

🔮 Future Enhancements

Automated periodic data updates

User authentication & profile history

Voice-based interaction

Mobile application support

Analytics dashboard for scheme usage

👨‍💻 Author

Leela Prasad
B.Tech – Computer Science & Engineering
AI | NLP | Full-Stack Development
