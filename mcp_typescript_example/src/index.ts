#!/usr/bin/env node

import {
  McpServer,
  ResourceTemplate,
} from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import fs from "fs";
import path from "path";

const { version: VERSION } = require("../package.json");

const MCP_NAME = "MY MCP";
const USER_DATA_FILE = path.join(__dirname, "../src/user_data.json");
const ACTIVITY_LOG_FILE = path.join(__dirname, "../log/activity.log");

const server = new McpServer({
  name: MCP_NAME,
  version: VERSION,
});

server.tool(
  "get_crypto_price",
  {
    description: "Get cryptocurrency price",
    inputSchema: {
      type: "object",
      properties: {
        symbol: { type: "string" },
      },
      required: ["symbol"],
    },
  },
  async (params) => {
    const symbol = params.symbol?.toUpperCase();

    if (!symbol) {
      throw new Error("Symbol parameter is required");
    }
    const url = `https://api.binance.com/api/v3/ticker/price?symbol=${symbol}`;

    const response = await fetch(url);
    if (!response.ok) {
      const errorText = await response.text();
      fs.appendFileSync(
        ACTIVITY_LOG_FILE,
        `Error getting price for ${symbol}: ${response.status} ${errorText}\n`
      );
      throw new Error(
        `Error getting price for ${symbol}: ${response.status} ${errorText}`
      );
    }

    const data = (await response.json()) as any;
    const price = data.price;

    fs.appendFileSync(
      ACTIVITY_LOG_FILE,
      `Successfully got price for ${symbol}. Current price is ${price}. Current time is ${new Date().toISOString()}\n`
    );
    return {
      content: [
        {
          type: "text",
          text: `The current price of ${symbol} is ${price}`,
        },
      ],
    };
  }
);

server.resource(
  "get_user_data",
  `file://${USER_DATA_FILE}`,
  async (uri: any) => {
    const data = fs.readFileSync(uri, "utf-8");
    return {
      contents: [
        {
          uri: uri,
          mimeType: "application/json",
          text: data,
        },
      ],
    };
  }
);

server.prompt("quick_crypto_summary", async (args) => {
  return {
    messages: [
      {
        role: "user",
        content: {
          type: "text",
          text: "Get current price of my favourite crypto currency",
        },
      },
    ],
  };
});

const main = async () => {
  if (!fs.existsSync(ACTIVITY_LOG_FILE)) {
    fs.writeFileSync(ACTIVITY_LOG_FILE, "");
  }

  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error(`${MCP_NAME} Server v${VERSION} started`);
};

main().catch((err) => {
  console.error("Error starting server:", err);
  process.exit(1);
});
