# your_dummy_llm.py

class DummyResponse:
    """A simple object that mimics an LLM response with a .content attribute."""
    def __init__(self, content: str):
        self.content = content


class DummyLLM:
    """Deterministic LLM simulator for testing."""
    def invoke(self, prompt: str) -> DummyResponse:
        # Always include 'sample' so tests can validate easily
        return DummyResponse(f"Analysis complete: this repo contains the word 'sample'. Prompt snippet: {prompt[:50]}")

    # Optional for compatibility with ChatOpenAI-like interface
    def __call__(self, prompt: str) -> DummyResponse:
        return self.invoke(prompt)
