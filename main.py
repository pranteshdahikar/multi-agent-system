# Replace the LangGraph part with a basic workflow
from agents.analyzer_agent import AnalyzerTool
from agents.metadata_agent import MetadataTool
from agents.improver_agent import ImproverTool
from tools.repo_reader import read_github_readme
from tools.summarizer import summarize_results

def run_multi_agent_system(repo_url: str):
    repo_content = read_github_readme(repo_url)
    analysis = AnalyzerTool.invoke(repo_content)
    tags = MetadataTool.invoke(analysis)
    improvements = ImproverTool.invoke(analysis)
    report = summarize_results(analysis, tags, improvements)
    print(report)

if __name__ == "__main__":
    repo = input("Enter GitHub repo URL: ")
    run_multi_agent_system(repo)
