from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from database import Base

class Property(Base):
    __tablename__ = "properties"
    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    rent_price = Column(Float)
    is_occupied = Column(Boolean, default=False)
    
    # Add these two new lines!
    mortgage = Column(Float, default=0.0)
    loan_balance = Column(Float, default=0.0)
    
    tenants = relationship("Tenant", back_populates="property")

class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    
    property_id = Column(Integer, ForeignKey("properties.id"))

    property = relationship("Property", back_populates="tenants")