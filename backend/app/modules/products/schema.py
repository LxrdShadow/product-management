from typing import Optional

from pydantic import BaseModel


class ProductBase(BaseModel):
    number: str
    design: str
    price: int
    quantity: int


class ProductCreate(ProductBase):
    pass


class ProductOut(ProductBase):
    pass


class ProductUpdate:
    design: Optional[str] = None
    price: Optional[int] = None
    quantity: Optional[int] = None
