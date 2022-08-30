from sqlalchemy import Column,Integer,String, ForeignKey
from sqlalchemy_utils import URLType
from backend.database.connection import Base
 
class TBCart(Base):
    __tablename__ = 'cart'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }

    cart_id = Column(Integer, primary_key = True, index = True)
    product_name = Column(String(250))
    image_id = Column(Integer, ForeignKey("product_images.image_id") )
    detail_id = Column(Integer, ForeignKey("product_detail.detail_id"))
    product_price = Column(Integer)
    quantity = Column(Integer)
    total_price = Column(Integer)
    r_id = Column(Integer,ForeignKey("register.register_id"))