from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime
from database import Base


class Record(Base):
    __tablename__ = "states"

    state_id = Column(Integer, primary_key=True)
    entity_id = Column(String(255), index=True)
    state = Column(String(255))
    created = Column(DateTime)
