from pydantic import BaseModel

class ProductDetail(BaseModel):
    detail_attribute_name: list[str]
    detail_attribute_value: list[str]
    product_name: str