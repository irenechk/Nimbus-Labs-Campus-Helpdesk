# MCP Server Test Results

Test method: Direct invocation of the registered Python server functions.
Date: 15 November 2026
Data: Fictional demonstration records only.

| Test | Input | Observed result | Status |
|---|---|---|---|
| Valid timetable | Batch A, Monday | Two classes returned | PASS |
| Second valid batch | Batch B, Monday | One class returned | PASS |
| Unknown batch | UNKNOWN, Monday | Unknown batch error | PASS |
| Invalid weekday | Batch A, Funday | Invalid weekday error | PASS |
| Valid fee ID | DEMO001 | Partially paid; INR 12,500 outstanding | PASS |
| Unknown fee ID | UNKNOWN999 | Student ID not found error | PASS |
| Hostel resource | campus://hostel/rules | Mock hostel rules returned | PASS |

Note: These are direct Python function tests. They do not replace MCP Inspector
or raw JSON-RPC protocol evidence.
