from pydantic import BaseModel

class Address(BaseModel):
    area: str
    city: str
    pincode: int
    state: str
    r_id: int