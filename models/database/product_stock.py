from sqlalchemy import Column,Integer,String,VARCHAR
from database.connection import Base

class TBProductStock(Base):
     __tablename__ = 'product_stock'
    
     __table_args__ = {
        'mysql_engine': 'InnoDB'
     }
     color_id = Column(Integer, primary_key = True, index = True)
     attribute_name = Column(String(50))
     attribute_value = Column(String(500))
     p_id = Column(Integer)