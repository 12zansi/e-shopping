from typing import Optional
from pydantic import BaseModel

class Status(BaseModel):
    status_name: str

class Delivery(BaseModel):

    delivery_type: str
    
    status_id: int
   