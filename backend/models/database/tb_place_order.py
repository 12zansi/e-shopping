import datetime
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from backend.database.connection import Base

# NextDay_Date = datetime.datetime.today() + datetime.timedelta(days = 3)

class TBPlaceOrder(Base):
      
      __tablename__ = 'user_order'
      __table_args__ = {
        'mysql_engine': 'InnoDB'
      }
      order_id = Column(Integer, primary_key = True, index = True)
      total_price = Column(Integer)
      delivery_type = Column(String(50), default = "cash on delivery")
      address_id = Column(Integer, ForeignKey("address.address_id"))
      order_date = Column(DateTime, default = datetime.datetime.today())
      status = Column(Integer,ForeignKey("status.status_id"), default = 1)
      user_id = Column(Integer, ForeignKey("register.user_id"))