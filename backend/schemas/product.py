from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):

    name: str
    description: str
    mrp: int
    price: int
    model_name: str
    brand_id: str
    category_id: int
    return_policy: int


