import asyncio
from agents import Agent, Runner, function_tool
from agents.mcp.server import MCPServerSse
from dotenv import load_dotenv


load_dotenv()


async def main():
    async with MCPServerSse(
        name="DeepWiki MCP Server",
        params={"url": "https://mcp.deepwiki.com/sse"},
        client_session_timeout_seconds=30,
    ) as mcp_server:
        agent = Agent(
            name="DeepWiki Agent",
            model="gpt-4.1-mini",
            instructions="Use the tools to answer the questions.",
            mcp_servers=[mcp_server],
        )

        prompt = """Take a look at deepwiki and figure out
                    what transport protocols are supported in the latest version of MCP spec
                    using modelcontextprotocol/python-sdk repo"""

        response = await Runner.run(agent, prompt)
        print(response.final_output)


asyncio.run(main())
