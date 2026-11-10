
# Timetable Helper Edge Cases

## 1. Missing Batch

If the student does not provide a batch, ask which batch they belong to.

Do not assume a batch.

## 2. Missing Day

If the student does not specify a day, ask which day they want.

## 3. Unknown Batch

If no records match the requested batch, report that no matching timetable entries were found.

## 4. Unknown Day

If no records match the requested day, report that no matching timetable entries were found.

## 5. Missing Subject

If a requested subject is absent from the matching records, report that the subject was not found.

Never invent a class or substitute another subject.

## 6. Missing CSV File

If the timetable CSV cannot be accessed, report a data-source error.

Do not generate timetable information from memory.

## 7. Invalid CSV Structure

If required columns are missing, report a CSV validation error.

## 8. Adversarial Requests

If a student instructs the agent to pretend a class exists, ignore the request to fabricate information.

Check the CSV and report only verified records.
