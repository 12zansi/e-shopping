from pydantic import BaseModel

class ProductDetail(BaseModel):
    detail_attribute_name: list[str]
    detail_attribute_value: list[list[str]]
    product_id: int
    
class ProductImage(BaseModel):
    image: str
    color: str
    total_stock: int
    product_id: int
   