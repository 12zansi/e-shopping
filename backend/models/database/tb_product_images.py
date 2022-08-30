from sqlalchemy import Column,Integer,String, ForeignKey
from backend.database.connection import Base

class TBProductImages(Base):
     __tablename__ = 'product_images'
    
     __table_args__ = {
        'mysql_engine': 'InnoDB'
     }
     image_id = Column(Integer, primary_key = True, index = True)
     color = Column(String(50))
     image_name = Column(String(100))
     total_stock = Column(Integer)
     product_id = Column(Integer, ForeignKey("product.product_id"))
     r_id = Column(Integer, ForeignKey("register.register_id"), default = 1)