from pydantic import BaseModel


class ResourceBase(BaseModel):
    resource_name: str
    amount: float
    unit: str


class ResourceCreate(ResourceBase):
    pass


class Resource(ResourceBase):
    resource_id: int

    class Config:
        from_attributes = True