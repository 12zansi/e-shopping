from sqlalchemy import Column,Integer,String, ForeignKey
from sqlalchemy_utils import URLType
from backend.database.connection import Base
 
class TBCart(Base):
    __tablename__ = 'cart'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }

    cart_id = Column(Integer, primary_key = True, index = True)
    quantity = Column(Integer)
    product_id = Column(Integer, ForeignKey("product.product_id"))
    image_id = Column(Integer, ForeignKey("product_images.image_id") )
    user_id = Column(Integer,ForeignKey("register.user_id"))