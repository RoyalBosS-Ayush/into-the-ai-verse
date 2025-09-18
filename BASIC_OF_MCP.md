# MCP (Model Context Protocol)

## Key Points

1. **Problem**: LLMs are isolated, creating NxM integration challenge
2. **Solution**: MCP is a universal, open standard for connecting AI to tools
3. **How**: A simple client-server architecture with tools, resources and prompts
4. **Why it matters**: It enables a secure and rapidly growing ecosystem

## NxM Problem

1. **N Models x N Tools**: An endless number of possible connections
2. **Redundant work**: Rebuilding the same integrations for different models
3. **Hight Maintenance**: API updates break multiple brittle connections
4. **Fragmented Experience**: Inconsistent behaviour across tools

## Core MCP Architecture

1. **Host**: The AI powered application where users interact (eg. IDEs, chatbots)
2. **MCP Client**: A module in the host that manages connections with servers
3. **MCP Server**: A wrapper around an external tool or data source (eg. GitHub server)
4. **Transport Layer**: The cable (HTTP or STDIO) connection client and server

## Server Capabilities

1. **Tools**: Callable functions the AI can execute (eg. create_ticket)
2. **Resources**: Readable data the AI can access (eg. a file)
3. **Prompts**: Reusable prompt templates for consistent outputs (eg. ticket summary)

## Intent To Action

1. **User Prompt**: User gives a prompt to the AI Host Application
2. **Tool Proposal**: The AI Analyses the intent and proposes a tool call
3. **Mediate**: The MCP Client and Server handle the request securely
4. **Execute Action**: The MCP Server executes the action on the enterprise system
5. **Get Result**: A structured result is returned to the MCP Client
6. **Final Answer**: The AI uses the result to generate the final answer

## Design Practice

1. **Specific Naming**: Use clear, unambiguous names for tools and parameters
2. **Schema**: Use strict types and formats. Clearly define required vs optional fields
3. **Versioning**: Adopt semantic versioning to ensure stability as tool evolves
4. **Deprecation**: Establish clear deprecation windows to avoid breaking changes
5. **Documentation**: Create doc directly from schemas to ensure it’s always up-to-date

## Design Checklist

1. **One clear intent**: Each tool should do one thing and do it well
2. **Idempotent**: Running a tool multiple times has the same effect
3. **Bound Inputs**: Limit the scope of what a tool can accept
4. **Clear Description**: Provide examples in the tool’s description

## Security

1. **Least Privilege**: Define granular scopes for every tool
2. **Input Validation**: Enforce strict schemas to prevent malicious requests
3. **Output Sanitisation**: Automatically redact PII (Personally Identifiable Information) and sensitive data
4. **Robust Authentication**: Use API keys or OAuth for secure connections

## Reliability

1. **Reliability**: Built in timeouts, retries with backoff and fallbacks
2. **Structured Errors**: Clear error codes tell the AI if an action is retry-able
3. **Graceful Degradation**: Return a cached value if a live system is down
4. **Observability**: Track metrics like latency and error rates per tool
5. **Audit Logs**: End-to-end tracking with correlation IDs for compliance

### **AI’s role (The Thinker)**: Analyses intent and proposes a plan of which tools to use

### **MCP Server’s Role (The Doer)**: Securely executes the action and enforces permissions
