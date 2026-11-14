# Part A — CTO Briefing Claim Audit

**Audit date:** 15 November 2026  
**Method:** Checked protocol, platform, standards, and Git documentation. “Unverified” means I could not establish the claim from a reliable source; it does not prove the claim is impossible.

## Ten-claim audit

### 1. MCP uses JSON-RPC 2.0 and defines Tools, Resources, and Prompts
**Verdict: TRUE**

MCP's protocol data layer uses JSON-RPC 2.0. Its core server features include tools, resources, and prompts, with different control semantics: tools are invoked by the model, resources are read by the application, and prompts are user-selected templates.

**Correction:** No correction required. Note that protocol revisions evolve, so implementations should identify and negotiate a supported protocol version.

**Source:** https://modelcontextprotocol.io/  
**Accessed:** 15 November 2026.

### 2. MCP revision 2025-02-30 introduced a mandatory Persistent Memory Primitive
**Verdict: FALSE**

The date 2025-02-30 is invalid because February 2025 did not have a 30th day. The official MCP feature model documents tools, resources, and prompts; it does not establish a mandatory core feature called “Persistent Memory Primitive.”

**Correction:** Cite a valid, published MCP specification revision and identify features using the official specification terminology. Do not present persistent memory as a mandatory MCP primitive.

**Sources:** https://modelcontextprotocol.io/specification/  
https://modelcontextprotocol.io/  
**Accessed:** 15 November 2026.

### 3. Skills use a SKILL.md file with YAML metadata and progressive disclosure
**Verdict: TRUE**

The Agent Skills format uses a `SKILL.md` file with YAML frontmatter, including a name and description. Skills can keep detailed instructions, scripts, and references in supporting files so that additional material is loaded when needed rather than placing every detail in the initial description.

**Correction:** No correction required. Follow the target platform's required folder structure and supported metadata fields.

**Sources:** https://agentskills.io/specification  
https://antigravity.google/docs/build-plugins/  
**Accessed:** 15 November 2026.

### 4. Every Skill requires skill.config.yaml and a Python runtime declaration
**Verdict: FALSE**

The documented Skill format uses `SKILL.md` and YAML frontmatter; it does not require a separate `skill.config.yaml` file or a Python runtime declaration for every Skill. Scripts may be included when a Skill needs them, but that does not make Python mandatory.

**Correction:** Provide the required `SKILL.md` metadata and only declare or document runtime prerequisites that the implementation actually needs.

**Sources:** https://agentskills.io/specification  
https://antigravity.google/docs/build-plugins/  
**Accessed:** 15 November 2026.

### 5. Git worktrees use separate working directories while sharing repository objects
**Verdict: TRUE**

A linked worktree provides another working directory associated with the same repository, allowing multiple branches to be checked out concurrently. The worktrees share the repository's common object database and most references, while worktree-specific state such as `HEAD` is kept separately.

**Correction:** No correction required. Remember that a branch is normally checked out in only one worktree at a time.

**Source:** https://git-scm.com/docs/git-worktree  
**Accessed:** 15 November 2026.

### 6. `git worktree sync --all` pulls or rebases every worktree
**Verdict: FALSE**

The documented `git worktree` command set includes operations such as `add`, `list`, `remove`, `prune`, `repair`, `lock`, and `unlock`. `sync` is not a command that pulls or rebases all worktrees. Worktrees share repository history; synchronising with a remote still requires normal fetch and integration operations.

**Correction:** Use `git fetch` to update remote-tracking references, then integrate the required branch in the relevant worktree using merge, rebase, or another deliberate workflow. Use `git worktree prune` to clean stale worktree metadata, not to update branches.

**Source:** https://git-scm.com/docs/git-worktree  
**Accessed:** 15 November 2026.

### 7. Antigravity plugins can bundle commands, subagents, Skills, hooks, and MCP configurations
**Verdict: TRUE, WITH QUALIFICATION**

Antigravity plugin documentation describes bundles containing Skills, custom agents or subagents, lifecycle hooks, and MCP server configurations. Skills can be invoked through slash commands, but the documented plugin component layout does not define a separate top-level `commands/` component.

**Correction:** Describe slash-command functionality as Skill invocation. Do not claim that a standalone commands directory is a supported native plugin component unless the platform documentation confirms it.

**Source:** https://antigravity.google/docs/build-plugins/  
**Accessed:** 15 November 2026.

### 8. RFC 9999 requires Ed25519 signatures for every stdio MCP server
**Verdict: FALSE**

RFC 9999 is titled “Remote ATtestation procedureS (RATS) Conceptual Message Wrapper (CMW).” It describes formats for wrapping remote-attestation conceptual messages; it does not establish a universal Ed25519-signing requirement for stdio MCP servers.

**Correction:** Do not attribute an MCP server-signing requirement to RFC 9999. Assess MCP transport and server security using the applicable MCP specification and deployment-specific security controls.

**Source:** https://www.rfc-editor.org/rfc/rfc9999.html  
**Accessed:** 15 November 2026.

### 9. Git permits the same branch to be checked out in two worktrees by default
**Verdict: FALSE**

Git normally refuses to check out a branch that is already checked out in another linked worktree. This safeguard prevents two working directories from independently modifying the same branch's checked-out state. Force options can override certain safeguards, but that is not the default behaviour.

**Correction:** Create or use separate branches for concurrent worktrees. Avoid force-checking out one branch in multiple worktrees unless the consequences are understood.

**Source:** https://git-scm.com/docs/git-worktree  
**Accessed:** 15 November 2026.

### 10. A 2024 study proves skill collapse at 12 Skills with a 40% accuracy drop
**Verdict: UNVERIFIED**

I could not identify a reliable, traceable 2024 study establishing this exact threshold and accuracy reduction. Without a paper title, authors, methodology, dataset, and results, the numerical claim cannot be treated as established evidence.

**Correction:** Remove the precise “12 Skills” and “40%” figures unless the original study can be produced and independently checked. Treat any general claim about performance degradation as a hypothesis until supported by reproducible evidence.

**Search location checked:** https://openalex.org/works?search=skill+collapse+agent+accuracy  
**Accessed:** 15 November 2026.

## Source register

| Source | Purpose |
|---|---|
| https://modelcontextprotocol.io/specification/ | MCP protocol and feature terminology |
| https://agentskills.io/specification | Agent Skills file format and metadata |
| https://antigravity.google/docs/build-plugins/ | Antigravity plugin structure and supported components |
| https://git-scm.com/docs/git-worktree | Worktree commands, shared repository state, and branch restrictions |
| https://www.rfc-editor.org/rfc/rfc9999.html | Actual scope of RFC 9999 |
| https://openalex.org/works?search=skill+collapse+agent+accuracy | Search for evidence behind the numerical research claim |

**Audit limitation:** The unverified research claim remains unverified rather than being labelled false. A search result alone is not proof that no such study exists.
