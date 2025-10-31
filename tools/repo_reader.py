# tools/repo_reader.py

import os


def read_github_readme(repo_path: str) -> str:
    """
    Reads the README.md file from a local or cloned GitHub repository.
    """
    readme_path = os.path.join(repo_path, "README.md")
    if not os.path.exists(readme_path):
        return "❌ README.md not found in repository."
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"⚠️ Error reading README.md: {e}"


def read_repository(repo_path: str) -> str:
    """
    Reads key files (README, setup, main files, docs) from a repository
    and combines their content for analysis.
    """
    collected = []
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.lower().endswith((".py", ".md", ".txt", ".json", ".yaml", ".yml")):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        collected.append(f"\n### {file} ###\n{content}\n")
                except Exception as e:
                    collected.append(f"\n⚠️ Could not read {file}: {e}")

    return "\n".join(collected) if collected else "❌ No readable files found."


class RepoReader:
    """Unified class wrapper to read repository contents for analysis."""

    def read_repo(self, repo_path: str) -> str:
        """
        Primary entrypoint for reading repository contents.
        Prioritizes README.md, falls back to full repo scan.
        """
        readme = read_github_readme(repo_path)
        if not readme.startswith("❌"):
            return readme

        return read_repository(repo_path)
