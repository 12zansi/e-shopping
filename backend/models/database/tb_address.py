from sqlalchemy import Column,Integer,String,ForeignKey
from backend.database.connection import Base

class TBAddress(Base):
    __tablename__ = 'address'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }
    
    address_id = Column(Integer, primary_key = True, index = True)
    area =  Column(String(250))
    city = Column(String(50))
    pincode = Column(String(50))
    state = Column(String(50))
    r_id = Column(Integer, ForeignKey("register.register_id"))
