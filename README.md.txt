🧠 Multi-Agent Repository Analyzer
🚀 Production-Ready AI System | Module 3 – Agentic AI Developer Capstone

A production-grade multi-agent system that analyzes GitHub repositories — summarizing their structure, extracting metadata, and suggesting improvements.
This project extends the prototype from Module 2: Build a Multi-Agent System into a robust, tested, and user-ready AI application.

🌟 Project Overview

The Multi-Agent Repository Analyzer automates code understanding and review.
It uses a team of specialized AI agents to analyze a repository, extract metadata, and provide actionable improvement suggestions.

You can interact with it via a Streamlit web interface or directly through Python functions.

🏗️ System Architecture
🔹 Agents
Agent	Purpose
AnalyzerAgent	Summarizes repository content and identifies structure & documentation gaps.
MetadataAgent	Extracts structured metadata (project name, tech stack, author, license, etc.).
ImproverAgent	Suggests improvements for code quality, documentation, and structure.
🔹 Tools
Tool	Function
repo_reader	Reads and summarizes repository files (README, .py, .md, etc.)
web_search_tool	Performs web lookups using DuckDuckGo (optional for enrichment)
summarizer	Combines multi-agent outputs into a cohesive summary
guardrails	Validates inputs, filters outputs, and enforces safety rules
🔹 Workflow
RepoReader → AnalyzerAgent → MetadataAgent → ImproverAgent → Summarizer


Each agent operates independently but contributes to the shared analysis context.

🧩 Key Features

✅ Modular Multi-Agent System – Each agent handles a unique task
✅ LLM Integration – Uses langchain_openai.ChatOpenAI or a fallback DummyLLM
✅ Comprehensive Testing Suite – Unit + Integration + End-to-End tests
✅ Safety & Guardrails – Input validation, output filtering, and error handling
✅ Interactive Streamlit UI – Simple user interface for non-technical users
✅ Resilience – Graceful fallback when API or network calls fail
✅ Documentation & Maintainability – Clear module structure and inline comments

🧰 Project Structure
multi-agent-system/
│
├── agents/
│   ├── analyzer_agent.py
│   ├── improver_agent.py
│   ├── metadata_agent.py
│   └── __init__.py
│
├── tools/
│   ├── repo_reader.py
│   ├── summarizer.py
│   ├── web_search_tool.py
│   └── __init__.py
│
├── utils/
│   ├── guardrails.py
│   └── __init__.py
│
├── tests/
│   ├── test_analyzer_agent.py
│   ├── test_metadata_agent.py
│   ├── test_improver_agent.py
│   ├── test_end_to_end.py
│   └── __init__.py
│
├── ui/
│   └── app.py                  # Streamlit UI
│
├── your_dummy_llm.py           # Mock LLM for tests
├── main.py                     # Workflow orchestrator
├── requirements.txt
└── README.md                   # (This file)

⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/yourusername/multi-agent-system.git
cd multi-agent-system

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt


If langchain_openai or langchain_community are missing, install manually:

pip install langchain-openai langchain-community streamlit duckduckgo-search

🧪 Running Tests
Run all tests:
pytest -v

Expected Output:

✅ 3 passed, 1 skipped or passed depending on test environment
✅ 70%+ coverage on agents and tools

💻 Running the Application
Start the Streamlit UI
streamlit run ui/app.py


Then open your browser at:

http://localhost:8501

Example Usage

Enter a local repository path

Click “Analyze Repository”

View structured JSON output:

{
  "analysis": "...",
  "metadata": {...},
  "improvements": "..."
}

🧠 Safety & Guardrails

Implemented via utils/guardrails.py:

Input validation — rejects empty/malformed input

Output filtering — removes sensitive or unsafe content

Error handling — catches LLM or file read errors gracefully

Fallback LLM — uses DummyLLM if API unavailable

🔍 Resilience & Monitoring

Retry & fallback mechanisms for failed LLM or I/O operations

Safe defaults for repository scanning

Logging of critical errors and exceptions (to be extended with monitoring tools)

🎨 User Interface (Streamlit)
Feature	Description
Input field	Enter local repo path
“Analyze Repository”	Triggers multi-agent workflow
JSON Viewer	Displays final output (analysis, metadata, improvements)
Error Handling	Shows descriptive error messages
🧾 Example Output
{
  "analysis": "This repository implements a Python-based web service using FastAPI...",
  "metadata": {
    "project_name": "FastAPI Boilerplate",
    "technologies": ["Python", "FastAPI", "Docker"],
    "author": "John Doe",
    "license": "MIT"
  },
  "improvements": "Add test coverage, update documentation, follow PEP8."
}

🧩 Deployment Notes

For deployment on a server or container:

pip install gunicorn
gunicorn ui.app:app


Optional enhancements:

Dockerize with Dockerfile

Add logging & monitoring (Sentry / OpenTelemetry)

Integrate with CI/CD pipeline for test automation

📘 Troubleshooting
Issue	Possible Fix
streamlit: command not found	Run pip install streamlit
ModuleNotFoundError: langchain_openai	Run pip install langchain-openai
Tests failing due to LLM	Use DummyLLM for offline mode
Repository not found	Ensure valid local repo path or absolute directory
🏁 Learning Outcomes

By completing this project, you demonstrate:

Building & testing multi-agent AI systems

Implementing guardrails & safe execution flows

Creating user interfaces for AI tools

Achieving production-grade reliability

🧑‍💻 Author

Prantesh Dahikar
AI & Automation Engineer | Capstone Project for Agentic AI Developer Certification

🧩 License

MIT License © 2025 – Multi-Agent Repository Analyzer