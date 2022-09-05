from typing import Optional
from pydantic import BaseModel

class OrderDetail(BaseModel):
      total_price: int
      delivery_type: Optional[str] = 'case on delivery'
      address_id: int
      user_id: int