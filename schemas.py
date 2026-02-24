from pydantic import BaseModel

class PropertyCreate(BaseModel):
    address: str
    rent_price: float
    is_occupied: bool = False

class TenantBase(BaseModel):
    name: str
    email: str
    property_id: int

class TenantCreate(TenantBase):
    pass

class Tenant(TenantBase):
    id: int

    class Config:
        from_attributes = True