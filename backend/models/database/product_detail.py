from sqlalchemy import Column,Integer,String,VARCHAR
from backend.database.connection import Base

class TBProductDetail(Base):
     __tablename__ = 'product_detail'
    
     __table_args__ = {
        'mysql_engine': 'InnoDB'
     }

     p_detail_id = Column(Integer, primary_key = True, index = True)
     detail_attribute = Column(String(50))
     detail_value = Column(String(50))
     product_id = Column(Integer)
     r_id = Column(Integer,default = 1)