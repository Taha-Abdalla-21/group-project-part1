from pydantic import BaseModel
from typing import Optional


class MenuItemBase(BaseModel):
    item_name: str
    ingredients: str
    price: float
    calories: Optional[int] = None
    category: Optional[str] = None


class MenuItemCreate(MenuItemBase):
    pass


class MenuItem(MenuItemBase):
    menu_item_id: int

    class Config:
        from_attributes = True