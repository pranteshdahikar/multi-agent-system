# agents/analyzer_agent.py

# ✅ Compatibility import for both new and old LangChain versions
try:
    from langchain_openai import ChatOpenAI  # newer versions
except ImportError:
    from langchain.chat_models import ChatOpenAI  # fallback for older versions

from utils.guardrails import validate_input, filter_output


class AnalyzerAgent:
    """
    Analyzes repository content or documentation and produces structured summaries.
    Falls back to a basic keyword-based analysis if LLM is unavailable.
    """

    def __init__(self, llm=None):
        # Allow DummyLLM injection for tests
        self.llm = llm or ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

    def analyze(self, repo_content: str) -> str:
        """Analyze repository content using an LLM, with guardrails."""
        if not validate_input(repo_content):
            return "❌ Invalid input: repository content is empty or not a valid string."

        prompt = (
            "You are an AI assistant that analyzes GitHub repository content. "
            "Given the repository README or file structure, summarize:\n"
            "1️⃣ Project purpose\n"
            "2️⃣ Technologies used\n"
            "3️⃣ Code structure overview\n"
            "4️⃣ Missing documentation areas\n\n"
            f"Repository content:\n{repo_content}\n\n"
            "Provide a concise, structured summary."
        )

        try:
            response = self.llm.invoke(prompt)
            text = response.content if hasattr(response, "content") else str(response)
            return filter_output(text)
        except Exception as e:
            # Fallback analysis if LLM call fails
            return self._fallback_analysis(repo_content, str(e))

    def _fallback_analysis(self, repo_text: str, error_msg: str) -> str:
        """Fallback analysis logic when LLM fails."""
        lines = repo_text.splitlines()
        num_lines = len(lines)
        keywords = ["api", "ml", "data", "cloud", "test", "docker"]
        found_keywords = [kw for kw in keywords if kw.lower() in repo_text.lower()]
        return (
            f"⚠️ LLM unavailable ({error_msg}). "
            f"Fallback analysis: {num_lines} lines, keywords found: {found_keywords}"
        )


# ✅ AnalyzerTool wrapper for backward compatibility (used in main.py & tests)
class AnalyzerTool(AnalyzerAgent):
    """
    Wrapper that exposes a `.run()` method for backward compatibility with tests and main workflow.
    """

    def run(self, repo_text: str) -> dict:
        if not validate_input(repo_text):
            return {"error": "Empty repository text"}

        analysis_result = self.analyze(repo_text)
        return {
            "analysis_summary": analysis_result,
        }
