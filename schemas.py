from pydantic import BaseModel

class PropertyCreate(BaseModel):
    address: str
    rent_price: float
    is_occupied: bool = False