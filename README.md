# Operational Exception Triage Agent

An Operational Exception Triage Agent built using Python

---

## Repository Structure

```
Operational Exception Triage Agent/
├── main.py
├── pyproject.toml
├── README.md
├── .gitignore
├── .env
├── .env.example
├── src/
    └── triage_agent/
        ├── __init__.py
        ├── config.py
        | 
        ├── ingestion/
        |   ├── __init__.py
        |   ├── base.py
        |   ├── webhook_source.py
        |   ├── polling_source.py
        |   └── deduplication.py
        |
        ├── classification/
        |   ├── __init__.py
        |   ├── models/
        |   |   ├──  openai_classifier.py
        |   |   └── gemini_classifier.py
        |   ├── multi_llm_compare.py
        |   └── schemas.py
        |
        ├── context/
        |   ├── __init__.py
        |   ├── retriever.py
        |   ├── incident_history.py
        |   └── account_context.py
        |
        ├── decision/
        |   ├── __init__.py
        |   ├── orchestrator.py
        |   ├── escalation_rules.py
        |   └── schemas.py
        |
        ├── guardrails/
        |   ├── __init__.py
        |   ├── kill_switch.py
        |   ├── audit_log.py
        |   └── scope_limits.py
        |
        ├── output/
            ├── __init__.py
            ├── kill_switch.py
            ├── audit_log.py
            └──
         
```

---

## Prerequisites

| Tool     | Version  |
|----------|----------|
| Python   | ≥ 3.10   |
| pip      | Latest   |

---

## Quick Start

```bash
# 1. Clone Repository
git clone https:///github.com/Renz-Victa/Operational-Exception-Triage-Agent
cd Operational Exception Triage Agent

# 2. Install the dependencies
pip install -r requirements.txt

# 3. Run the Agent
python main.py
```

---

## Configuration

Create an API key in the .env file

```
API_KEY=sk-your_api_key_here
MODEL_NAME=gemini-flash
```

After that, load it in the main.py file before you run the Agent

---

## How it works

- It uses the `python-dotenv` to load your API keys form the `.env` file.
- It uses `argparse` to read the command line options.

## License

This project is licensed under the MIT license.