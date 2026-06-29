import os
import sys
import yaml
from dotenv import load_dotenv
from openai import OpenAI

from prompts import generate_prompt

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")


def run_spec(config: dict) -> dict:
    """Compile a parsed spec and run it against the LLM."""
    prompt = generate_prompt(config)

    client = OpenAI(base_url=OLLAMA_BASE_URL, api_key="ollama")
    response = client.chat.completions.create(
        model=OLLAMA_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    answer = response.choices[0].message.content

    return {"prompt": prompt, "response": answer}

def main():
    yaml_file = sys.argv[1] if len(sys.argv) > 1 else "sample.yaml"

    with open(yaml_file) as f:
        config = yaml.safe_load(f)

    print("=== Parsed YAML ===")
    print(config)
    print()

    result = run_spec(config)

    print("=== Prompt ===")
    print(result["prompt"])

    print("=== LLM response ===")
    print(result["response"])


if __name__ == "__main__":
    main()
