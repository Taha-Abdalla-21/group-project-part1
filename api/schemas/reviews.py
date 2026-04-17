from pydantic import BaseModel
from typing import Optional


class ReviewBase(BaseModel):
    customer_id: int
    menu_item_id: int
    rating: int
    review_text: Optional[str] = None
    review_date: str


class ReviewCreate(ReviewBase):
    pass


class Review(ReviewBase):
    review_id: int

    class Config:
        from_attributes = True