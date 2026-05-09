import google.generativeai as genai
from dotenv import load_dotenv
import os

from tools import search_web

# =========================================================
# LOAD ENV VARIABLES
# =========================================================

load_dotenv()

# =========================================================
# CONFIGURE GEMINI
# =========================================================

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

# =========================================================
# SEARCH AGENT
# =========================================================

def search_agent(query):

    try:

        results = search_web(query)

        if not results:
            return ["No live search results found."]

        return results

    except Exception as e:

        return [f"Search Agent Error: {str(e)}"]


# =========================================================
# MAIN RESEARCH AGENT
# =========================================================

def research_agent(search_data):

    prompt = f"""
    You are an advanced AI research assistant.

    Analyze the following research data.

    Generate the following sections:

    ## SUMMARY
    Give a concise summary.

    ## FACT CHECK
    Identify possible inaccuracies or unsupported claims.

    ## FINAL REPORT
    Generate a professional research report with:
    - Introduction
    - Key Findings
    - Risks/Challenges
    - Conclusion

    Research Data:
    {search_data}
    """

    try:

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"Research Agent Error: {str(e)}"