import pytest
from agents.analyzer_agent import AnalyzerAgent

class DummyLLM:
    def generate(self, prompt):
        return "dummy summary"

def test_analyze_minimal():
    agent = AnalyzerAgent(DummyLLM())
    out = agent.analyze("Short README content")
    assert "dummy" in out.lower()
