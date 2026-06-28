# PromptOps — Declarative Prompt Compiler

A YAML-driven prompt compiler that turns declarative task specifications into LLM prompts and runs them against a local Ollama model.

```
YAML spec  →  parse  →  compile prompt  →  Ollama  →  response
```

## Tech Stack

Python, PyYAML, python-dotenv, OpenAI SDK (Ollama-compatible API), Ollama

## Project Structure

```
prompt-compiler/
├── main.py           # CLI entry point — parse YAML, compile, call LLM
├── prompts.py        # Prompt compiler — task registry and templates
├── sample.yaml       # Example: summarize task
├── .env              # Ollama config (not committed)
└── venv/             # Python virtual environment
```

## Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com) installed and running

## Setup

```bash
cd prompt-compiler
python3 -m venv venv
source venv/bin/activate
pip install openai pyyaml python-dotenv
```

Install and start Ollama, then pull a model:

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2:1b
```

Create `.env`:

```
OLLAMA_BASE_URL=http://localhost:11434/v1
OLLAMA_MODEL=llama3.2:1b
```

### Ollama on CPU (GPU driver issues)

If you see `CUDA error: device kernel image is invalid`, force CPU mode:

```bash
sudo mkdir -p /etc/systemd/system/ollama.service.d
sudo tee /etc/systemd/system/ollama.service.d/override.conf << 'EOF'
[Service]
Environment="CUDA_VISIBLE_DEVICES="
Environment="OLLAMA_LLM_LIBRARY=cpu_avx2"
EOF
sudo systemctl daemon-reload
sudo systemctl restart ollama
```

CPU inference is slower (~5–10s per request) but works fine for development.

## Usage

```bash
source venv/bin/activate
python main.py
```

By default this reads `sample.yaml`. Expected output:

1. Parsed YAML dict
2. Compiled prompt string
3. LLM response

## Example YAML

### Summarize

```yaml
task: summarize

audience: engineers

tone: concise

text: |
  Kubernetes is an open-source container orchestration platform.
  It automates deployment, scaling, and management of containerized applications.
```

## How It Works

1. **Parse** — `yaml.safe_load()` reads the YAML file into a Python dict.
2. **Compile** — `generate_prompt()` in `prompts.py` maps `task` to a prompt template.
3. **Execute** — `main.py` sends the compiled prompt to Ollama via the OpenAI-compatible API.
4. **Respond** — The model output is printed to the terminal.

## Roadmap

| Stage | Status | Description |
|-------|--------|-------------|
| 1 | Done | YAML → prompt → Ollama |
| 2 | Planned | Multiple tasks (`code_review`, `interview_question`) |
| 3 | Planned | FastAPI REST API |
| 4 | Planned | Pydantic schema validation |
| 5 | Planned | Jinja2 prompt templates |
| 6 | Planned | Prompt compression + token/quality metrics |

## Resume

**Title:** PromptOps — Declarative Prompt Compiler

**Bullet:** Built a YAML-driven prompt compiler that validates task specs, generates templated LLM prompts, and returns structured responses via a FastAPI service.
