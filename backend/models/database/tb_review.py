import datetime
from sqlalchemy import Column,String,ForeignKey,Integer,DateTime
from backend.database.connection import Base

class TBReview(Base):
    __tablename__ = 'review'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }
    review_id = Column(Integer, primary_key = True, index = True)
    rating = Column(Integer)
    review = Column(String)
    date  = Column(DateTime, default = datetime.datetime.today())
    like = Column(Integer, default = 1)
    product_id = Column(Integer, ForeignKey("product.product_id"))
    user_id = Column(Integer, ForeignKey("register.user_id"))
