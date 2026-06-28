import os

import yaml
from dotenv import load_dotenv
from openai import OpenAI

from prompts import generate_prompt

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")


def main():
    with open("sample.yaml") as f:
        config = yaml.safe_load(f)

    print("=== Parsed YAML ===")
    print(config)
    print()

    prompt = generate_prompt(config)

    print("=== Compiled prompt ===")
    print(prompt)
    print()

    client = OpenAI(
        base_url=OLLAMA_BASE_URL,
        api_key="ollama",
    )
    response = client.chat.completions.create(
        model=OLLAMA_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )

    answer = response.choices[0].message.content

    print("=== LLM response ===")
    print(answer)


if __name__ == "__main__":
    main()
