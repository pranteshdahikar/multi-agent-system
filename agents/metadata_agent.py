# agents/metadata_agent.py
from langchain_openai import ChatOpenAI
from utils.guardrails import validate_input, filter_output
import json


class MetadataAgent:
    """Extracts high-level metadata such as purpose, author info, tags, and key components from a repository."""

    def __init__(self, llm=None):
        # Allow DummyLLM injection for testing
        self.llm = llm or ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

    def extract_metadata(self, repo_content: str) -> dict:
        """Extract repository metadata in structured form."""
        if not validate_input(repo_content):
            return {"error": "❌ Invalid input: repository content is empty or malformed."}

        prompt = (
            "You are an assistant that extracts structured metadata from GitHub repositories.\n"
            "Analyze the following repository description and return the result in JSON format with these keys:\n"
            "project_name, description, technologies, author, tags, license, repo_structure.\n\n"
            f"Repository content:\n{repo_content}\n\n"
            "Return only valid JSON (no commentary)."
        )

        try:
            response = self.llm.invoke(prompt)
            text = response.content if hasattr(response, "content") else str(response)
            clean_text = filter_output(text)

            try:
                data = json.loads(clean_text)
            except json.JSONDecodeError:
                # Fallback simple metadata parsing
                data = self._fallback_metadata(repo_content)
                data["raw_output"] = clean_text

            return data
        except Exception as e:
            return {"error": f"⚠️ Error during metadata extraction: {str(e)}"}

    def _fallback_metadata(self, repo_text: str) -> dict:
        """Simple rule-based metadata extraction as fallback."""
        lines = repo_text.splitlines()
        title = lines[0].strip("# ").strip() if lines else "Untitled"
        description = " ".join(lines[1:3]).strip() if len(lines) > 1 else "No description available."
        techs = [t for t in ["python", "java", "node", "react", "docker"] if t in repo_text.lower()]

        return {
            "project_name": title,
            "description": description,
            "technologies": techs or ["unspecified"],
            "author": "unknown",
            "tags": [],
            "license": "unspecified",
            "repo_structure": "basic",
        }


# ✅ Backward-compatible wrapper for main.py & tests
class MetadataTool(MetadataAgent):
    """
    Lightweight wrapper exposing `.run()` for test and main.py use.
    Provides minimal deterministic metadata extraction when LLM is unavailable.
    """

    def run(self, repo_text: str) -> dict:
        if not repo_text:
            return {"error": "Empty repository text"}

        lines = repo_text.splitlines()
        title = lines[0].strip("# ").strip() if lines else "Untitled"
        description = " ".join(lines[1:3]).strip() if len(lines) > 1 else "No description found."

        return {
            "title": title,
            "description": description,
            "metadata_summary": f"Project '{title}' — {description[:60]}...",
        }
