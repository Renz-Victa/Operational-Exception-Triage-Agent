import json
from pydantic import BaseModel, EmailStr, ConfigDict, ValidationError
from datetime import date
from pathlib import Path
from datetime import datetime, timezone

class Customer(BaseModel):
  model_config = ConfigDict(extra="forbid")
  id: int
  name: str
  email: EmailStr
  date: date

QUARANTINE_DIR = Path("data/quarantine")
QUARANTINE_DIR.mkdir(parents=True, exist_ok=True)

def validate_action(data):
  required = ["action", "query", "confidence"]
  if not isinstance(data, dict):
      return False 
  if not 0 <= data["confidence"] <= 1:
    return False
  for key in required:
    if key not in data:
      return False 
  
  return True

def validate_rows(rows: list[dict]) -> list[Customer]:
  valid_rows = []
  for row_number, row in enumerate(rows, start=1):
    try: 
      user = Customer.model_validate(row)
      valid_rows.append(Customer)

    except ValidationError as exc:
      quarantine_row(
        row_number=row_number,
        row=row,
        error=exc,
      )

  return valid_rows, user

def quarantine_row(
    row_number: int,
    row: dict,
    error: ValidationError
) -> None:
  timestamp = datetime.now(timezone.utc).isoformat()

  quarantine_record = {
    "timestampt": timestamp,
    "row_number": row_number,
    "reason": "schema_validation_failed",
    "errors": error.errors(),
    "row": row,
  }

  filename = QUARANTINE_DIR / f"row{row_number}.json"

  filename.write_text(
    json.dumps(quarantine_record, indent=2, default=str),
    encoding="utf-8",
  )

  print(
    f"{QUARANTINE} row={row_number} "
    f"reason=schema_validation_failed "
    f"details={error.errors()}"
  )

def main():
  Customer(BaseModel)
  validate_action()

if __name__ == "__main__":
  valid_users = validate_rows(rows)
  print(f"Valid rows: {len(valid_users)}")
  main()