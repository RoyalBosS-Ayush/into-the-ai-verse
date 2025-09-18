from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import asyncio
from pydantic import AnyUrl

MCP_FILE = str(Path(__file__).parent / "mcp_server.py")

server_params = StdioServerParameters(
    command="python",
    args=[MCP_FILE],
    env=None,
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()

            tool_result = await session.call_tool(
                "get_crypto_price", arguments={"symbol": "BTCUSDT"}
            )
            print("TOOL RESULT:", tool_result)

            resource_result = await session.read_resource(
                AnyUrl("file://user_data.json")
            )
            print("RESOURCE RESULT:", resource_result)

            prompt_result = await session.get_prompt("quick_crypto_summary")
            print("PROMPT RESULT:", prompt_result)


if __name__ == "__main__":
    asyncio.run(run())
