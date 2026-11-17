# Nimbus Labs — Campus Helpdesk Agent

**Building and Auditing an AI-Agent Toolchain | Assignment 8**

A modular AI-powered campus helpdesk prototype developed using Agent Skills, a plugin architecture, Model Context Protocol (MCP), and Git worktrees.

---

## 1. Project Overview

The **Nimbus Campus Helpdesk Agent** is a prototype designed to assist students with common campus-related enquiries through structured AI-agent tools.

The project demonstrates how an AI-agent toolchain can be designed, integrated, tested, and audited using multiple components:

- **Agent Skills** for task-specific instructions and timetable assistance.
- **Plugin architecture** for packaging Skills, hooks, and MCP configuration.
- **Model Context Protocol (MCP)** for exposing structured tools and resources.
- **Git Worktrees** for parallel development and branch management.
- **Security hooks** for controlling potentially unsafe file operations.

The project uses fictional demonstration data and does not connect to a live university database.

## 2. Project Objectives

The main objectives are:

1. Build a timetable-helper Skill using the Agent Skills format.
2. Develop a campus-helpdesk plugin containing the Skill and security configuration.
3. Implement an MCP server using the official Python SDK.
4. Expose structured tools for timetable and fee-status enquiries.
5. Provide hostel rules through an MCP resource.
6. Test tool behaviour, input validation, and security scenarios.
7. Explore parallel development using Git worktrees.
8. Maintain an audit trail of AI prompts, outputs, and verification decisions.

## 3. System Architecture

The project consists of three primary components.

### A. Timetable Helper Skill

The timetable-helper Skill handles student timetable enquiries.

**Main capabilities:**
- Retrieve timetable information by batch and weekday.
- Search for scheduled subjects.
- Identify faculty and classroom information.
- Handle missing or invalid search criteria.
- Request clarification for ambiguous questions.

### B. Campus Helpdesk Plugin

The plugin packages the timetable Skill and supporting configuration.

**Components:**
- Plugin manifest (`plugin.json`)
- Bundled Skill
- PreToolUse security hook
- MCP server configuration (`mcp_config.json`)

The security hook checks file-writing operations against a protected directory.

### C. MCP Server

The MCP server provides structured access to mock campus information.

It exposes two tools and one resource:

| Type | Name | Purpose |
|---|---|---|
| Tool | `get_timetable` | Retrieves timetable entries by batch and day |
| Tool | `get_fee_status` | Retrieves mock student fee information |
| Resource | `campus://hostel/rules` | Provides hostel rules |

The server uses the stdio transport.

## 4. Repository Structure

```text
campus-helpdesk-agent/
│
├── skill/
│   └── timetable-helper/
│       ├── SKILL.md
│       ├── data/
│       │   └── timetable.csv
│       ├── references/
│       └── scripts/
│           └── timetable_lookup.py
│
├── plugin/
│   └── campus-helpdesk/
│       ├── plugin.json
│       ├── skills/
│       ├── hooks.json
│       ├── hooks/
│       │   └── protect-folder.py
│       └── mcp_config.json
│
├── mcp-server/
│   ├── server.py
│   └── data/
│       ├── timetable.csv
│       ├── fees.json
│       └── hostel-rules.md
│
├── evidence/
│   ├── plugin/
│   ├── mcp/
│   └── worktrees/
│
├── report/
│   ├── claim-audit.md
│   ├── prompt-log.md
│   ├── reflection.md
│   ├── threat-model.md
│   └── 150096725146_Irene Koner_Assignment8.pdf
│
├── .gitignore
└── README.md
```

*Note: The structure represents the intended project organisation. Refer to the actual repository for the complete file inventory.*

## 5. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Helper scripts and MCP server implementation |
| Agent Skills | Task-specific agent instructions |
| Google Antigravity | Agent and plugin development environment |
| Model Context Protocol | Structured tool and resource communication |
| MCP Python SDK | MCP server implementation |
| MCP Inspector | Server testing and protocol inspection |
| Git | Version control |
| Git Worktrees | Parallel branch development |
| JSON / CSV / Markdown | Configuration and demonstration data |

## 6. Installation and Setup

### Prerequisites

- macOS or a compatible operating system
- Python
- Git
- Google Antigravity CLI
- MCP Python SDK
- MCP Inspector development tooling

### Clone the repository

```bash
git clone https://github.com/irenechk/Nimbus-Labs-Campus-Helpdesk.git
```

Navigate to the project:

```bash
cd Nimbus-Labs-Campus-Helpdesk
```

### Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install the MCP SDK if it is not already installed:

```bash
python -m pip install "mcp[cli]"
```

## 7. Running the MCP Server

From the repository root, activate the virtual environment:

```bash
source .venv/bin/activate
```

Start the server:

```bash
python mcp-server/server.py
```

The server communicates using standard input/output (stdio).

### Running MCP Inspector

To inspect and test the MCP server, run:

```bash
mcp dev mcp-server/server.py
```

The Inspector can be used to examine server initialisation, available tools, tool calls, and resource access.

## 8. MCP Tools and Resource

### Tool 1: get_timetable

**Purpose:** Retrieves timetable records using a batch identifier and weekday.

Inputs:
- `batch`
- `day`

Example conceptual request:

```json
{
  "batch": "A",
  "day": "Monday"
}
```

### Tool 2: get_fee_status

**Purpose:** Retrieves mock fee-status information.

Input:
- `student_id`

Example conceptual request:

```json
{
  "student_id": "DEMO001"
}
```

### Resource: Hostel Rules

**Resource URI:**

```text
campus://hostel/rules
```

This resource provides the demonstration hostel rules stored in the project data directory.

## 9. Testing and Validation

Testing was conducted across the Skill, plugin, MCP server, and Git workflow.

### Skill Testing
- Timetable requests for different batches and weekdays.
- Subject-based searches.
- Combined batch, day, and subject filters.
- Unknown-subject handling.
- Ambiguous timetable requests.
- Adversarial prompt testing against fabricated timetable information.

### Plugin Testing
- Plugin manifest validation.
- Security hook logic testing.
- Protected-path and allowed-path scenarios.
- Local plugin installation and lifecycle checks.

### MCP Testing
- Server initialisation.
- Tool discovery.
- Timetable retrieval.
- Fee-status lookup.
- Invalid input handling.
- Hostel rules resource access.
- JSON-RPC protocol inspection.

### Git Worktree Testing
- Creation of separate development worktrees.
- Branch checkout restriction.
- Merge conflict demonstration.
- Conflict resolution and commit history inspection.

Test results and supporting evidence are maintained in the repository.

## 10. Security Considerations

Security was considered throughout the development process.

Key areas include:

- **Prompt injection:** Treating trusted timetable data as the source of truth.
- **Protected file operations:** Checking write operations against a protected directory.
- **Path traversal:** Testing whether attempts to access protected paths are rejected.
- **MCP tool security:** Reviewing tool inputs, schemas, and returned information.
- **Data privacy:** Using fictional demonstration records instead of real student information.

**Security limitation:** Synthetic hook tests passed for representative protected, allowed, and traversal scenarios. However, end-to-end live enforcement after the hook revision was not conclusively established. The hook should not be considered a verified production security boundary.

## 11. Known Limitations

This project is an academic prototype rather than a production campus information system.

Current limitations include:

- Timetable and fee information is based on mock data.
- No live university database integration is implemented.
- The plugin marketplace registration attempt was unsuccessful.
- Live protected-path blocking after the hook revision remains unconfirmed.
- The demonstrated Git conflict was an add/add conflict rather than a same-line edit conflict.
- Additional verified incorrect or unverifiable AI-output examples are needed to satisfy the full prompt-log requirement.

These limitations are documented to distinguish tested functionality from incomplete or unverified behaviour.

## 12. Project Documentation and Evidence

The `report/` directory contains the written assignment documentation:

- `claim-audit.md` — Technical claim verification.
- `prompt-log.md` — AI prompts, outputs, and verification decisions.
- `reflection.md` — Project reflection and learning outcomes.
- `threat-model.md` — Security risks and mitigations.
- `150096725146_Irene Koner_Assignment8.pdf` — Assignment report.

The `evidence/` directory contains supporting screenshots, protocol exports, and development evidence.

## 13. Future Improvements

Potential future improvements include:

- Integration with an authenticated university information system.
- Stronger end-to-end security enforcement.
- Expanded automated tests for Skills and MCP tools.
- Improved plugin marketplace integration.
- More comprehensive prompt-injection and tool-poisoning evaluations.
- Enhanced error handling and structured logging.

## 14. Author

**Student:** Irene Koner  
**Student ID:** 150096725146  
**Project:** Nimbus Labs — Campus Helpdesk Agent  
**Assignment:** Assignment 8 — Building and Auditing an AI-Agent Toolchain


*Developed as an individual academic project demonstrating the design, implementation, testing, and auditing of an AI-agent toolchain.*