import sqlite3
import csv
from pathlib import Path

conn = sqlite3.connect("data/db/triage.sqlite")
CSV_PATH = Path("config/critical_materials.csv")

def read_rows(CSV_PATH):
  with CSV_PATH.open("r", newline="", encoding="utf-8-sig") as file:
    return list(csv.DictReader(file))

def tasks():
  cursor = conn.cursor()

  cursor.execute("""
  CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY,
    message TEXT,
    priority TEXT,
    assigned_agent TEXT,
    status TEXT
  )
  """)

  cursor.execute("""
  INSERT INTO TASKS
  (message, priority, assigned_agent, status)
  VALUES (?, ?, ?, ?)    
  """,
  (
    "User cannot process tasks",
    "high",
    "operational_agent",
    "pending"
  ))

  conn.commit()
  conn.close()

def validate_row(row):
  errors = []

  if not isinstance(row.get("value"), (int, float)):
    errors.append("Value must be numeric")

  return {
    **row,
    "status": "valid" if not errors else "invalid",
    "error": "; ".join(errors) if errors else None 
  }


def insert_validated_rows(row):
  cursor = conn.cursor()
  validated = [validate_row(row) for row in row]

  cursor.executemany("""
    INSERT INTO validated_rows
    (message, value, status, error)
    VALUES (?, ?, ?, ?)
  """, [
    (
      row.get("value"),
      row["status"],
      row["error"]
    )
    for row in validated
  ])

  conn.commit(1)
  return validated

def main():
  row = read_rows(CSV_PATH)
  tasks()
  validate_row(row)
  insert_validated_rows(row)
  conn.commit()
  conn.close()

if __name__ == "__main__":
  main()