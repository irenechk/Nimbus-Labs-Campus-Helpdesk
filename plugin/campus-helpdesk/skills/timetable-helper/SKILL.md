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
- On which days does Batch A have Data Structures?
- Find all classes for Data Structures.

## 3. When Not to Use This Skill

Do not activate this Skill for:

- Fee payment or fee status enquiries.
- Hostel rules and accommodation questions.
- Attendance calculations.
- General academic advice unrelated to scheduled classes.

These queries require other helpdesk capabilities.

## 4. Workflow

1. Identify the student's timetable search request.
2. Determine which search filters are available: batch, day, and subject.
3. Ask for clarification when essential information is missing to answer the request accurately.
4. Read `references/csv-dictionary.md` if clarification about the CSV structure is needed.
5. Use `scripts/timetable_lookup.py` with the appropriate command-line arguments, or use its interactive mode.
6. Check the returned records before preparing the answer.
7. Present the subject, time, faculty, batch, day and classroom as relevant to the question.
8. If no matching record exists, inform the student that no timetable entry was found.
9. Consult `references/edge-cases.md` when an unusual input or missing record occurs.
10. Consult `references/lookup-guide.md` for detailed search and presentation instructions when needed.

## 5. Important Rules

- Treat the CSV as the only authoritative timetable source.
- Never invent a subject, lecture, faculty member, time or classroom.
- Never assume a missing timetable entry means a cancelled class.
- Do not change the batch, day or subject without confirmation.
- Accept case differences in batch, day and subject names.
- Do not expose information from unrelated records.
- Report missing or invalid information honestly.
- Use fictional timetable data only.

## 6. Examples

User: Show me Batch A's Monday timetable.

Action: Retrieve Batch A records for Monday and present all matching classes.

User: Where is Operating Systems on Monday for Batch A?

Action: Search the matching batch and day records, then return the classroom exactly as recorded.

User: Find Data Structures for Batch A.

Action: Search for the exact subject and batch, then present all matching records.

User: Show Batch C's Monday timetable.

Action: Report that no matching timetable entries were found. Do not create a timetable.

User: What is my fee balance?

Action: Do not use this Skill because the question concerns fee information.

## 7. Edge Cases

- Missing batch or day for a batch-and-day request: Ask the student for the missing information.
- Unknown batch: Report that no matching entries were found.
- Unknown day: Report the validation error or no matching entries, as appropriate.
- Unknown subject: Report that no matching entries were found.
- No matching class: Never invent a substitute class.
- Missing CSV: Report a data-source error rather than guessing.
- Invalid CSV structure: Report the validation error.
- Ambiguous request: Ask a clarifying question rather than assuming the intended search.

## 8. References

Read these files only when their details are required:

- `references/csv-dictionary.md` — CSV columns and data definitions.
- `references/edge-cases.md` — Input validation and exceptional situations.
- `references/lookup-guide.md` — Instructions for timetable searches, subject lookups, and presenting results.

## 9. Script

The timetable lookup script is located at:

`scripts/timetable_lookup.py`

The script supports interactive searches and command-line filters.

Examples:

Batch and day:

`python3 scripts/timetable_lookup.py --batch A --day Monday`

Subject:

`python3 scripts/timetable_lookup.py --subject "Data Structures"`

Subject and batch:

`python3 scripts/timetable_lookup.py --subject "Data Structures" --batch A`

Subject, batch and day:

`python3 scripts/timetable_lookup.py --subject "Data Structures" --batch A --day Wednesday`

If no command-line arguments are supplied, the script prompts the user for a batch and day.

Use the script to retrieve actual records rather than generating timetable information from memory. Check its output before responding to the student.