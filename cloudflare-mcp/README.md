# 🚀 Deploy MCP Server on Cloudflare (No Authentication Required)

## 1. Generate the Boilerplate Code

Use Cloudflare’s project generator to scaffold a new MCP server:

```sh
npm create cloudflare@latest -- cloudflare-mcp --template=cloudflare/ai/demos/remote-mcp-authless
```

---

## 2. Add MCP Tools, Resources, or Prompts

Open the project’s entry point and customize your server:

```
src/index.ts
```

This is where you define tools, resources, or prompts your MCP server exposes.

---

## 🧪 3. Test Locally

### Start the MCP server

```sh
npm start
```

### Test with the MCP Inspector

```sh
npx @modelcontextprotocol/inspector@latest
```

#### In the inspector:

- **Transport Type:** `Streamable HTTP`
- **URL:** `http://localhost:8787/mcp`

---

## 4. Log In with Wrangler (Required for Deployment)

```sh
npx wrangler login
```

---

## 5. Deploy to Cloudflare

```sh
npx wrangler deploy
```

After deployment, you'll receive a public Worker URL.

---

## 🔍 6. Test the Deployed Worker with MCP Inspector

In the inspector:

- **Transport Type:** `Streamable HTTP`
- **URL:** `<your-worker-url>/mcp`

**Example:**

```
https://cloudflare-mcp.n8n-testacc.workers.dev/mcp
```

---
