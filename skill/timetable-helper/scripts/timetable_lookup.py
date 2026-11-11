
import argparse
import csv
from pathlib import Path


# Locate the timetable CSV relative to this script.
SCRIPT_DIR = Path(__file__).resolve().parent
CSV_FILE = SCRIPT_DIR.parent / "data" / "timetable.csv"

REQUIRED_COLUMNS = {
    "batch",
    "day",
    "start_time",
    "end_time",
    "subject",
    "faculty",
    "room",
}

VALID_DAYS = {
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
}


def get_timetable(batch=None, day=None, subject=None):
    """Return timetable records matching the supplied filters."""

    if not any([batch, day, subject]):
        raise ValueError(
            "Provide at least one search filter: batch, day or subject."
        )

    if batch is not None and not batch.strip():
        raise ValueError("Batch cannot be empty.")

    if day is not None and not day.strip():
        raise ValueError("Day cannot be empty.")

    if day is not None and day.strip().casefold() not in VALID_DAYS:
        raise ValueError(
            "Invalid day. Please enter a valid weekday "
            "(Monday to Sunday)."
        )

    if subject is not None and not subject.strip():
        raise ValueError("Subject cannot be empty.")

    if not CSV_FILE.is_file():
        raise FileNotFoundError(
            f"Timetable CSV not found: {CSV_FILE}"
        )

    results = []

    with CSV_FILE.open(
        mode="r",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError("The CSV file has no header.")

        missing = REQUIRED_COLUMNS - set(reader.fieldnames)

        if missing:
            raise ValueError(
                f"Missing CSV columns: {', '.join(sorted(missing))}"
            )

        for row in reader:
            row_batch = (row.get("batch") or "").strip()
            row_day = (row.get("day") or "").strip()
            row_subject = (row.get("subject") or "").strip()

            if not row_batch or not row_day or not row_subject:
                continue

            if batch is not None:
                if row_batch.casefold() != batch.strip().casefold():
                    continue

            if day is not None:
                if row_day.casefold() != day.strip().casefold():
                    continue

            if subject is not None:
                if row_subject.casefold() != subject.strip().casefold():
                    continue

            results.append(row)

    results.sort(key=lambda item: item["start_time"])

    return results


def display_results(classes, description):
    """Print matching timetable records."""

    if not classes:
        print(f"No timetable entries found for {description}.")
        return

    print(f"\nTimetable results: {description}\n")

    for item in classes:
        print(f"Batch   : {item['batch']}")
        print(f"Day     : {item['day']}")
        print(f"Subject : {item['subject']}")
        print(
            f"Time    : {item['start_time']} - {item['end_time']}"
        )
        print(f"Faculty : {item['faculty']}")
        print(f"Room    : {item['room']}")
        print("-" * 35)


def main():
    parser = argparse.ArgumentParser(
        description="Search the fictional campus timetable."
    )

    parser.add_argument("--batch", help="Batch identifier, e.g. A")
    parser.add_argument("--day", help="Weekday, e.g. Monday")
    parser.add_argument("--subject", help="Exact subject name")

    args = parser.parse_args()

    try:
        # No command-line filters: use interactive mode.
        if not any([args.batch, args.day, args.subject]):
            print("=== CAMPUS TIMETABLE HELPER ===")

            batch = input("Enter batch (A/B): ").strip()
            day = input("Enter day (Monday-Sunday): ").strip()

            classes = get_timetable(batch=batch, day=day)
            description = f"Batch {batch.upper()}, {day.title()}"

        else:
            # Batch and day must be supplied together unless
            # a subject search is also being performed.
            if (args.batch is None) != (args.day is None):
                if args.subject is None:
                    raise ValueError(
                        "Provide both --batch and --day, "
                        "or use --subject for a subject search."
                    )

            classes = get_timetable(
                batch=args.batch,
                day=args.day,
                subject=args.subject
            )

            filters = []

            if args.batch:
                filters.append(f"Batch {args.batch.upper()}")

            if args.day:
                filters.append(args.day.title())

            if args.subject:
                filters.append(f"Subject {args.subject}")

            description = ", ".join(filters)

        display_results(classes, description)

    except (ValueError, FileNotFoundError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
