from typing import Optional
from backend.database.session import start_session
from requests import Session
from fastapi import Depends

from backend.models.database.product import TBProduct
from backend.models.database.tb_brand import TBBrand
from backend.models.database.tb_category import TBCategory


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
