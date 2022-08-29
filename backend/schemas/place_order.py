from typing import Optional
from pydantic import BaseModel

class PlaceOrder(BaseModel):
      username: str
      email: str
      products: str
      total_price: int
      address: str
      delivery_type: Optional[str] = 'case on delivery'
      r_id: int