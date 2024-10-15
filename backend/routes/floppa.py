from sqlalchemy import select, and_
from main import app
from db import Session, Floppa
from schemas import (FloppaData,
                     SeeFlopps
)


@app.get("/default")
def get_floppas(data: SeeFlopps):
    with Session.begin() as session:
        floppas = session.scalars(select(Floppa).where(Floppa.owner == data.email))
        floppas = [FloppaData.model_validate(floppa) for floppa in floppas]
        return floppas
    


@app.post('/create')
def create_floppa(data: FloppaData):
    with Session.begin() as session:
        floppa = Floppa(**data.model_dump())
        session.add(floppa)
        return floppa
    

@app.get("/floppa/{floppa_id}")
def get_floppa(floppa_id, data: SeeFlopps):
    with Session.begin() as session:
        floppa = session.scalar(select(Floppa).where(and_(Floppa.id == floppa_id, Floppa.owner == data.email)))
        if floppa:
                floppa = Floppa.model_validate(floppa)
                return floppa
        else:
             return "Error"