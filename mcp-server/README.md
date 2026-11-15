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

## Validation and error handling

The server validates the requested weekday and checks that the batch exists
in the mock timetable data before returning results.

Direct Python functional checks performed:

- Valid batch and weekday: returns matching timetable records.
- Unknown batch: returns `{"error": "Unknown batch"}`.
- Invalid weekday: returns `{"error": "Invalid weekday"}`.
- Known mock student ID: returns the mock fee-status record.
- Unknown student ID: returns `{"error": "Student ID not found"}`.
- Hostel rules resource: returns the mock hostel-rules text.

These checks call the server functions directly. They are not a substitute
for MCP Inspector or raw JSON-RPC protocol tests.
