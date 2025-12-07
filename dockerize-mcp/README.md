# Dockerize & Deploy MCP Server

This guide walks you through building, publishing, and deploying your MCP Server using Docker, GitHub Container Registry (GHCR), and Render.

---

## 1. Build the Docker Image Locally

```bash
docker build -t simple-mcp-server .
```

This creates a local Docker image named simple-mcp-server.

---

## 2. Run the Docker Container Locally (Optional Test)

```bash
docker run simple-mcp-server
```

Use this to verify everything is working before deploying.

---

## 3. Generate a GitHub Container Registry (GHCR) Token

Go to:
https://github.com/settings/tokens/new

Enable these permissions:

- write:packages
- delete:packages

Click Generate token  
Copy and save the token (you will not see it again)

---

## 4. Login to GHCR via Docker

```bash
docker login ghcr.io
```

When prompted:

- Username: `<github-username>`
- Password: `<your-generated-token>`

---

## 5. Build an amd64 Image for Production

```bash
docker buildx build --platform linux/amd64 -t simple-mcp-server -t ghcr.io/<github-username-in-lowercase>/<package-name> . --load
```

Example:
`docker buildx build --platform linux/amd64 -t simple-mcp-server -t ghcr.io/royalboss-ayush/simple-mcp-server . --load`

---

## 6. Push the Image to GitHub Container Registry

```bash
docker push ghcr.io/<github-username-in-lowercase>/<package-name>
```

Example:
`docker push ghcr.io/royalboss-ayush/simple-mcp-server`

---

## 7. Make the Package Public (Required for Deployment)

Open:
https://github.com/users/`<github-username>`/packages/container/`<package-name>`/settings

Example:
`https://github.com/users/RoyalBosS-Ayush/packages/container/simple-mcp-server/settings`

Change Visibility → Public  
Copy the Docker Pull Command URL

---

## 8. Deploy on Render

Login:
https://render.com

Create a new Web Service:
https://dashboard.render.com/web/new

Select:

- Existing Image
- Paste the Docker Pull Command URL

Click:

- Connect
- Choose a Pricing Plan
- Deploy Web Service

Copy the Public URL after deployment

Example:
`https://simple-mcp-server-latest.onrender.com`

---

## 9. Test with MCP Inspector

Start the Inspector:

```bash
npx @modelcontextprotocol/inspector@latest
```

Set:

- Transport Type: Streamable HTTP
- URL: `<render-public-url>`/mcp

Example:
`https://simple-mcp-server-latest.onrender.com/mcp`

Final Step:
Click Connect

---

MCP Server is now fully deployed and ready to use!
