def generate_prompt(cfg: dict) -> str:
    """Turn a parsed YAML dict into a prompt string for the LLM."""
    task = cfg.get("task")

    if task == "summarize":
        return f"""Summarize the following text.

Audience: {cfg.get("audience", "general")}
Tone: {cfg.get("tone", "neutral")}

Text:
{cfg.get("text", "")}

Write a clear summary in 2-4 sentences."""

    raise ValueError(f"Unknown task: {task!r}. Supported: summarize")
