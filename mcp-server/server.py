import csv
import json
from pathlib import Path
from mcp.server.fastmcp import FastMCP

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"

mcp = FastMCP("nimbus-campus-helpdesk")

@mcp.tool()
def get_timetable(batch: str, day: str) -> dict:
    """Get scheduled classes for a batch on a weekday from the mock timetable."""
    if day.title() not in {
        "Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"
    }:
        return {"error": "Invalid weekday"}
    with (DATA / "timetable.csv").open(newline="") as f:
        rows = list(csv.DictReader(f))
    matches = [
        row for row in rows
        if row["batch"].casefold() == batch.casefold()
        and row["day"].casefold() == day.title().casefold()
    ]
    return {"batch": batch, "day": day.title(), "classes": matches}

@mcp.tool()
def get_fee_status(student_id: str) -> dict:
    """Get mock fee status for a student ID. Uses fictional demonstration records."""
    records = json.loads((DATA / "fees.json").read_text())
    return records.get(student_id, {"error": "Student ID not found"})

@mcp.resource("campus://hostel/rules")
def hostel_rules() -> str:
    """Read the mock campus hostel rules."""
    return (DATA / "hostel-rules.md").read_text()

if __name__ == "__main__":
    mcp.run(transport="stdio")
