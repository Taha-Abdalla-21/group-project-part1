from sqlalchemy import Column, Integer, String, Float, ForeignKey
from api.dependencies.database import Base


class Order(Base):
    __tablename__ = "customer_orders"

    order_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    order_date = Column(String(50), nullable=False)
    tracking_number = Column(String(50), unique=True, nullable=False)
    order_status = Column(String(50), nullable=False)
    order_type = Column(String(50), nullable=False)
    total_price = Column(Float, nullable=False)
    promo_id = Column(Integer, ForeignKey("promotions.promo_id"), nullable=True)