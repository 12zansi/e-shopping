from typing import Optional
from pydantic import BaseModel

class DeleteCart(BaseModel):
    cart_id: Optional[int] = 0
    r_id: int
