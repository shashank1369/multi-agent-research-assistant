from agents import (
    search_agent,
    summarizer_agent,
    fact_checker_agent,
    report_agent
)

query = "Blockchain security threats"

print("\nSEARCH AGENT RUNNING...\n")

search_results = search_agent(query)

print(search_results)

print("\nSUMMARIZER AGENT RUNNING...\n")

summary = summarizer_agent(search_results)

print(summary)

print("\nFACT CHECKER AGENT RUNNING...\n")

fact_check = fact_checker_agent(summary)

print(fact_check)

print("\nREPORT AGENT RUNNING...\n")

final_report = report_agent(summary, fact_check)

print(final_report)