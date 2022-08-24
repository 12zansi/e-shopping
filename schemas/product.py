from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):

    name: str
    description: str
    price: int
    in_the_box: str
    model_name: str
    brand_name: str
    category_name: str
    is_electronic: Optional[str] = 'yes'
    c_id: int


