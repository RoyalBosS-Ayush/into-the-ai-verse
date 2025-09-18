from pathlib import Path
import json
import requests
from mcp.server.fastmcp import FastMCP
from typing import Any

THIS_FILE = Path(__file__).absolute()
THIS_FOLDER = THIS_FILE.parent
USER_DATA_FILE = THIS_FOLDER / "user_data.json"
MCP_NAME = "MY MCP"

mcp = FastMCP(MCP_NAME)


@mcp.tool()
def get_crypto_price(symbol: str) -> float:
    """
    Get the current price of a crypto asset from Binance

    Args:
        symbol (str): The symbol of the crypto asset to get the price of

    Returns:
        Any: The current price of the crypto asset
    """
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    data = response.json()
    return float(data["price"])


@mcp.resource("file://user_data.json")
def get_user_data() -> Any:
    """Returns user data in json format"""
    with open(USER_DATA_FILE, "r") as f:
        return json.load(f)


@mcp.prompt()
def quick_crypto_summary() -> str:
    """Returns a summary of a crypto asset"""
    return "Get current price of my favourite crypto currency"


if __name__ == "__main__":
    print(f"Starting {MCP_NAME}")
    mcp.run(transport="stdio")
