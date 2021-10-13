from datetime import datetime
from pydantic import BaseModel


class Record(BaseModel):
    state_id: int
    entity_id: str
    state: str
    created: datetime

    class Config:
        orm_mode = True