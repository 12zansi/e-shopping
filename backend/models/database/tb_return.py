from sqlalchemy import Column,String,ForeignKey,Integer
from backend.database.connection import Base

class TBReturn(Base):
    __tablename__ = 'return'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }
    
    return_id = Column(Integer, primary_key = True, index = True)
    reason = Column(String)
    order_item_id =  Column(Integer, ForeignKey("order_item.item_id") )
    order_id =  Column(Integer, ForeignKey("user_order.order_id") )
    user_id = Column(Integer, ForeignKey("register.user_id"))
