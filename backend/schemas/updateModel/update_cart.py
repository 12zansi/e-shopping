from pydantic import BaseModel

class UpdateQuantity(BaseModel):
    cart_id: int
    quantity: int
