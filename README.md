# Multi-Agent Research Assistant

An AI-powered research assistant that performs intelligent web research using multiple AI agents for search, analysis, and report generation.

---

# Live Demo

## Frontend (Vercel)

https://multi-agent-research-assistant-six.vercel.app/

---

## Backend API (Railway)

https://multi-agent-research-assistant-production-49a6.up.railway.app/

---

## Deployed link

API URL:

https://multi-agent-research-assistant-production-49a6.up.railway.app/


---

# Features

- AI-powered research workflow
- Web search integration
- Gemini AI analysis
- Research report generation
- FastAPI backend
- React frontend
- Markdown rendering support
- Fully deployed cloud application

---

# Tech Stack

## Frontend
- React.js
- Vite
- Axios
- React Markdown

## Backend
- FastAPI
- Python
- Gemini API
- DuckDuckGo Search

## Deployment
- Vercel (Frontend)
- Railway (Backend)

---

# System Architecture

```text
                ┌────────────────────┐
                │    React Frontend   │
                │      (Vercel)       │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │   FastAPI Backend   │
                │      (Railway)      │
                └─────────┬──────────┘
                          │
         ┌────────────────┴────────────────┐
         ▼                                 ▼
┌──────────────────┐          ┌─────────────────────┐
│   Search Agent    │          │   Research Agent    │
│ DuckDuckGo Search │          │ Gemini AI Analysis  │
└──────────────────┘          └─────────────────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Structured Research │
                │       Report        │
                └────────────────────┘




##Project Workflow

User enters a research topic
Frontend sends request to FastAPI backend
Search Agent gathers web research data
Gemini AI analyzes the findings
AI generates structured research response
Frontend renders the final report




##Folder Structure

multi_agent_research_assistant/
│
├── backend/
│   ├── agents.py
│   ├── main.py
│   ├── tools.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   │
│   ├── package.json
│   └── vite.config.js
│
└── README.md


##Local Installation Guide

1. Clone Repository
git clone https://github.com/shashank1369/multi-agent-research-assistant.git
2. Move Into Project
cd multi-agent-research-assistant
Backend Setup
3. Open Backend Folder
cd backend
4. Create Virtual Environment
python -m venv venv
5. Activate Virtual Environment
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
6. Install Dependencies
pip install -r requirements.txt
7. Create .env File

Create a .env file inside backend folder.

Add:

GEMINI_API_KEY=your_gemini_api_key
8. Run Backend Server
uvicorn main:app --reload

Backend runs at:

http://127.0.0.1:8000
Frontend Setup
9. Open New Terminal

Move to frontend folder:

cd frontend
10. Install Frontend Dependencies
npm install
11. Start Frontend
npm run dev

Frontend runs at:

http://localhost:5173
API Endpoints
Root Endpoint
GET /

Response:

{
  "message": "Multi-Agent Research Assistant API Running"
}
Research Endpoint
POST /research

Request Body:

{
  "query": "blockchain security threats"
}
Deployment
Frontend Deployment

Frontend deployed using:

Vercel

Live URL:

https://multi-agent-research-assistant-six.vercel.app/

Backend Deployment

Backend deployed using:

Railway


Environment Variables
Backend
GEMINI_API_KEY=your_api_key
Future Improvements
Multi-agent orchestration
PDF export support
Citation generation
AI memory integration
Authentication system
Research history storage
Streaming AI responses
Screenshots
Homepage

<img width="1907" height="975" alt="image" src="https://github.com/user-attachments/assets/b8562c75-6a14-4db6-9535-39005db796e5" />


Author
Shashank Mamidi

GitHub:

https://github.com/shashank1369

License

This project is for educational and portfolio purposes.
