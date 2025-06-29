from sqlalchemy import select, and_
from main import app
from db import Session, Floppa
from schemas import (PurchaseData,
                     SeePurchases
)


@app.get("/default")
def get_floppas(data: SeePurchases):
    with Session.begin() as session:
        purchases = session.scalars(select(Floppa)).all()
        purchases = [PurchaseData.model_validate(floppa) for floppa in purchases]
        return purchases
    


@app.post('/create')
def create_floppa(data: PurchaseData):
    with Session.begin() as session:
        floppa = Floppa(**data.model_dump())
        session.add(floppa)
        return floppa
    

@app.get("/floppa/{floppa_id}")
def get_floppa(floppa_id, data: SeePurchases):
    with Session.begin() as session:
        floppa = session.scalar(select(Floppa).where(and_(Floppa.id == floppa_id, Floppa.owner == data.email)))
        if floppa:
                floppa = Floppa.model_validate(floppa)
                return floppa
        else:
             return "Error"