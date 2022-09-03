from sqlalchemy import Column,String,ForeignKey,Integer,BigInteger
from backend.database.connection import Base

class TBBankAccount(Base):
    __tablename__ = 'bank_account'
    
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }
    bank_id = Column(Integer, primary_key = True, index = True)
    account_no = Column(BigInteger)
    ifsc_code =  Column(String)
    address_id = Column(Integer, ForeignKey("address.address_id"))
    user_id = Column(Integer, ForeignKey("register.user_id"))