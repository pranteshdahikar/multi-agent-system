# main.py

from agents.analyzer_agent import AnalyzerAgent
from agents.improver_agent import ImproverAgent
from agents.metadata_agent import MetadataAgent
from tools.repo_reader import read_repository, read_github_readme
from tools.summarizer import summarize_results


def run_workflow(repo_path: str, llm=None) -> dict:
    """
    End-to-end workflow: reads repository, analyzes it, extracts metadata, and suggests improvements.
    Allows optional injection of DummyLLM for testing.
    """
    # 1️⃣ Read repository content
    repo_content = read_repository(repo_path)
    if "❌" in repo_content:
        readme_fallback = read_github_readme(repo_path)
        repo_content = readme_fallback if readme_fallback else "❌ Repository appears empty."

    # 2️⃣ Initialize agents with shared LLM (real or dummy)
    analyzer = AnalyzerAgent(llm=llm)
    metadata = MetadataAgent()
    improver = ImproverAgent()

    # Inject DummyLLM manually if provided
    if llm is not None:
        metadata.llm = llm
        improver.llm = llm

    # 3️⃣ Run workflow steps
    analysis = analyzer.analyze(repo_content)
    metadata_info = metadata.extract_metadata(repo_content)
    improvement_suggestions = improver.suggest_improvements(repo_content)

    # 4️⃣ Summarize results
    summary = summarize_results({
        "analysis": analysis,
        "metadata": metadata_info,
        "improvements": improvement_suggestions
    })

    # 5️⃣ Return structured workflow result
    return {
        "analysis": analysis,
        "metadata": metadata_info,
        "improvements": improvement_suggestions,
        "summary": summary
    }


if __name__ == "__main__":
    # Example usage (manual run)
    repo_path = "./sample_repo"
    print(run_workflow(repo_path))
