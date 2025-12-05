# %%
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# %%
prompt = """Take a look at deepwiki and figure out
            what transport protocols are supported in the latest version of MCP spec
            using modelcontextprotocol/python-sdk repo"""

resp = client.responses.create(
    model="gpt-4o-mini",
    tools=[
        {
            "type": "mcp",
            "server_label": "deepwiki",
            "server_url": "https://mcp.deepwiki.com/mcp",
            "require_approval": "never",  # <-
        }
    ],
    input=prompt,
)

print(resp.model_dump_json(indent=2))
print(resp.output_text)

# %%
prompt = """Take a look at deepwiki and figure out
            what transport protocols are supported in the latest version of MCP spec
            using modelcontextprotocol/python-sdk repo"""

resp = client.responses.create(
    model="gpt-4o-mini",
    tools=[
        {
            "type": "mcp",
            "server_label": "deepwiki",
            "server_url": "https://mcp.deepwiki.com/mcp",
            "require_approval": "never",  # <-
            "allowed_tools": ["ask_question"],  # <-
        }
    ],
    input=prompt,
)

# print(resp.model_dump_json(indent=2))
print(resp.output_text)

# %%
