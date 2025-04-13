"""
Author: Robin Shindelman
Created: 2025-04-12
A simple inventory tracking system.
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    """Index page"""
    return {'message':'Welcome to Simple ITS'}