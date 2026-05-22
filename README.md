Banking RAG Chatbot

A full-stack Generative AI application that allows users to upload banking-related PDF documents and ask contextual questions using Retrieval-Augmented Generation (RAG).

Project Overview

The Banking RAG Chatbot enables users to:

Upload banking PDF documents
Process and store document content
Ask natural language questions
Retrieve contextual answers from uploaded documents

The system uses:

FastAPI backend
React frontend
ChromaDB vector database
LangChain-based RAG pipeline
Features
Implemented Features
PDF Upload Support
Banking Knowledge Extraction
Text Chunking
Vector Database Storage
Retrieval-Augmented Generation (RAG)
Question Answering System
FastAPI REST APIs
React Frontend
Cloud Deployment using Render
GitHub Integration
Tech Stack
Frontend
React.js
Vite
Axios
CSS
Backend
FastAPI
Python
LangChain
Vector Database
ChromaDB
Document Processing
PyPDFLoader
RecursiveCharacterTextSplitter
Deployment
GitHub
Render
Project Architecture

The project follows a Retrieval-Augmented Generation workflow.

Architecture Flow
User uploads a banking PDF
Backend extracts text from PDF
Text is split into chunks
Chunks are stored in ChromaDB
User asks a question
Relevant chunks are retrieved
Response is generated from retrieved context
Answer is returned to frontend
Architecture Diagram
Folder Structure
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
API Endpoints
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

Installation & Setup
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
Deployment Links
Frontend
https://banking-rag-frontend.onrender.com
Backend
https://banking-rag-chatbot-0ki1.onrender.com
Example Workflow
Upload Banking PDF
Ask Question:
“What is a personal loan?”
“What is a home loan?”
Chatbot retrieves relevant banking information
Response displayed on frontend
Challenges Faced

During development, several technical challenges were encountered:

Render free-tier memory limitations
Embedding optimization
CORS configuration
Backend deployment issues
Vector database persistence
Frontend-backend integration
Future Improvements
Integrate Gemini/OpenAI embeddings
Improve semantic retrieval accuracy
Add authentication system
Add persistent memory
Use cloud vector databases like Pinecone
Multi-document support
Better AI-generated summarized responses
Current Limitations

To optimize deployment for Render free-tier hosting, lightweight placeholder embeddings are currently used instead of production-grade semantic embeddings.

This allows successful deployment while maintaining the complete RAG architecture.

Learning Outcomes

This project provided practical experience in:

Full-stack AI development
FastAPI backend engineering
React frontend development
Retrieval-Augmented Generation
Vector databases
Cloud deployment
API integration
LangChain workflows
Author
Vivek

GitHub:

https://github.com/viv3k89
Conclusion

The Banking RAG Chatbot successfully demonstrates a complete Retrieval-Augmented Generation pipeline using modern AI engineering tools.

The project combines:

frontend development
backend APIs
vector databases
document intelligence
cloud deployment
Generative AI architecture

making it a strong portfolio and internship-level GenAI project.
