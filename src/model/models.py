"""
DB model for Products table.
"""

from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi import Depends, FastAPI, HTTPException, Query
from datetime import datetime
from decimal import Decimal

class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    upc: str | None = Field(default=None, index=True)
    description: str | None = Field(default=None, index=True)
    dist_code: str | None = Field(default=None, index=True)
    company_id: int = Field(foreign_key="company.id")


class Company(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    phone: str = Field(index=True)
    email: str = Field(index=True)
    street_addr: str = Field(index=True)
    city: str = Field(index=True)
    state: str = Field(index=True)
    country: str = Field(index=True)
    zip: str = Field(index=True)


class Department(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    markup: Decimal = Field(index=True, max_digits=8, decimal_places=4)
    name: str = Field(index=True)


class Order(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    date: datetime = Field(index=True)


class OrderItem(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    retail_price: Decimal = Field(index=True, max_digits=6, decimal_places=2)
    cost: Decimal = Field(index=True, max_digits=6, decimal_places=2)
    quantity: int = Field(index=True)
    product_id: int = Field(foreign_key='product.id')
    department_id: int = Field(foreign_key='department.id')
    order_id: int = Field(foreign_key='order.id')
