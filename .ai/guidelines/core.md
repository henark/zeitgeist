# Core AI Guidelines for TimeKeeper Boost

You are an AI agent interacting with the TimeKeeper Boost MCP server. Your goal is to assist with development tasks within this environment.

## Available Tools

- **filesystem**: `read`, `list`, `write`
- **uploader**: `upload_file`, `upload_blockchain_data`, etc.
- **connector**: `get_latest_block`
- **documentation**: `search`

## General Principles

1.  **Safety First**: All file system operations are restricted to the project directory. Do not attempt to access files outside of this scope.
2.  **Clarity**: Be clear and explicit in the commands you issue. Provide all necessary arguments for each tool action.
3.  **Efficiency**: Use the available tools to gather information before making changes. Read existing code before writing new code.
4.  **Documentation**: When adding new features, also add or update the relevant documentation using the `filesystem` tool.
