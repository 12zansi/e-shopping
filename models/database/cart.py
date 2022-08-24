from sqlalchemy import Column,Integer,String
from sqlalchemy_utils import URLType
from database.connection import Base
 
class TBCart(Base):
    __tablename__ = 'cart'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }

    cart_id = Column(Integer, primary_key = True, index = True)
    product_name = Column(String(50))
    c_image = Column(URLType)
    product_price = Column(Integer)
    quantity = Column(Integer)
    total_price = Column(Integer)
    r_id = Column(Integer)