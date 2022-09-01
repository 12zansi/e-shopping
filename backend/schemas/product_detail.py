from pydantic import BaseModel

class ProductDetail(BaseModel):
    dict_type: dict
    product_id: int

    
# class MultiProductType(BaseModel):
#     product_name : str
#     color: str
#     image_name : str
#     total_stock: int
