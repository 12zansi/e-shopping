from typing import Optional
from pydantic import BaseModel,HttpUrl

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