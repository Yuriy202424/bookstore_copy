from typing import Optional
from pydantic import BaseModel, ConfigDict


class PurchaseData(BaseModel):
    model_config = ConfigDict(from_attributes=True) #помолись на дядюшку
    id: Optional[int] = None
    owner: str
    age: int
    name: str
    desc: str



class SeePurchases(BaseModel):
    email: str