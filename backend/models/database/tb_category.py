from email.policy import default
from sqlalchemy import Column,Integer,String, ForeignKey
from backend.database.connection import Base

class TBCategory(Base):
    __tablename__ = 'category'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }

    category_id = Column(Integer, primary_key = True, index = True)
    category_name = Column(String(50))
    parent_id = Column(Integer,ForeignKey("category.category_id"), default = 0)
    user_id = Column(Integer, ForeignKey("register.user_id"), default = 1)

    