from pydantic import BaseModel,HttpUrl
from fastapi import UploadFile,File

class CartDetail(BaseModel):
    product_name: str
    product_price: int
    quantity: int
    image_id: int
    detail_id: int
    r_id: int