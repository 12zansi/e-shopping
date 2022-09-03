from sqlalchemy import Column,Integer,String, ForeignKey
from backend.database.connection import Base

class TBProductDetail(Base):
     __tablename__ = 'product_detail'
    
     __table_args__ = {
        'mysql_engine': 'InnoDB'
     }

     detail_id = Column(Integer, primary_key = True, index = True)
     attribute_name = Column(String(50))
     attribute_value = Column(String(50))
     product_id = Column(Integer, ForeignKey("product.product_id"))
     user_id = Column(Integer,ForeignKey("register.user_id"), default = 1)