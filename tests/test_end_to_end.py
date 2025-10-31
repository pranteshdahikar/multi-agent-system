def test_end_to_end(tmp_path):
    # create sample repo folder
    repo_dir = tmp_path / "sample"
    repo_dir.mkdir()
    (repo_dir / "README.md").write_text("# Sample\nThis is a sample")
    # use Dummy LLM that returns deterministic outputs
    from main import run_workflow
    from your_dummy_llm import DummyLLM
    out = run_workflow(str(repo_dir), DummyLLM())
    assert "sample" in out["analysis"].lower()
