from pydantic import BaseModel, EmailStr
from datetime import date

class Customer(BaseModel):
  id: int
  name: str
  email: EmailStr
  date: date

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

def main():
  Customer(BaseModel)
  validate_action()

if __name__ == "__main__":
  main()