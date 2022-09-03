from sqlalchemy import Column,Integer,String,ForeignKey
from backend.database.connection import Base

class TBProduct(Base):
    __tablename__ = 'product'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }

    product_id = Column(Integer, primary_key = True)
    name = Column(String(100), unique = True)
    return_policy = Column(Integer)
    description = Column(String(100))
    mrp = Column(Integer)
    price = Column(Integer)
    model_name = Column(String(100))
    category_id = Column(Integer,ForeignKey("category.category_id"))
    brand_id = Column(Integer,ForeignKey("brand.brand_id"))
    user_id = Column(Integer,ForeignKey("register.user_id"), default = 1)
