# agents/metadata_agent.py
from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool

llm = ChatOpenAI(model="gpt-4-turbo")

def suggest_tags(repo_summary: str) -> str:
    """Suggest tags or keywords for the repository."""
    prompt = f"Based on this project summary, suggest relevant tags or categories:\n\n{repo_summary}"
    return llm.invoke(prompt).content

MetadataTool = Tool.from_function(
    func=suggest_tags,
    name="MetadataRecommender",
    description="Suggests metadata tags based on the repo summary"
)
