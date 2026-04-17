from sqlalchemy import Column, Integer, String, Float
from api.dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotions"

    promo_id = Column(Integer, primary_key=True, index=True)
    promo_code = Column(String(50), nullable=False, unique=True)
    expiration_date = Column(String(50), nullable=False)
    discount_amount = Column(Float, nullable=False)