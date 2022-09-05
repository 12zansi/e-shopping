from pydantic import BaseModel,HttpUrl
from fastapi import UploadFile,File

class CategoryDetail(BaseModel):
    category_name: str
    parent_id: int
