from pydantic import BaseModel


class PromotionBase(BaseModel):
    promo_code: str
    expiration_date: str
    discount_amount: float


class PromotionCreate(PromotionBase):
    pass


class Promotion(PromotionBase):
    promo_id: int

    class Config:
        from_attributes = True