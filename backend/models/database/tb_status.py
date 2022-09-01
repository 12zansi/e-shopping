from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import  relationship
from backend.database.connection import Base

class TBStatus(Base):
    __tablename__ = 'order_status'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }
    
    status_id =  Column(Integer, primary_key = True, index = True)
    status_name = Column(String(70), unique = True)
