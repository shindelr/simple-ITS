"""
DB control for the product table
"""

from sqlmodel import Session, select
from fastapi import HTTPException
from model.models import Product

PROD_NOT_FOUND = 'Product not found'

# Create a product
def create_product(new_product: Product, session: Session) -> Product:
    """Create a new product."""
    session.add(new_product)
    session.commit()
    session.refresh(new_product)
    return new_product

# Read all products
def get_all_products(session: Session) -> list[Product]:
    """List all products in the table"""
    prods = session.exec(select(Product)).all()
    if not prods:
        raise HTTPException(404, 'No products found')
    return prods

# Read a specific product
def get_a_product_by_id(product_id: int, session: Session) -> Product:
    """Find a specific product in the DB."""
    prod = session.get(Product, product_id)
    if not prod:
        raise HTTPException(404, PROD_NOT_FOUND)
    return prod

# Update a product
def update_a_product(product_id: int, session: Session) -> Product:
    """Update the specifics on a single product."""
    db_prod = get_a_product_by_id(product_id, session)
    data = db_prod.model_dump(exclude_unset=True)
    db_prod.sqlmodel_update(data)
    session.add(db_prod)
    session.commit()
    session.refresh(db_prod)
    return db_prod

# Delete a product
def delete_a_product(product: Product, session: Session) -> Product:
    """Delete a product."""
    db_prod = get_a_product(product, session)
    if not db_prod:
        raise HTTPException(404, PROD_NOT_FOUND)
    session.delete(db_prod)
    session.commit()
    return {'200 OK': 'Product deleted'}
