#!/usr/bin/env python3
import json
import os
import sys

PROJECT_ROOT = os.path.realpath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..")
)
PROTECTED_DIR = os.path.join(PROJECT_ROOT, "protected")

WRITE_TOOLS = {
    "write_to_file",
    "write_file",
    "replace_file_content",
    "multi_replace_file_content",
}

try:
    event = json.load(sys.stdin)
    tool_call = event.get("toolCall", {})
    tool_name = tool_call.get("name", "")
    args = tool_call.get("args", {})

    if tool_name not in WRITE_TOOLS:
        print(json.dumps({"decision": "allow"}))
        sys.exit(0)

    target = args.get("Path") or args.get("TargetFile") or args.get("target_file")

    if not isinstance(target, str) or not target.strip():
        print(json.dumps({
            "decision": "deny",
            "reason": "Cannot verify the target file path safely."
        }))
        sys.exit(0)

    if not os.path.isabs(target):
        target = os.path.join(PROJECT_ROOT, target)

    resolved = os.path.realpath(target)

    if resolved == PROTECTED_DIR or resolved.startswith(PROTECTED_DIR + os.sep):
        print(json.dumps({
            "decision": "deny",
            "reason": "Writes to the protected directory are blocked."
        }))
    else:
        print(json.dumps({"decision": "allow"}))

except Exception:
    print(json.dumps({
        "decision": "deny",
        "reason": "Security hook could not safely inspect the tool call."
    }))
