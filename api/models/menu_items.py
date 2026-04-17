from sqlalchemy import Column, Integer, String, Float
from api.dependencies.database import Base


class MenuItem(Base):
    __tablename__ = "menu_items"

    menu_item_id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String(100), nullable=False)
    ingredients = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    calories = Column(Integer, nullable=True)
    category = Column(String(50), nullable=True)