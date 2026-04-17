from pydantic import BaseModel
from typing import Optional


class CustomerBase(BaseModel):
    full_name: str
    email: Optional[str] = None
    phone: str
    address: str


class CustomerCreate(CustomerBase):
    pass


class Customer(CustomerBase):
    customer_id: int

    class Config:
        from_attributes = True