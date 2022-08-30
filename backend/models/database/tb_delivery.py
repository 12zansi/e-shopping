
from sqlalchemy import Column,Integer,String,ForeignKey
from backend.database.connection import Base

class TBDelivery(Base):
    __tablename__ = 'delivery'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }

    delivery_id = Column(Integer, primary_key = True, index = True)

    delivery_type = Column(String(50), default = "cash on delivery")
    status_id = Column(Integer,ForeignKey("status.status_id"))


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