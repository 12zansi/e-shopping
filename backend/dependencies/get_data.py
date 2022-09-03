from typing import Optional
from backend.database.session import start_session
from requests import Session
from fastapi import Depends
from sqlalchemy import cast, Integer, Text, Column, ForeignKey, literal, null
from backend.schemas.detail import BDetail, BItem, BItemDetail
from backend.models.database.tb_favorite import Cate, Detail, Item, ItemDetail, Pro
from backend.models.database.tb_product import TBProduct
from backend.models.database.tb_brand import TBBrand
from backend.models.database.tb_category import TBCategory
from sqlalchemy.orm import aliased


class GetData:
    def __init__(self, db: Session = Depends(start_session)):
        self.db = db

    def get_data(self, search_for: str, name: Optional[str] = '', id: Optional[int] = None):

        if search_for == 'product':
            product_detail = self.db.query(TBProduct).all()
            if name != '':
                product_detail = self.db.query(TBProduct).filter(
                    TBProduct.name.like(name)).first()
            elif id != None:
                product_detail = self.db.query(TBProduct).filter(
                    TBProduct.product_id.like(id)).first()

        elif search_for == 'category':
            product_detail = self.db.query(TBCategory).all()
            if name != '':
                product_detail = self.db.query(TBCategory).filter(
                    TBCategory.category_name.like(name)).all()

        elif search_for == 'brand':
            product_detail = self.db.query(TBBrand).all()

        else:
            product_detail = "please enter brand or category or product"

        return product_detail

    def get_product(self, product: Optional[str] = '', db: Session = Depends(start_session)):
        if product != '':
            get_product_detail = self.db.query(TBProduct).filter(
                TBProduct.name.like(product)).all()

        else:
            get_product_detail = self.db.query(TBProduct).all()
        return get_product_detail


    def get_item(self,id:int, db: Session = Depends(start_session)):

        get = db.query(Detail.name, Item.name ).filter(Detail.id == id).join(ItemDetail, Detail.id == ItemDetail.detailId).join(Item, ItemDetail.detailId == Item.id).all()
        dict = {}
        for i in get:
            print(i[1])
           
            if i[0] in dict:
                dict[i[0]].append(i[1])
            else:
               dict[i[0]] = [i[1]]
        print(dict)
        return get
    
    def get_cate(self,id:int, db: Session = Depends(start_session)):
        category = db.query(Cate).filter(Cate.cate_id == id).all()
        # hierarchy = db.query(Cate).filter(Cate.c_id == id).cte(name="hierarchy", recursive=True)
        # parent = aliased(hierarchy, name="p")
        # children = aliased(Cate, name="c")
        # print(db.query(children).filter(children.cate_id == parent.c.c_id))
        # udp = hierarchy.union_all(db.query(Pro).filter(Pro.cate_id == parent.c.c_id))
        # hierarchy = hierarchy.union_all(db.query(children).filter(children.cate_id == parent.c.c_id))
        # dep = db.query(Cate).filter(Cate.cate_id == id).all()
        # print(dep[0].cate_id)
        # urp = db.query(Pro).filter(Pro.cate_id == ).all()
        # return dep
        
        # ud = db.query(Pro).select_entity_from(udp).all()
        # result = db.query(Cate).select_entity_from(hierarchy).all()
        # return category,result,ud
        beginning_getter = db.query(Cate).filter(Cate.cate_id ==  id).cte(name='parent_for', recursive=True)
        print(db.query(Cate).filter (Cate.c_id == beginning_getter.c.cate_id))
        with_recursive = beginning_getter.union_all(db.query(Cate).filter (Cate.cate_id == beginning_getter.c.c_id))
        urp = db.query(with_recursive).all()
        uep = []
        for i in urp:
              print(i[0])
              dg = db.query(Pro).filter(Pro.cate_id == i[0]).all() 
              uep.append(dg)
            # for j in i:
            #     print(j)
        print(urp)
        return category,urp,uep
        
