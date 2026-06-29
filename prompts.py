def summarize_prompt(cfg: dict) -> str:
    return f"""Summarize the following text.

Audience: {cfg.get("audience", "general")}
Tone: {cfg.get("tone", "neutral")}

Text:
{cfg.get("text", "")}

Write a clear summary in 2-4 sentences."""


def code_review_prompt(cfg: dict) -> str:
    return f"""You are a senior {cfg.get("language", "python")} engineer.

Review the following code.

Goals:
{chr(10).join(f"- {goal}" for goal in cfg.get("goals", ["find bugs", "suggest improvements"]))}

Code:
{cfg.get("code", "")}

Provide:
1. Issues found
2. Suggested fixes
3. A short overall assessment"""


def interview_question_prompt(cfg: dict) -> str:
    focus = cfg.get("focus", [])
    focus_lines = "\n".join(f"- {item}" for item in focus) if focus else "- general topics"

    return f"""You are a senior {cfg.get("domain", "software engineering")} interviewer.

Generate one {cfg.get("difficulty", "mid-level")} interview question.

Requirements:
{chr(10).join(f"- {req}" for req in cfg.get("requirements", ["include follow-up questions"]))}

Focus areas:
{focus_lines}

Output format:
1. Question
2. Follow-up questions
3. What a strong answer should cover"""


TASKS = {
    "summarize": summarize_prompt,
    "code_review": code_review_prompt,
    "interview_question": interview_question_prompt,
}


def generate_prompt(cfg: dict) -> str:
    """Turn a parsed YAML dict into a prompt string for the LLM."""
    task = cfg.get("task")
    if task not in TASKS:
        supported = ", ".join(sorted(TASKS))
        raise ValueError(f"Unknown task: {task!r}. Supported: {supported}")

    return TASKS[task](cfg)
