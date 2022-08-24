
from typing import Optional
from pydantic import BaseModel,HttpUrl

class BrandDetail(BaseModel):
     brand_name: str
     user_id: int

class Attribute1(BaseModel):
     s_name: str
     # s_value: HttpUrl
     # s_value: Optional[str] = ''
     b_id: int

     # class Config:
     #    orm_mode = True