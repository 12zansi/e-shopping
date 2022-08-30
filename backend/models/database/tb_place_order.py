import datetime
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from backend.database.connection import Base

NextDay_Date = datetime.datetime.today() + datetime.timedelta(days = 3)

class TBPlaceOrder(Base):
      
      __tablename__ = 'place_order'
      __table_args__ = {
        'mysql_engine': 'InnoDB'
      }
      order_id = Column(Integer, primary_key = True, index = True)
      product_names = Column(String(550))
      total_price = Column(Integer)
      address_id = Column(Integer, ForeignKey("address.address_id"))
      order_date = Column(DateTime, default = datetime.datetime.today())
      delivery_date = Column(DateTime, default = NextDay_Date)
      delivery_type = Column(String(40))
      r_id = Column(Integer, ForeignKey("register.register_id"))