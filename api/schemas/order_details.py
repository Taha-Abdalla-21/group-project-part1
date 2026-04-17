from pydantic import BaseModel
from typing import Optional


class OrderDetailBase(BaseModel):
    order_id: int
    menu_item_id: int
    quantity: int
    item_price: float


class OrderDetailCreate(OrderDetailBase):
    pass


class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    menu_item_id: Optional[int] = None
    quantity: Optional[int] = None
    item_price: Optional[float] = None


class OrderDetail(OrderDetailBase):
    order_detail_id: int

    class Config:
        from_attributes = True