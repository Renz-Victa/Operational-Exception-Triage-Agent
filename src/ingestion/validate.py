from pydantic import BaseModel, EmailStr
from datetime import date

class Customer(BaseModel):
  id: int
  name: str
  email: EmailStr
  date: date

def main():
  Customer(BaseModel)

__name__ = "__main__":
main()