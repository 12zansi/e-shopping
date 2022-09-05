from pydantic import BaseModel

class Address(BaseModel):
    mobile_no: int
    address_line: str
    city: str
    pincode: int
    state: str
    address_type: str
    user_id: int