from agents.metadata_agent import MetadataAgent

def test_metadata_agent_basic():
    agent = MetadataAgent()
    result = agent.extract_metadata("Sample Python repo for a trading bot by Prantesh.")
    assert isinstance(result, dict)
    assert "project_name" in result or "raw_output" in result
