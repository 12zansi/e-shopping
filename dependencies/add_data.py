
from typing import Optional
from interfaces.interfaces_class import AddDataInterface
from models.database.cart import TBCart
from models.database.product import TBProduct
from models.database.product_detail import TBProductDetail
from models.database.product_electronic import TBProductElectronic
from schemas.cart import CartDetail
from schemas.category import CategoryDetail
from models.database.tb_category import TBCategory
from database.session import start_session
from requests import Session
from fastapi import Depends,UploadFile,File,Form

from schemas.product import Product
from schemas.product_details import ProductDetail

class AddData(AddDataInterface):

    def add_in_database(add_new_data, db:Session = Depends(start_session)):
        db.add(add_new_data)
        db.commit()
        db.refresh(add_new_data)
        return add_new_data

    def add_category(self, category: CategoryDetail, db:Session = Depends(start_session)):
        new_category = TBCategory(category_name = category.category_name,
          b_id = category.b_id)
        return AddData.add_in_database(new_category,db)

    def add_product(self,product: Product,db:Session = Depends(start_session)):
        new_product = TBProduct(name = product.name, 
            description = product.description, 
            price = product.price,
            in_the_box = product.in_the_box,
            model_name = product.model_name,
            brand_name = product.brand_name,
            category_name = product.category_name,
            is_electronic = product.is_electronic,
            c_id = product.c_id )

        product = AddData.add_in_database(new_product, db)

        return product

    def add_product_detail(self,product_detail: ProductDetail,db:Session = Depends(start_session)):
        for i,v in zip(product_detail.detail_attribute_name,product_detail.detail_attribute_value):
            product = TBProductDetail(detail_attribute = i,detail_value = v,product_name = product_detail.product_name)
            AddData.add_in_database(product, db)
        return "successfully inserted"


    def add_cart(self,file1: UploadFile,product_name: str = Form(...), price: int = Form(...), quantity: int = Form(...),r_id: int = Form(...),  db: Session = Depends(start_session)):
        mapping_cart = CartDetail(product_name = product_name,product_price=price,quantity=quantity,r_id = r_id)
        total_price = quantity * price
        cart = TBCart(product_name = mapping_cart.product_name,product_price = mapping_cart.product_price,quantity = mapping_cart.quantity,total_price = total_price,c_image = file1.filename,r_id = mapping_cart.r_id)
       
        return AddData.add_in_database(cart, db)