from sqlalchemy import Column,Integer,String
from database.connection import Base

class TBHAccessories(Base):
    __tablename__ = 'h_accessories'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }
    
    a_id = Column(Integer, primary_key = True, index = True)
    febric = Column(String(50), default = None)
    ideal_for = Column(String(50), default = None)
    pattern = Column(String(50), default = None)

    type = Column(String(50), default = None)
    type_of_flats = Column(String(50), default = None)
    closure = Column(String(50), default = None)

    dial_color = Column(String(50), default = None)
    display_type = Column(String(50), default = None)
    watch_type = Column(String(50), default = None)

    minimum_age = Column(Integer, default = 0)
    material = Column(String(50), default = None)

    p_id = Column(String(50), unique = True)