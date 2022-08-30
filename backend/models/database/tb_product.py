from sqlalchemy import Column,Integer,String,ForeignKey
from backend.database.connection import Base

class TBProduct(Base):
    __tablename__ = 'product'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }

    product_id = Column(Integer, primary_key = True)
    name = Column(String(100))
    description = Column(String(100))
    price = Column(Integer)
    in_the_box = Column(String(1000))
    model_name = Column(String(100))
    brand_name = Column(String(100)) 
    category_name = Column(String(100))
    is_electronic = Column(String(100))
    c_id = Column(Integer,ForeignKey("category.category_id"))
    r_id = Column(Integer,ForeignKey("register.register_id"), default = 1)
