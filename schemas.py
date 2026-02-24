from datetime import date
from typing import Optional
from pydantic import BaseModel

class PropertyCreate(BaseModel):
    address: str
    rent_price: float
    mortgage: float = 0.0      # New
    loan_balance: float = 0.0  # New
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