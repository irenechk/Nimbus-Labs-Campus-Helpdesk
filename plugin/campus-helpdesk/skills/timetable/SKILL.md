---
name: timetable
description: Use when a student explicitly invokes /timetable to look up campus class schedules, batch timetables, lecture timings, subjects, faculty, or classrooms using the bundled timetable-helper Skill and its supplied CSV data.
---

# Timetable Command

This Skill provides the `/timetable` entry point for the campus-helpdesk plugin.

## Instructions

1. Treat the request as a timetable lookup.
2. Follow the bundled `timetable-helper` Skill instructions.
3. Use only the bundled timetable CSV as the source of truth.
4. Run the bundled helper script using the appropriate batch, day, or subject filters.
5. Ask for missing information when necessary.
6. Report matching records accurately.
7. Never invent a class, subject, faculty member, time, or room.
8. Do not answer fee, hostel, or unrelated administrative questions through this command.

## Bundled helper

The detailed instructions are in `../timetable-helper/SKILL.md`.

The helper script is:

`../timetable-helper/scripts/timetable_lookup.py`

Examples:

- `/timetable Batch A Monday`
- `/timetable Data Structures`
- `/timetable Batch A Wednesday`

If the request is ambiguous, ask the student for clarification before running the lookup.