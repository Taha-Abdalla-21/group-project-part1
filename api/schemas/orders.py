from pydantic import BaseModel
from typing import Optional


class OrderBase(BaseModel):
    customer_id: int
    order_date: str
    tracking_number: str
    order_status: str
    order_type: str
    total_price: float
    promo_id: Optional[int] = None


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_id: Optional[int] = None
    order_date: Optional[str] = None
    tracking_number: Optional[str] = None
    order_status: Optional[str] = None
    order_type: Optional[str] = None
    total_price: Optional[float] = None
    promo_id: Optional[int] = None


class Order(OrderBase):
    order_id: int

    class Config:
        from_attributes = True