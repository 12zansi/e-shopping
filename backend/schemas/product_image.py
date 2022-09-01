from pydantic import BaseModel
    
class ProductImage(BaseModel):
    image: str
    color: str
    total_stock: int
    product_id: int
   

class Image(BaseModel): 
    product_id: int
    image_id: int