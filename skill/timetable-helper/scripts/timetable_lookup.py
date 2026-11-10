
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


def get_timetable(batch, day):
    """Return timetable entries for the requested batch and day."""

    if not batch or not batch.strip():
        raise ValueError("Batch cannot be empty.")

    if not day or not day.strip():
        raise ValueError("Day cannot be empty.")

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
            if not row.get("batch") or not row.get("day"):
                continue

            if (
                row["batch"].strip().casefold() == batch.strip().casefold()
                and row["day"].strip().casefold() == day.strip().casefold()
            ):
                results.append(row)

    results.sort(key=lambda item: item["start_time"])

    return results


def main():
    print("=== CAMPUS TIMETABLE HELPER ===")

    batch = input("Enter batch (A/B): ").strip()
    day = input("Enter day (Monday-Sunday): ").strip()

    try:
        classes = get_timetable(batch, day)

        if not classes:
            print(f"No timetable entries found for Batch {batch}, {day}.")
            return

        print(f"\nTimetable for Batch {batch.upper()} - {day.title()}\n")

        for item in classes:
            print(f"Subject : {item['subject']}")
            print(
                f"Time    : {item['start_time']} - {item['end_time']}"
            )
            print(f"Faculty : {item['faculty']}")
            print(f"Room    : {item['room']}")
            print("-" * 35)

    except (ValueError, FileNotFoundError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
