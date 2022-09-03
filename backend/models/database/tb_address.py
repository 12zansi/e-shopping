from sqlalchemy import Column,String,ForeignKey,Integer,BigInteger
from backend.database.connection import Base

class TBAddress(Base):
    __tablename__ = 'address'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }
    
    address_id = Column(Integer, primary_key = True, index = True)
    mobile_no = Column(BigInteger)
    address_line =  Column(String(300))
    city = Column(String(50))
    pincode = Column(String(50))
    state = Column(String(50))
    address_type = Column(String(50))
    user_id = Column(Integer, ForeignKey("register.user_id"))
