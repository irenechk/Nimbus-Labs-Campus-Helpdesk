# Campus Helpdesk Plugin — Threat Model

## 1. Prompt injection
**Threat:** A student message or timetable data may contain instructions designed to override the Skill's rules or invent timetable entries.

**Mitigations:** Treat student messages and CSV rows as untrusted data, never as system instructions. The Skill uses the timetable dataset as the source of truth and should not invent missing classes. An adversarial test supplied a fabricated Friday Machine Learning class; the agent refused to present it as a real entry.

**Residual risk:** Model behaviour is not a security boundary. Important decisions must be checked against validated data and deterministic code.

## 2. Malicious hooks
**Threat:** A hook runs code with the permissions of the local user. A malicious or modified hook could read files, alter data, or expose secrets.

**Mitigations:** Inspect hook source before installation, keep its scope narrow, resolve paths before checking protected locations, and test both denied and allowed operations. The protected-folder hook was tested directly with a simulated `write_file` event and returned a deny decision. A previous live agent write succeeded before the hook was corrected; therefore, complete end-to-end blocking in the live Antigravity runtime is not claimed.

**Residual risk:** Hook event formats and runtime loading behaviour can change. Re-test after changing or reinstalling the plugin.

## 3. MCP tool poisoning
**Threat:** A malicious server or misleading tool description could induce an agent to call tools with unsafe arguments or treat tool output as trusted instructions.

**Mitigations:** Use a locally reviewed server, expose only the two required tools (`get_timetable` and `get_fee_status`), validate inputs, return mock data, and expose hostel rules as a read-only resource. Do not put credentials or real student records in the server. Treat all tool results as data, not instructions.

**Residual risk:** A compromised server can still return misleading data. Verify server code and tool schemas before connecting it.

## 4. General safeguards
- Use mock student identifiers and synthetic records only.
- Do not store API keys, passwords, or personal student information in the repository.
- Review plugin manifests, hooks, MCP configuration, and dependencies before installation.
- Keep tool permissions and filesystem access to the minimum required.
