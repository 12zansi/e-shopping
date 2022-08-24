from sqlalchemy import Column,Integer,String
from database.connection import Base

class TBBrand(Base):
    __tablename__ = 'brand'
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }
    brand_id = Column(Integer, primary_key = True, index = True)
    brand_name = Column(String(50), unique = True)
    u_id = Column(Integer)