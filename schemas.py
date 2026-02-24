from datetime import date
from typing import Optional
from pydantic import BaseModel

class PropertyBase(BaseModel):
    address: str
    rent_price: float
    mortgage: float = 0.0
    loan_balance: float = 0.0
    is_occupied: bool = False
    # Use Optional for everything else so old data doesn't break the app
    property_type: Optional[str] = "Single Family"
    beds: Optional[int] = 0
    baths: Optional[float] = 0.0
    purchase_price: Optional[float] = 0.0
    land_value: Optional[float] = 0.0
    interest_rate: Optional[float] = 0.0
    lease_end: Optional[date] = None

class PropertyCreate(PropertyBase):
    """Used for POST requests - incoming data from frontend"""
    pass

class Property(PropertyBase):
    """Used for GET/Response - outgoing data with an ID"""
    id: int

    class Config:
        from_attributes = True
        
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