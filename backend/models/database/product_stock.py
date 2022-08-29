from sqlalchemy import Column,Integer,String
from backend.database.connection import Base

class TBProductStock(Base):
     __tablename__ = 'product_images'
    
     __table_args__ = {
        'mysql_engine': 'InnoDB'
     }
     color_id = Column(Integer, primary_key = True, index = True)
     color = Column(String(50))
     image_name = Column(String(100))
     total_stock = Column(Integer)
     product_id = Column(Integer)
     r_id = Column(Integer,default = 1)