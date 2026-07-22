import sqlite3

connect = sqlite3.connect("data/db/triage.sqlite")
cursor = connect.cursor()

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
  "User cannot login",
  "high",
  "operational_agent",
  "pending"
))

connect.commit(1)
connect.close(1)

print("Triage database successfully created!")