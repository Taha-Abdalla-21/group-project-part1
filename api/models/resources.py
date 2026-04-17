from sqlalchemy import Column, Integer, String, Float
from api.dependencies.database import Base


class Resource(Base):
    __tablename__ = "resources"

    resource_id = Column(Integer, primary_key=True, index=True)
    resource_name = Column(String(100), nullable=False)
    amount = Column(Float, nullable=False)
    unit = Column(String(50), nullable=False)