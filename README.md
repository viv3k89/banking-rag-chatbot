# 🏦 Banking RAG Chatbot

A full-stack Generative AI application that allows users to upload banking-related PDF documents and ask contextual questions using Retrieval-Augmented Generation (RAG).

---

# 📌 Project Overview

The Banking RAG Chatbot enables users to:

- Upload banking PDF documents
- Process and store document content
- Ask natural language questions
- Retrieve contextual answers from uploaded documents

The system uses:

- FastAPI backend
- React frontend
- ChromaDB vector database
- LangChain-based RAG pipeline

---

# 🚀 Features

## Implemented Features

- PDF Upload Support
- Banking Knowledge Extraction
- Text Chunking
- Vector Database Storage
- Retrieval-Augmented Generation (RAG)
- Question Answering System
- FastAPI REST APIs
- React Frontend
- Cloud Deployment using Render
- GitHub Integration

---

# 🛠️ Tech Stack

## Frontend
- React.js
- Vite
- Axios
- CSS

## Backend
- FastAPI
- Python
- LangChain

## Vector Database
- ChromaDB

## Document Processing
- PyPDFLoader
- RecursiveCharacterTextSplitter

## Deployment
- GitHub
- Render

---

# 🏗️ Project Architecture

The project follows a Retrieval-Augmented Generation workflow.

## Architecture Flow

1. User uploads a banking PDF
2. Backend extracts text from PDF
3. Text is split into chunks
4. Chunks are stored in ChromaDB
5. User asks a question
6. Relevant chunks are retrieved
7. Response is generated from retrieved context
8. Answer is returned to frontend

---

# 📊 Architecture Diagram

```mermaid
flowchart TD

A[User] --> B[React Frontend]

B -->|Upload PDF| C[FastAPI Backend]
B -->|Ask Question| C

C --> D[PyPDFLoader]
D --> E[Text Chunking]
E --> F[Chroma Vector Database]

C --> G[Retriever]
G --> F

F --> H[Relevant Chunks Retrieved]
H --> I[Response Generator]

I --> C
C --> B
B --> A


banking-rag-chatbot/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── routes/
│   ├── rag/
│   └── data/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md


🔌 API Endpoints
Upload PDF
POST /upload

Uploads and processes PDF documents.

Chat Endpoint
POST /chat

Accepts user questions and returns contextual responses.

Request Body
{
  "question": "What is a home loan?"
}
Health Check
GET /health

Checks backend server status.

⚙️ Installation & Setup
1. Clone Repository
git clone https://github.com/viv3k89/banking-rag-chatbot.git
Backend Setup
Navigate to Backend
cd backend
Create Virtual Environment
Windows
python -m venv venv
Activate Virtual Environment
Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Run Backend
uvicorn app:app --reload

Backend runs on:

http://127.0.0.1:8000
Frontend Setup
Navigate to Frontend
cd frontend
Install Dependencies
npm install
Run Frontend
npm run dev

Frontend runs on:

http://localhost:5173
🌐 Deployment Links
Frontend

https://banking-rag-frontend.onrender.com

Backend

https://banking-rag-chatbot-0ki1.onrender.com

🧠 Example Workflow
Upload Banking PDF
Ask Question:
“What is a personal loan?”
“What is a home loan?”
Chatbot retrieves relevant banking information
Response displayed on frontend
⚠️ Challenges Faced

During development, several technical challenges were encountered:

Render free-tier memory limitations
Embedding optimization
CORS configuration
Backend deployment issues
Vector database persistence
Frontend-backend integration
🔮 Future Improvements
Integrate Gemini/OpenAI embeddings
Improve semantic retrieval accuracy
Add authentication system
Add persistent memory
Use cloud vector databases like Pinecone
Multi-document support
Better AI-generated summarized responses
📚 Learning Outcomes

This project provided practical experience in:

Full-stack AI development
FastAPI backend engineering
React frontend development
Retrieval-Augmented Generation
Vector databases
Cloud deployment
API integration
LangChain workflows
👨‍💻 Author
Vivek

GitHub:
https://github.com/viv3k89

✅ Conclusion

The Banking RAG Chatbot successfully demonstrates a complete Retrieval-Augmented Generation pipeline using modern AI engineering tools.

The project combines:

frontend development
backend APIs
vector databases
document intelligence
cloud deployment
Generative AI architecture

making it a strong portfolio and internship-level GenAI project.


After replacing:

```bash
git add .
git commit -m "Updated professional README"
git push origin main
