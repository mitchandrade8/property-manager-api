from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models, schemas

# Create tables in the SQLite database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# This opens a temporary lane to the database for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1. Serve the actual website HTML file
@app.get("/")
def read_root():
    return FileResponse("index.html")

# 2. CREATE: Add a new property
@app.post("/properties")
def create_property(property: schemas.PropertyCreate, db: Session = Depends(get_db)):
    db_property = models.Property(
        address=property.address,
        rent_price=property.rent_price,
        is_occupied=property.is_occupied
    )
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property

# 3. READ: Get all properties
@app.get("/properties")
def get_properties(db: Session = Depends(get_db)):
    return db.query(models.Property).all()

# 4. UPDATE: Change occupancy status
@app.put("/properties/{property_id}")
def update_property(property_id: int, is_occupied: bool, db: Session = Depends(get_db)):
    db_prop = db.query(models.Property).filter(models.Property.id == property_id).first()
    if db_prop:
        db_prop.is_occupied = is_occupied
        db.commit()
    return {"status": "updated"}

# 5. DELETE: Remove a property
@app.delete("/properties/{property_id}")
def delete_property(property_id: int, db: Session = Depends(get_db)):
    db_prop = db.query(models.Property).filter(models.Property.id == property_id).first()
    if db_prop:
        db.delete(db_prop)
        db.commit()
    return {"status": "deleted"}