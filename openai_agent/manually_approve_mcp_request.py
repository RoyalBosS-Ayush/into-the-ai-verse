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
        }
    ],
    input=prompt,
)

print(resp.model_dump_json(indent=2))

# %%
request_id = str(resp.output[-1].id)

resp = client.responses.create(
    model="gpt-4o-mini",
    tools=[
        {
            "type": "mcp",
            "server_label": "deepwiki",
            "server_url": "https://mcp.deepwiki.com/mcp",
        }
    ],
    previous_response_id=resp.id,
    input=[
        {
            "type": "mcp_approval_response",
            "approve": True,
            "approval_request_id": request_id,
        },
    ],
)
print(resp.model_dump_json(indent=2))

# %%
