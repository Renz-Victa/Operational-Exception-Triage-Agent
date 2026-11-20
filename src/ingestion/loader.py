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
    value TEXT,
    priority TEXT,
    assigned_agent TEXT,
    status TEXT,
    error TEXT
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

def validate_row(row):
  value = row.get("value")
  errors = []

  if not isinstance(value, (int, float)) or isinstance(value, bool):
    errors.append("Value must be numeric")

  return {
    **row,
    "status": "valid" if not errors else "invalid",
    "error": "; ".join(errors) if errors else None 
  }


def insert_validated_rows(row):
  cursor = conn.cursor()
  validated = [validate_row(row) for row in row]

  cursor.execute("""
      CREATE TABLE IF NOT EXISTS validated_rows(
        id INTEGEER PRIMARY KEY,
        message TEXT,
        value TEXT,
        status TEXT,
        error TEXT 
      )
  """) 

  cursor.executemany("""
    INSERT INTO validated_rows
    (message, value, status, error)
    VALUES (?, ?, ?, ?)
  """, [
    (
      row.get("message"),
      row.get("value"),
      row["status"],
      row["error"]
    )
    for row in validated
  ])

  conn.commit()
  return validated

def main():
  row = read_rows(CSV_PATH)
  tasks()
  insert_validated_rows(row)
  conn.commit()
  conn.close()

if __name__ == "__main__":
  main()