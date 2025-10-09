# Connecting Local/Remote MCP with Claude or Cursor

Claude Desktop and Cursor allow you to connect **MCP (Model Context Protocol) servers** via configuration files.  
You can run both **remote MCP servers** (via URL) and **local MCP servers** (via Node.js or Python scripts).

⚠️ **Note:** The **free versions** of Claude Desktop and Cursor **do not support direct remote MCP connections**.  
To work around this, we use the **[`mcp-remote`](https://www.npmjs.com/package/mcp-remote) NPM package**, which acts as a **proxy** to your remote MCP server.

---

## Configuration Snippet

Add the following to your configuration file:

```json
{
  "mcpServers": {
    "remote-mcp": {
      "command": "npx",
      "args": ["mcp-remote", "<server-url>"]
    },
    "local-mcp": {
      "command": "<node/python-path>",
      "args": ["<mcp-server-file-path>"]
    }
  }
}
```

- Replace `<server-url>` with the remote MCP endpoint (e.g., `https://example.com/mcp`).
- Replace `<node/python-path>` with your local runtime path (`node`, `python`, or `python3`).
- Replace `<mcp-server-file-path>` with the local MCP server script path.

---

## File Path to Edit Config File

- **Claude Desktop (macOS / Linux / Windows):**  
  `~/Library/Application\ Support/Claude/claude_desktop_config.json`  
  (On Linux it may be under `~/.config/Claude/claude_desktop_config.json`)

- **Cursor IDE:**  
  `~/.cursor/mcp.json`

---

## GUI Steps to Edit Config File

### Claude Desktop

1. Open **Claude Desktop**.
2. Go to **Settings → Developer Settings**.
3. Look for the **MCP Servers** section.
4. Click **Edit Config** – this will open the `claude_desktop_config.json` file.
5. Paste the above JSON snippet (merge with existing config).
6. Save and restart Claude.

### Cursor

1. Open **Cursor IDE**.
2. Go to **Settings → MCP Servers** (sometimes under **Experimental / Developer Tools**).
3. Click **Edit Config** – this will open `~/.cursor/mcp.json`.
4. Add the MCP server configuration as shown above.
5. Save and restart Cursor.

---

✅ You are now connected to your **local/remote MCP server** in Claude or Cursor (with `mcp-remote` acting as a proxy for free versions).
