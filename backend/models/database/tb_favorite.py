from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from backend.database.connection import Base


class ItemDetail(Base):
    __tablename__ = 'ItemDetail'
    id = Column(Integer, primary_key=True, index=True)
    itemId = Column(Integer, ForeignKey('Item.id'))
    detailId = Column(Integer, ForeignKey('Detail.id'))

class Item(Base):
    __tablename__ = 'Item'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    details = relationship('Detail', secondary=ItemDetail.__table__, backref='Item')

class Detail(Base):
    __tablename__ = 'Detail'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    items = relationship('Item', secondary=ItemDetail.__table__, backref='Detail')

class Cate(Base):
    __tablename__ = 'p_cate'
    c_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    cate_id = Column(Integer,default = 0)

class Pro(Base):
    __tablename__ = 'Prop'
    pro_id =  Column(Integer, primary_key=True)
    name = Column(String(255))
    cate_id = Column(Integer,ForeignKey('p_cate.c_id'))

class TBFavorite(Base):
    __tablename__ = 'favorite'
    favorite_id =  Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("product.product_id"))
    user_id = Column(Integer, ForeignKey("register.user_id"))
