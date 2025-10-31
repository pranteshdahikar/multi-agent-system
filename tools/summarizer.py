# tools/summarizer.py
from langchain_openai import ChatOpenAI
from utils.guardrails import validate_input, filter_output


def summarize_text(text: str) -> str:
    """Summarizes text (like README or repo content) into clear bullet points."""
    if not validate_input(text):
        return "❌ Invalid input: text is empty or malformed."

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
    prompt = (
        "You are a summarization assistant. Summarize the following text into 3–5 clear bullet points:\n\n"
        f"{text}\n\n"
        "Provide only the summarized points."
    )
    try:
        response = llm.invoke(prompt)
        summary = response.content if hasattr(response, "content") else str(response)
        return filter_output(summary)
    except Exception as e:
        return f"⚠️ Error during summarization: {str(e)}"


def summarize_results(results: dict) -> str:
    """Summarizes combined results (metadata, analysis, improvements) into a final summary."""
    if not isinstance(results, dict) or not results:
        return "❌ Invalid input: no results to summarize."

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
    prompt = (
        "You are an assistant summarizing results from a multi-agent repository analysis.\n"
        "Write 4–6 concise bullet points summarizing the overall findings.\n\n"
        f"Results:\n{results}\n\n"
        "Return only the summarized bullet points."
    )
    try:
        response = llm.invoke(prompt)
        summary = response.content if hasattr(response, "content") else str(response)
        return filter_output(summary)
    except Exception as e:
        return f"⚠️ Error during summarization: {str(e)}"
