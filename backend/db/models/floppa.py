from sqlalchemy.orm import Mapped
from .. import Base


class Purchase(Base):
    __tablename__ = "floppas"

    owner: Mapped[str]
    age: Mapped[int]
    name: Mapped[str]
    desc: Mapped[str]