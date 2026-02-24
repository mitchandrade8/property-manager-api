from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from database import Base

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    rent_price = Column(Float)
    is_occupied = Column(Boolean, default=False)
    
    # Financials
    mortgage = Column(Float, default=0.0)
    loan_balance = Column(Float, default=0.0)

    # --- THE NEW PRO FIELDS ---
    property_type = Column(String, default="Single Family")
    beds = Column(Integer, default=0)
    baths = Column(Float, default=0.0)
    purchase_price = Column(Float, default=0.0)
    land_value = Column(Float, default=0.0)
    interest_rate = Column(Float, default=0.0)
    lease_end = Column(Date, nullable=True)

    tenants = relationship("Tenant", back_populates="property")

class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    
    property_id = Column(Integer, ForeignKey("properties.id"))

    property = relationship("Property", back_populates="tenants")