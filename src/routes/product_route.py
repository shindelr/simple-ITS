"""
Endpoints and views for the product table. The FastAPI routing decorator is
interesting. The paths are relative to the prefix given at the top.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database.sqlite_db_connect import get_session
from controller import product_control
from model.models import Product
from schemas.product_schema import ProductUpdate

router = APIRouter(prefix='/products', tags=['Products'])

# Create a product

# Get all products
@router.get("/")
async def list_all_products(session: Session = Depends(get_session)):
    """Get all items in the product table"""
    return product_control.get_all_products()

# Get a product
@router.get("/{product_id}")
# Update a product
# Delete a product