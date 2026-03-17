from pydantic import BaseModel


class ProductBase(BaseModel):
    pass


class ProductCreate(ProductBase):
    number: str
    design: str
    price: int
    quantity: int
