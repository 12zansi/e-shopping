from pydantic import BaseModel

class Favorite(BaseModel):
    product_id: int
    user_id: int