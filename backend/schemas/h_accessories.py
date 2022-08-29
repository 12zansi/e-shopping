from typing import Optional
from pydantic import BaseModel

class HAccessories(BaseModel):
    febric: Optional[str] = ''
    ideal_for: Optional[str] = ""
    pattern: Optional[str] = ""

    footwear_type:  Optional[str] = ""
    type_of_flats:  Optional[str] = ""
    closure: Optional[str] = ""

    dial_color: Optional[str] = ""
    display_type: Optional[str] = ""
    watch_type: Optional[str] = ""

    minimum_age: Optional[int] = 0
    material: Optional[str] = ""

    p_id:Optional[int] = 0

class MultiProductType(BaseModel):
    product_name : str
    color: str
    image_name : str
    total_stock: int

class Producti(BaseModel):
     dict_type: dict
     product_id: int