from sqlalchemy import Column, Integer, String, ForeignKey
from api.dependencies.database import Base


class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("customer_orders.order_id"), nullable=False)
    payment_type = Column(String(50), nullable=False)
    card_info = Column(String(100), nullable=True)
    transaction_status = Column(String(50), nullable=False)
    payment_date = Column(String(50), nullable=False)