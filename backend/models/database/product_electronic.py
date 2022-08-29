
from sqlalchemy import Column,Integer,String
from database.connection import Base

class TBProductElectronic(Base):
    __tablename__ = 'product_electronic'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }

    electronic_id = Column(Integer, primary_key = True, index = True)
    capacity = Column(String(50), default = None)
    technology = Column(String(50), default = None)

    ram =  Column(String(50), default = None)
    display_size = Column(String(50), default = None)
    battery_type = Column(String(50), default = None)
    operating_system = Column(String(50), default = None)
    internal_storage = Column(String(50), default = None)
    resolution = Column(String(50), default = None)
    processor_brand = Column(String(50), default = None)
    processor_name = Column(String(50), default = None)
    ssd = Column(String(50), default = None)

    no_of_doors = Column(Integer, default = 0)
    warranty = Column(String(50))

    processor_type = Column(String(50), default = None)

    p_id = Column(Integer, unique = True)
