import sqlite3

def database():
  conn = sqlite3.connect("data/db/triage.sqlite")
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

  conn.commit(1)
  conn.close(1)

print("Triage database successfully created!")

def validate_row(row):
  errors = []

  if not isinstance(row.get("value"), int):
    errors.append("value must be numeric")

  return {
    **row,
    "status": "valid" if not errors else "invalid",
    "error": "; ".join(errors) if errors else None 
  }

def insert_validated_rows(rows):
  cursor = conn.cursor()
  conn = sqlite3.connect("data/db/triage.sqlite")
  validated = [validate_row(row) for row in rows]

  cursor.executemany("""
    INSERT INTO validated_rows
    (name, value, status, error)
    VALUES (?, ?, ?, ?  )
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
  database()
  validate_row()
  insert_validated_rows()

if __name__ == "__main__":
  main()