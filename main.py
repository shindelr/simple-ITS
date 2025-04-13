"""
Author: Robin Shindelman
Created: 2025-04-12
A simple inventory tracking system.
"""
from fastapi import FastAPI
from src.database.sqlite_db_connect import create_db_and_tables

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def root():
    """Index page"""
    return {'message':'Welcome to Simple ITS'}