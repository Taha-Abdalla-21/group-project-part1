from sqlalchemy import Column, Integer, String, ForeignKey
from api.dependencies.database import Base


class Review(Base):
    __tablename__ = "reviews"

    review_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    menu_item_id = Column(Integer, ForeignKey("menu_items.menu_item_id"), nullable=False)
    rating = Column(Integer, nullable=False)
    review_text = Column(String(255), nullable=True)
    review_date = Column(String(50), nullable=False)