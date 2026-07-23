from pydantic import BaseModel, EmailStr
from datetime import date

class Customer(BaseModel):
  id: int
  name: str
  email: EmailStr