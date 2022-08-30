from typing import Optional
from pydantic import BaseModel

class PlaceOrder(BaseModel):
      product_name: str
      total_price: int
      address_id: int
      delivery_type: Optional[str] = 'case on delivery'
      r_id: int