# Nimbus Campus Helpdesk MCP Server

Python MCP server using the official MCP Python SDK 1.x over stdio.

## Tools
1. get_timetable(batch, day): Retrieves mock timetable entries.
2. get_fee_status(student_id): Retrieves fictional fee status.

## Resource
campus://hostel/rules: Reads mock hostel rules.

## Run
From the repository root:
source .venv/bin/activate
python mcp-server/server.py

## Inspector
Run: mcp dev mcp-server/server.py

## Verified tests
- get_timetable: Batch A, Monday
- get_fee_status: DEMO001
- hostel rules resource
- JSON-RPC initialize
- JSON-RPC tools/list
- JSON-RPC tools/call

All records are fictional demonstration data.
