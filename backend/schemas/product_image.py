from pydantic import BaseModel
    
class ProductImage(BaseModel):
    image: str
    product_id: int
   

class Image(BaseModel): 
    product_id: int
    image_id: int