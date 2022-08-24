
from sqlalchemy import Column,Integer,String
from database.connection import Base


class TBRegister(Base):
    __tablename__ = 'register'
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }
    user_id = Column(Integer, primary_key = True, index = True)
    username = Column(String(50), unique = True)
    email = Column(String(70), unique = True)
    password = Column(String(200))
    is_admin = Column(Integer, default = 0)




