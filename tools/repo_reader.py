# tools/repo_reader.py
import requests

def read_github_readme(repo_url: str) -> str:
    """Read README.md from GitHub repo."""
    if not repo_url.endswith("/"):
        repo_url += "/"
    raw_url = repo_url.replace("github.com", "raw.githubusercontent.com") + "main/README.md"
    response = requests.get(raw_url)
    return response.text if response.status_code == 200 else "README not found."
