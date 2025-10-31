# utils/dummy_llm.py
"""
A simple deterministic fake LLM for testing agents.
Used in pytest to simulate consistent language model responses.
"""

class DummyLLM:
    """Mock LLM that returns predictable responses for tests."""

    def invoke(self, prompt: str):
        # This mimics the structure returned by LangChain ChatOpenAI.invoke()
        return type("Response", (), {"content": f"Dummy response for: {prompt[:60]}..."})
