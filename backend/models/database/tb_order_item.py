from sqlalchemy import Column,Integer,ForeignKey
from backend.database.connection import Base

class TBPOrderItem(Base):
      
      __tablename__ = 'order_item'
      __table_args__ = {
        'mysql_engine': 'InnoDB'
      }
      item_id = Column(Integer, primary_key = True, index = True)
      quantity = Column(Integer)
      product_id =  Column(Integer, ForeignKey("product.product_id"))
      image_id = Column(Integer, ForeignKey("product_images.image_id") )
      order_id =  Column(Integer, ForeignKey("user_order.order_id") )
      user_id = Column(Integer, ForeignKey("register.user_id"))