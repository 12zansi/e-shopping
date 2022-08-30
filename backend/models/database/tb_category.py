from sqlalchemy import Column,Integer,String, ForeignKey
from backend.database.connection import Base

class TBCategory(Base):
    __tablename__ = 'category'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }

    category_id = Column(Integer, primary_key = True, index = True)
    category_name = Column(String(50))
    b_id = Column(Integer,ForeignKey("brand.brand_id"))
    r_id = Column(Integer, ForeignKey("register.register_id"), default = 1)

    