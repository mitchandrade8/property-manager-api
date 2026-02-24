from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List
from database import engine, SessionLocal
import models, schemas

# Initialize the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get a database session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- ROUTES ---

# 1. Dashboard Landing (Serves your index.html)
@app.get("/")
def read_root():
    return FileResponse("index.html")

# 2. Health Check (Helps Render monitor your app)
@app.get("/health")
def health_check():
    return {"status": "Property Manager is Online"}

# 3. CREATE: Add a new property with professional metrics
@app.post("/properties", response_model=schemas.Property)
def create_property(property: schemas.PropertyCreate, db: Session = Depends(get_db)):
    db_property = models.Property(
        address=property.address,
        rent_price=property.rent_price,
        mortgage=property.mortgage,
        loan_balance=property.loan_balance,
        is_occupied=property.is_occupied,
        # PRO FIELDS FOR NEBULASREALESTATE LLC
        property_type=property.property_type,
        beds=property.beds,
        baths=property.baths,
        purchase_price=property.purchase_price,
        land_value=property.land_value,
        interest_rate=property.interest_rate,
        lease_end=property.lease_end
    )
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property

# 4. READ: Get all properties for the dashboard
@app.get("/properties", response_model=List[schemas.Property])
def get_properties(db: Session = Depends(get_db)):
    return db.query(models.Property).all()

# 5. UPDATE: Change occupancy status
@app.put("/properties/{property_id}")
def update_property(property_id: int, is_occupied: bool, db: Session = Depends(get_db)):
    db_prop = db.query(models.Property).filter(models.Property.id == property_id).first()
    if not db_prop:
        raise HTTPException(status_code=404, detail="Property not found")
    db_prop.is_occupied = is_occupied
    db.commit()
    return {"status": "updated"}

# 6. DELETE: Remove a property
@app.delete("/properties/{property_id}")
def delete_property(property_id: int, db: Session = Depends(get_db)):
    db_prop = db.query(models.Property).filter(models.Property.id == property_id).first()
    if not db_prop:
        raise HTTPException(status_code=404, detail="Property not found")
    db.delete(db_prop)
    db.commit()
    return {"status": "deleted"}

# 7. CREATE: Add a tenant and auto-occupy property
@app.post("/tenants")
def create_tenant(tenant: schemas.TenantCreate, db: Session = Depends(get_db)):
    db_tenant = models.Tenant(
        name=tenant.name,
        email=tenant.email,
        property_id=tenant.property_id
    )
    db.add(db_tenant)
    
    # Auto-mark property as occupied
    db_prop = db.query(models.Property).filter(models.Property.id == tenant.property_id).first()
    if db_prop:
        db_prop.is_occupied = True
        
    db.commit()
    db.refresh(db_tenant)
    return db_tenant

# 8. READ: Get all tenants
@app.get("/tenants")
def get_tenants(db: Session = Depends(get_db)):
    return db.query(models.Tenant).all()