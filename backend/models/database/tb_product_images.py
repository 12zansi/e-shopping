from sqlalchemy import Column,Integer,String, ForeignKey
from backend.database.connection import Base

class TBProductImages(Base):
     __tablename__ = 'product_images'
    
     __table_args__ = {
        'mysql_engine': 'InnoDB'
     }
     image_id = Column(Integer, primary_key = True, index = True)
     image_name = Column(String(100))
     product_id = Column(Integer, ForeignKey("product.product_id"))
     user_id = Column(Integer, ForeignKey("register.user_id"), default = 1)

# class TBImages(Base):
#      __tablename__ = 'images'
    
#      __table_args__ = {
#         'mysql_engine': 'InnoDB'
#      }
#      id = Column(Integer, primary_key = True, index = True)
#      image_id = Column(Integer, ForeignKey("product_images.image_id"))
#      product_id = Column(Integer, ForeignKey("product.product_id"))