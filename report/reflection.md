# Part F — Reflection

Building the campus helpdesk toolchain showed me that an agent workflow is not reliable just because a prompt produces a convincing answer. Each component needs a separate way to be checked. The timetable Skill needed trigger and no-trigger tests, the helper script needed input validation, and the MCP server needed protocol-level inspection and failure tests. Using mock records also made it possible to test the workflow without exposing real student information.

The most important lesson came from the protected-folder hook. My first live test allowed a file to be created in the protected directory. That result contradicted my initial expectation that the hook was already blocking the operation. I investigated the actual tool-call event, corrected the hook to recognise the observed `write_file` event and its argument fields, and tested the revised logic directly with a simulated event. The direct test returned a deny decision. However, I cannot claim that the live runtime was fully protected end to end without a successful live retest. This distinction between a unit test and an integration test is important.

I also learned to verify commands and package claims rather than trusting plausible suggestions. The proposed `@nimbus/mcp-skill-bridge` version could not be retrieved from npm and returned an E404 response. The marketplace-link attempt also failed because the CLI did not recognise the proposed marketplace name. I recorded these limitations instead of presenting them as successful installations.

Git worktrees made parallel development easier because each branch had its own working directory while sharing repository history. The deliberate merge conflict demonstrated why changes still need review and explicit resolution.

If I extended this project, I would add automated regression tests for Skill routing, hook integration tests using the actual runtime, stronger schema validation, and continuous checks for dependencies and plugin configuration. I would also improve evidence capture so every important claim is linked to a reproducible command, output, or screenshot. Overall, the project taught me to treat verification, honest reporting, and least privilege as essential parts of agent engineering.

## Choosing a Skill or an MCP Tool

I would choose a Skill when the task needs conversational guidance,
domain-specific instructions, progressive disclosure, or clarification
of incomplete user requests. For example, the timetable Skill can ask
which batch or day a student means before performing a lookup. I would
choose an MCP tool when the agent needs a defined, repeatable operation
against structured data, such as retrieving timetable records or
checking a fictional fee status. A Skill guides the agent's behaviour;
an MCP tool exposes a structured capability that the agent can call.
