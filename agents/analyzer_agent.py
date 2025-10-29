# agents/analyzer_agent.py
from langchain_community.chat_models import ChatOpenAI
from langchain.tools import Tool

llm = ChatOpenAI(model="gpt-4-turbo")

def analyze_repo(repo_content: str) -> str:
    """Analyze repo content (e.g., README, structure)."""
    prompt = f"Analyze the following GitHub repository content and summarize its purpose and structure:\n\n{repo_content}"
    return llm.invoke(prompt).content

AnalyzerTool = Tool.from_function(
    func=analyze_repo,
    name="RepoAnalyzer",
    description="Analyzes the content and structure of a GitHub repository"
)
