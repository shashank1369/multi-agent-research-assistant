import { useState } from "react";
import axios from "axios";
import ReactMarkdown from "react-markdown";

function App() {

  const [query, setQuery] = useState("");

  const [loading, setLoading] = useState(false);

  const [result, setResult] = useState(null);

  const handleResearch = async () => {

    if (!query) return;

    setLoading(true);

    try {

      const response = await axios.post(
        "https://multi-agent-research-assistant-production-49a6.up.railway.app/research",
        {
          query: query
        }
      );

      setResult(response.data);

    } catch (error) {

      console.error(error);

      alert("Error calling backend API");

    }

    setLoading(false);
  };

  return (

    <div style={styles.container}>

      {/* HEADER */}

      <div style={styles.header}>

        <h1 style={styles.title}>
          Multi-Agent Research Assistant
        </h1>

        <p style={styles.subtitle}>
          AI-powered research pipeline using Search,
          Retrieval, Analysis, and Report Generation.
        </p>

      </div>

      {/* SEARCH BOX */}

      <div style={styles.searchBox}>

        <input
          type="text"
          placeholder="Enter research topic..."
          value={query}

          onChange={(e) => setQuery(e.target.value)}

          onKeyDown={(e) => {
            if (e.key === "Enter") {
              handleResearch();
            }
          }}

          style={styles.input}
        />

        <button
          onClick={handleResearch}
          style={styles.button}
          disabled={loading}
        >
          {loading ? "Researching..." : "Research"}
        </button>

      </div>

      {/* LOADING */}

      {loading && (

        <div style={styles.loading}>
          <h2>Agents are researching...</h2>
        </div>

      )}

      {/* RESULTS */}

      {result && (

        <div style={styles.resultContainer}>

          {/* SEARCH AGENT */}

          <div style={styles.card}>

            <h2 style={styles.agentTitle}>
              Search Agent
            </h2>

            <p>
              Results Found:
              {" "}
              {result.agents.search_agent.results_found}
            </p>

          </div>

          {/* MAIN RESEARCH AGENT */}

          <div style={styles.card}>

            <h2 style={styles.agentTitle}>
              AI Research Analysis
            </h2>

            <ReactMarkdown>
              {result.agents.research_agent.response}
            </ReactMarkdown>

          </div>

        </div>
      )}

    </div>
  );
}

const styles = {

  container: {
    padding: "40px",
    maxWidth: "1100px",
    margin: "auto"
  },

  header: {
    textAlign: "center",
    marginBottom: "40px"
  },

  title: {
    fontSize: "48px",
    marginBottom: "10px",
    color: "white"
  },

  subtitle: {
    color: "#94a3b8",
    fontSize: "18px",
    lineHeight: "1.6"
  },

  searchBox: {
    display: "flex",
    gap: "12px",
    marginBottom: "30px"
  },

  input: {
    flex: 1,
    padding: "18px",
    fontSize: "16px",
    borderRadius: "12px",
    border: "1px solid #334155",
    backgroundColor: "#1e293b",
    color: "white",
    outline: "none"
  },

  button: {
    padding: "16px 24px",
    backgroundColor: "#2563eb",
    color: "white",
    border: "none",
    borderRadius: "12px",
    cursor: "pointer",
    fontWeight: "bold",
    fontSize: "16px",
    transition: "0.2s"
  },

  loading: {
    textAlign: "center",
    marginTop: "30px",
    marginBottom: "30px",
    color: "#60a5fa"
  },

  resultContainer: {
    display: "flex",
    flexDirection: "column",
    gap: "20px"
  },

  card: {
    backgroundColor: "#1e293b",
    padding: "24px",
    borderRadius: "16px",
    border: "1px solid #334155",
    boxShadow: "0px 4px 20px rgba(0,0,0,0.3)"
  },

  agentTitle: {
    color: "#60a5fa",
    marginBottom: "16px"
  }
};

export default App;