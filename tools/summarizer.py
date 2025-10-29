# tools/summarizer.py
def summarize_results(analysis: str, tags: str, improvements: str) -> str:
    """Combine all agent outputs into one report."""
    return f"""
### Repository Analysis Report

**Structure Summary:**
{analysis}

**Suggested Tags:**
{tags}

**Improvement Suggestions:**
{improvements}
"""
