import yaml
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from main import run_spec

app = FastAPI(title="PromptOps", description="Declarative prompt compiler API")


class GenerateRequest(BaseModel):
    yaml_spec: str


@app.get("/")
def health():
    return {"status": "ok"}


@app.post("/generate")
def generate(req: GenerateRequest):
    try:
        config = yaml.safe_load(req.yaml_spec)
    except yaml.YAMLError as e:
        raise HTTPException(status_code=400, detail=f"Invalid YAML: {e}")

    if not isinstance(config, dict):
        raise HTTPException(status_code=400, detail="YAML must be a mapping of fields")

    try:
        result = run_spec(config)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {
        "task": config.get("task"),
        "prompt": result["prompt"],
        "response": result["response"],
    }
