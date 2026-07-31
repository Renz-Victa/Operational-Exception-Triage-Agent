from pydantic import BaseModel, EmailStr
from datetime import date

class Customer(BaseModel):
  id: int
  name: str
  email: EmailStr
  date: date

def validate_action(data):
  if not isinstance(data, dict):
    return False 

  if "action" not in data:
    return False

  if "query" not in data:
    return False

  return True

def main():
  Customer(BaseModel)
  validate_action()

if __name__ == "__main__":
  main()