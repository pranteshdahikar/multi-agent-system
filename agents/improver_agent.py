# agents/improver_agent.py

from langchain_openai import ChatOpenAI
from utils.guardrails import validate_input, filter_output


class ImproverAgent:
    """
    Suggests improvements for code quality, documentation, and structure.
    Uses an LLM for rich analysis, with a deterministic fallback.
    """

    def __init__(self, llm=None):
        # Allow DummyLLM injection for testing
        self.llm = llm or ChatOpenAI(model="gpt-4o-mini", temperature=0.4)

    def suggest_improvements(self, repo_content: str) -> str:
        """Generate practical improvement suggestions for the repository."""
        if not validate_input(repo_content):
            return "❌ Invalid input: repository content is empty or malformed."

        prompt = (
            "You are an expert code reviewer. Analyze the GitHub repository content below "
            "and provide improvement suggestions:\n\n"
            "1️⃣ Code quality feedback\n"
            "2️⃣ Documentation improvements\n"
            "3️⃣ Architecture or structure suggestions\n"
            "4️⃣ Missing best practices\n\n"
            f"Repository content:\n{repo_content}\n\n"
            "Give concise, actionable, bullet-point feedback."
        )

        try:
            response = self.llm.invoke(prompt)
            text = response.content if hasattr(response, "content") else str(response)
            return filter_output(text)
        except Exception as e:
            # Fallback to basic rule-based improvement suggestions
            return self._fallback_improvements(repo_content, str(e))

    def _fallback_improvements(self, repo_text: str, error_msg: str) -> str:
        """Fallback rule-based analysis if LLM is unavailable."""
        suggestions = []
        if "install" not in repo_text.lower():
            suggestions.append("Add installation instructions.")
        if "usage" not in repo_text.lower():
            suggestions.append("Include a usage example section.")
        if "license" not in repo_text.lower():
            suggestions.append("Mention a license type.")
        if not suggestions:
            suggestions.append("README looks well documented and complete.")

        summary = f"⚠️ Fallback due to LLM error ({error_msg}).\n" \
                  f"Found {len(suggestions)} improvement suggestion(s)."
        return summary + "\n- " + "\n- ".join(suggestions)


# ✅ Backward-compatible wrapper
class ImproverTool(ImproverAgent):
    """
    Wrapper exposing a `.run()` method (for use in main.py and tests).
    """

    def run(self, repo_text: str) -> dict:
        if not validate_input(repo_text):
            return {"error": "Empty repository text"}

        result = self.suggest_improvements(repo_text)
        suggestions = []

        # Extract structured suggestions (basic parsing)
        for line in result.splitlines():
            if "-" in line or "•" in line:
                suggestions.append(line.strip("•- "))

        if not suggestions:
            suggestions = [result.strip()]

        return {
            "suggestions": suggestions,
            "improvement_summary": f"{len(suggestions)} improvement suggestion(s).",
        }
