from ddgs import DDGS


def search_web(query):

    results_list = []

    try:

        with DDGS() as ddgs:

            results = ddgs.text(
                query,
                max_results=5
            )

            for result in results:

                title = result.get("title", "")
                body = result.get("body", "")
                href = result.get("href", "")

                formatted_result = f"""
Title: {title}

Snippet: {body}

Source: {href}
"""

                results_list.append(formatted_result)

        if not results_list:
            return ["No live search results found."]

        return results_list

    except Exception as e:

        return [f"Search Tool Error: {str(e)}"]