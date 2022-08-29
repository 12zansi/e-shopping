from typing import Optional
from pydantic import BaseModel

class PElectronic(BaseModel):
    
    capacity: Optional[str] = ''
    technology: Optional[str] = ''
    ram : Optional[str] = ''
    display_size: Optional[str] = ''
    battery_type: Optional[str] = ''
    operating_system: Optional[str] = ''
    internal_storage: Optional[str] = ''
    resolution: Optional[str] = ''
    processor_brand: Optional[str] = ''
    processor_name: Optional[str] = ''
    ssd: Optional[str] = ''
    no_of_door: Optional[int] = ''
    processor_type: Optional[str] = ''
    p_id: Optional[int] = ''
