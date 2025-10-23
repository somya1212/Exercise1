# LLM Code Generation: Prompting, Debugging, Innovation

**Models (two families):**
- Family A: GPT (ChatGPT)
- Family B: ______ (Claude OR Gemini)  ← fill this once chosen

**Structure**
- `prompts/` — exact prompts used (markdown files)
- `generated_code/` — model outputs (organized by family)
- `tests/` — unit tests for each of the 10 problems
- `eval/` — simple evaluation scripts (runs tests, computes pass@k=1)
- `results/` — CSV logs of runs

**Pass@k policy**: Using pass@1 (single attempt) for baseline; we’ll extend later if time allows.
