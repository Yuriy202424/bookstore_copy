from sqlalchemy.orm import Mapped
from .. import Base


class Floppa(Base):
    __tablename__ = "floppas"

    owner: Mapped[str]
    age: Mapped[int]
    name: Mapped[str]
    desc: Mapped[str]