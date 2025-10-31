# utils/guardrails.py

import re
import html

def validate_input(text: str) -> bool:
    """Check if input text is non-empty and safe to process."""
    return bool(text and isinstance(text, str) and len(text.strip()) > 0)

def sanitize_input(text: str) -> str:
    """Clean input text to prevent prompt injection or unwanted code."""
    text = html.escape(text)
    text = re.sub(r"(?i)(delete|drop|shutdown|sudo|system\(|os\.|subprocess)", "[REDACTED]", text)
    return text.strip()

def filter_output(output: str) -> str:
    """Filter LLM outputs for potentially unsafe or verbose content."""
    if not output:
        return "No response generated."
    output = re.sub(r"(CONFIDENTIAL|SECRET|PRIVATE)", "[REDACTED]", output, flags=re.I)
    return output.strip()
