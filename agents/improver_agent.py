# agents/improver_agent.py
from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool

llm = ChatOpenAI(model="gpt-4-turbo")

def improve_readme(repo_summary: str) -> str:
    """Suggest improvements to the README layout or writing."""
    prompt = f"Given this summary, suggest improvements to the README or documentation clarity:\n\n{repo_summary}"
    return llm.invoke(prompt).content

ImproverTool = Tool.from_function(
    func=improve_readme,
    name="ContentImprover",
    description="Suggests better README structure or content improvements"
)
