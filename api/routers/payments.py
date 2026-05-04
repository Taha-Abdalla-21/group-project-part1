from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..controllers import payments as controller
from ..schemas import payments as schema
from ..dependencies.database import get_db

router = APIRouter(prefix="/payments", tags=["Payments"])

@router.post("/", response_model=schema.Payment, status_code=status.HTTP_201_CREATED)
def create(request: schema.PaymentCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=list[schema.Payment])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=schema.Payment)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id)

@router.put("/{item_id}", response_model=schema.Payment)
def update(item_id: int, request: schema.PaymentCreate, db: Session = Depends(get_db)):
    return controller.update(db, item_id, request)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, item_id)