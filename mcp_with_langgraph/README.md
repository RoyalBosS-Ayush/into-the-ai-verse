# MCP Example with Langraph + Langsmith

This project demonstrates how to connect an **MCP (Model Context Protocol) server** with **Langraph** and use **Langsmith** for debugging and tracing.

---

## Prerequisites

Before running this project:

- You must set up the project at:
  ```
  PROJECT_DIR/mcp_example/
  ```
- Make sure your environment has **Python 3.10+** and **uv** installed.
- Update the provided `.env` file with your API keys and rename it to `.env`.

### Configure Secrets

1. Open the `.env` file in this project.
2. Fill in your API keys:
   - **OpenAI API Key** → from [https://platform.openai.com](https://platform.openai.com)
   - **Langsmith API Key** → from [https://smith.langchain.com](https://smith.langchain.com)
3. Save the file.

---

## Setup

```bash
uv sync
```

---

## Run

Activate the virtual environment (if not already):

```bash
source .venv/bin/activate
```

Then run the project:

```bash
python main.py
```

---

✅ You’re now ready to use MCP with **Langraph** (workflow orchestration) and **Langsmith** (debugging & tracing).
