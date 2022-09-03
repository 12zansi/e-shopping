from pydantic import BaseModel

class BItemDetail(BaseModel):
    item_id: int
    detail_id: int

class BItem(BaseModel):
    name: str

class BDetail(BaseModel):
    name: str

class Bcate(BaseModel): 
    name: str
    cate_id: int

class Bpro(BaseModel):
    name: str
    c_id: int
