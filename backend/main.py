from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agents import (
    search_agent,
    research_agent
)

# =========================================================
# FASTAPI APP CONFIG
# =========================================================

app = FastAPI(
    title="Multi-Agent Research Assistant",
    description="AI-powered research and report generation system",
    version="2.0.0"
)

# =========================================================
# CORS CONFIGURATION
# =========================================================

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

# =========================================================
# REQUEST MODEL
# =========================================================

class ResearchQuery(BaseModel):
    query: str

# =========================================================
# ROOT ROUTE
# =========================================================

@app.get("/")
def home():

    return {
        "message": "Multi-Agent Research Assistant API Running"
    }

# =========================================================
# RESEARCH ROUTE
# =========================================================

@app.post("/research")
def research(request: ResearchQuery):

    query = request.query

    # =====================================================
    # SEARCH AGENT
    # =====================================================

    search_results = search_agent(query)

    # =====================================================
    # MAIN RESEARCH AGENT
    # =====================================================

    ai_response = research_agent(search_results)

    # =====================================================
    # FINAL RESPONSE
    # =====================================================

    return {

        "status": "success",

        "research_topic": query,

        "agents": {

            "search_agent": {

                "status": "completed",

                "results_found": len(search_results),

                "data": search_results
            },

            "research_agent": {

                "status": "completed",

                "response": ai_response
            }
        }
    }