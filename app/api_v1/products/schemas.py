from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    price: int


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)  # @todo что это
    id: int
