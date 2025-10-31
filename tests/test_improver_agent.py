from agents.improver_agent import ImproverAgent

def test_improver_agent_basic():
    agent = ImproverAgent()
    result = agent.suggest_improvements("The repo lacks tests and clear documentation.")
    assert isinstance(result, str)
    assert "documentation" in result.lower() or "test" in result.lower()
