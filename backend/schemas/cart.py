from pydantic import BaseModel,HttpUrl
from fastapi import UploadFile,File

class CartDetail(BaseModel):
    quantity: int
    product_id: int
    image_id: int
    user_id: int