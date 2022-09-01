
from datetime import date
from sqlalchemy import Column,Integer,String,ForeignKey,DateTime
from backend.database.connection import Base

class TBDelivery(Base):
    __tablename__ = 'delivery'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }

    delivery_id = Column(Integer, primary_key = True, index = True)
    shipping_price = Column(Integer, default = 0)
    Total_Price = Column(Integer)
    delivery_type = Column(String(50), default = "cash on delivery")
    delivery_date = Column(DateTime, )
    courier_boy_id = Column(Integer, ForeignKey("courier_boy.id") )
    order_id = Column(Integer, ForeignKey("order.order_id"))


# Table flipcart.status{
#    status_id int
#    status_name str
# }

# Table flipcart.delivery{
#   delivery_id int
#   delivery_date date
#   delivery_type str
#   status_id str
#   place_order_id int
#   courier_id int
#   courier_boy_id int
# }