import asyncio
from pathlib import Path
from dotenv import load_dotenv

from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.sessions import Connection
from langchain_openai import ChatOpenAI

from langgraph.prebuilt import create_react_agent

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

ROOT_FOLDER = Path(__file__).parent.parent.absolute()
MCP_PATH = str(ROOT_FOLDER / "mcp_example/mcp_server.py")
MCP_NAME = "MY MCP"


mcp_config: dict[str, Connection] = {
    "MY MCP": {
        "command": "python",
        "args": [MCP_PATH],
        "transport": "stdio",
    }
}


async def main():
    client = MultiServerMCPClient(mcp_config)
    async with client.session("MY MCP") as session:
        tools = await client.get_tools()
        agent = create_react_agent(model, tools)

        query = "What are the current prices of Bitcoin and Ethereum?"
        message = HumanMessage(content=query)

        response = await agent.ainvoke({"messages": [message]})
        answer = response["messages"][-1].content
        return answer


if __name__ == "__main__":
    response = asyncio.run(main())
    print(response)
