from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str
    price: str


class Product(ProductBase):
    id: int

class ProductCreate(ProductBase):
    pass