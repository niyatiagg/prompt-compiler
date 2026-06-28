# PromptOps — Declarative Prompt Compiler

A declarative prompt compilation system that converts YAML task specifications into structured LLM prompts and executes them against a local language model.

## Overview

PromptOps separates task intent from prompt authoring. Users define requirements in YAML; the compiler generates the prompt and returns the model response.

```
YAML specification → Schema parsing → Prompt compilation → LLM inference → Response
```

## Tech Stack

- **Python** — application runtime
- **PyYAML** — YAML parsing
- **Pydantic-compatible OpenAI SDK** — LLM client
- **Ollama** — local model inference
- **python-dotenv** — environment configuration

## Prerequisites

- Python 3.10 or later
- [Ollama](https://ollama.com) installed and running locally

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd prompt-compiler
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install openai pyyaml python-dotenv
```

4. Install Ollama and download a model:

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2:1b
```

## Configuration

Create a `.env` file in the project root:

```env
OLLAMA_BASE_URL=http://localhost:11434/v1
OLLAMA_MODEL=llama3.2:1b
```

## Usage

1. Define a task specification in a YAML file (see `sample.yaml`).
2. Run the compiler:

```bash
source venv/bin/activate
python main.py
```

The program prints the parsed specification, compiled prompt, and model response.

## Input Specification

Example task definition:

```yaml
task: summarize

audience: engineers

tone: concise

text: |
  Kubernetes is an open-source container orchestration platform.
  It automates deployment, scaling, and management of containerized applications.
```

## Project Structure

| File | Description |
|------|-------------|
| `main.py` | Entry point: parses YAML, invokes the compiler, calls the LLM |
| `prompts.py` | Prompt compiler: maps task types to prompt templates |
| `sample.yaml` | Example task specification |
| `.env` | Local configuration (not committed) |

## Architecture

1. **Parse** — Load the YAML specification into a structured dictionary.
2. **Compile** — Select the task handler and generate the final prompt.
3. **Execute** — Send the prompt to Ollama via its OpenAI-compatible API.
4. **Output** — Return the generated response.

## Supported Tasks

| Task | Description |
|------|-------------|
| `summarize` | Summarize input text for a given audience and tone |

Additional task types (code review, interview questions, structured JSON output) are planned as part of the workflow engine expansion.
