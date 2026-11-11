
---
name: timetable-helper
description: Answers student questions about campus class schedules, lecture timings, subjects, faculty, classrooms, and batch-wise timetables. Use when a student asks to view, check, find, or verify a class timetable or a scheduled lecture. Do not use for fee enquiries, hostel rules, attendance, or general academic questions.
---

# Timetable Helper

## 1. Purpose

Help students retrieve accurate timetable information from the supplied fictional campus timetable CSV.

The source of truth is:

`data/timetable.csv`

The lookup program is:

`scripts/timetable_lookup.py`

## 2. When to Use This Skill

Activate this Skill when the user asks questions such as:

- Show my Monday timetable.
- What classes does Batch A have on Tuesday?
- When is Database Management?
- Which room is assigned to Operating Systems?
- Who teaches Data Structures?

## 3. When Not to Use This Skill

Do not activate this Skill for:

- Fee payment or fee status enquiries.
- Hostel rules and accommodation questions.
- Attendance calculations.
- General academic advice unrelated to scheduled classes.

These queries require other helpdesk capabilities.

## 4. Workflow

1. Identify the requested batch and day.
2. Check whether both values are provided.
3. If either value is missing, ask the student for it.
4. Read `references/csv-dictionary.md` if clarification about the CSV structure is needed.
5. Use `scripts/timetable_lookup.py` to retrieve the requested timetable.
6. Check the returned records before preparing the answer.
7. Present the subject, time, faculty and classroom clearly.
8. If no matching record exists, inform the student that no timetable entry was found.
9. Consult `references/edge-cases.md` when an unusual input or missing record occurs.

## 5. Important Rules

- Treat the CSV as the only authoritative timetable source.
- Never invent a subject, lecture, faculty member, time or classroom.
- Never assume a missing timetable entry means a cancelled class.
- Do not change the batch or day without confirmation.
- Accept case differences in batch and day names.
- Do not expose information from unrelated records.
- Report missing or invalid information honestly.
- Use fictional timetable data only.

## 6. Examples

User: Show me Batch A's Monday timetable.

Action: Retrieve Batch A records for Monday and present all matching classes.

User: Where is Operating Systems on Monday for Batch A?

Action: Check the matching timetable record and return its classroom.

User: Show Batch C's Monday timetable.

Action: Report that no matching timetable entries were found. Do not create a timetable.

User: What is my fee balance?

Action: Do not use this Skill because the question concerns fee information.

## 7. Edge Cases

- Missing batch: Ask the student to provide their batch.
- Missing day: Ask the student to specify a day.
- Unknown batch: Report that no matching entries were found.
- Unknown day: Report that no matching entries were found.
- No matching class: Never invent a substitute class.
- Missing CSV: Report a data-source error rather than guessing.
- Invalid CSV structure: Report the validation error.

## 8. References

Read these files only when their details are required:

- `references/csv-dictionary.md` — CSV columns and data definitions.
- `references/edge-cases.md` — Input validation and exceptional situations.
- `references/lookup-guide.md` — Instructions for timetable searches, subject lookups, and presenting results.

## 9. Script

The timetable lookup script is located at:

`scripts/timetable_lookup.py`

Use the script to retrieve actual records rather than generating timetable information from memory.

The script's execution method and input format must be checked before use. Do not assume it accepts command-line arguments unless its implementation confirms this.
