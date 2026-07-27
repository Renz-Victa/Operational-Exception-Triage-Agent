# Operational Exception Triage Agent

An Operational Exception Triage Agent built using Python

---

## Repository Structure

```
Operational Exception Triage Agent/
├── config
├── ├── schemas/
|   |   └── po_status.yaml
|   ├── rules.yaml
|   ├── severity_weights.yaml
|   └── critical_materials.csv
|
├── data/
|   ├── inbound/
|   ├── quarantine/
|   └── db/
|       └── triage.sqlite
|
├── README.md
├── .gitignore
├── .env
├── .env.example
├── src/
|   ├── triage/
|   |   ├── failback_template.py
|   |   ├── llm_client.py
|   |   ├── narrative.py
|   |   ├── rules.py
|   |   └──  severity.py
|   |
|   ├── ingestion/
|   |   ├── watcher.py
|   |   ├── validate.py
|   |   └── loader.py
|   |
|   ├── rooting/
|   |   └── audience.py
|   |
|   ├── output/
|   |   ├── pdf_coo.py
|   |   ├── pdf_director.py
|   |   └── styles.py
|   |
|   └── pipeline.py
| 
├── tests/
|   ├── test_rules.py
|   ├── test_severity.py
|   ├── test_validate.py
|   └── fixtures/
|       └── sample_po_status.csv
|
├── logs/
|   └── run_2026-07-18.log
|
├── reports/
|   ├──  coo_rollup_2026-07-18.pdf
|   └── director_detail_2026-07-18.pdf
|
├── model/
|
├── metadata.json
├── download_model.sh
├── REPORT.md
└── requirements.txt
     
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