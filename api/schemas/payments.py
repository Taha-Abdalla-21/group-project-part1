from pydantic import BaseModel
from typing import Optional


class PaymentBase(BaseModel):
    order_id: int
    payment_type: str
    card_info: Optional[str] = None
    transaction_status: str
    payment_date: str


class PaymentCreate(PaymentBase):
    pass


class Payment(PaymentBase):
    payment_id: int

    class Config:
        from_attributes = True