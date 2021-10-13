from typing import List
import os
import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from starlette.responses import RedirectResponse
import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.get("/records/", response_model=List[schemas.Record])
def show_records(db: Session = Depends(get_db)):
    query_str = text("select * " 
                   "from states " 
                   "where entity_id = 'sensor.downstairs_temperature' " 
                   "ORDER BY created DESC LIMIT 1")
    records = db.query(models.Record).from_statement(query_str).all()
    return records

if __name__ == '__main__':
    uvicorn.run(app, port=os.environ['PORT'], host='0.0.0.0')