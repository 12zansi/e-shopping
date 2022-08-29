from backend.interfaces.interfaces_class import AddDataInterface
from backend.models.database.cart import TBCart
from backend.models.database.place_order import TBPlaceOrder
from backend.models.database.product import TBProduct
from backend.models.database.product_detail import TBProductDetail
from backend.models.database.product_stock import TBProductStock
from backend.schemas.cart import CartDetail
from backend.schemas.category import CategoryDetail
from backend.models.database.tb_category import TBCategory
from backend.database.session import start_session
from requests import Session
from fastapi import Depends, UploadFile, File, Form
from backend.schemas.h_accessories import Producti
from backend.schemas.place_order import PlaceOrder
import random
from backend.schemas.product import Product
from backend.schemas.product_details import ProductImage


class AddData(AddDataInterface):
    def __init__(self, db: Session = Depends(start_session)):
        self.db = db

    def _add_in_database(self, add_new_data):
        self.db.add(add_new_data)
        self.db.commit()
        self.db.refresh(add_new_data)

        return add_new_data

    def __rename_image_name(image, name: str):
        txt = image.filename
        split_image_name = txt.split(".")

        split_image_name[0] = name+str(random.randint(0, 999))
        image_name = '.'.join(split_image_name)

        with open(f'images/{name}/{image_name}', "wb") as buffer:
            buffer.write(image.file.read())

        return image_name

    def add_category(self, category: CategoryDetail):
        new_category = TBCategory(category_name = category.category_name, 
            brand_name = category.brand_name,
            b_id = category.b_id)

        return AddData._add_in_database(self, new_category)

    def add_product(self, product: Product):
        new_product = TBProduct(name = product.name,
                                description = product.description,
                                price = product.price,
                                in_the_box = product.in_the_box,
                                model_name = product.model_name,
                                brand_name = product.brand_name,
                                category_name = product.category_name,
                                is_electronic = product.is_electronic,
                                c_id = product.c_id)

        product = AddData._add_in_database(new_product)

        return product

    def add_images(self, images_list: list[UploadFile] = File(...), product_id: int = Form(...), color: str = Form(...), total_stock: int = Form(...),  db: Session = Depends(start_session)):
        image_list = []
        for image in images_list:

            image_name = AddData.__rename_image_name(image, "product")

            data = ProductImage(image = image_name,
                                color = color,
                                total_stock = total_stock,
                                product_id = product_id
                                )

            images = TBProductStock(
                product_id = data.product_id,
                image_name = data.image,
                color = data.color,
                total_stock = data.total_stock)

            AddData._add_in_database(images, db)
            image_list.append(images)
            print(data)

        return image_list

    # def add_product_detail(self, product_detail: ProductDetail):
    #     detail_list = []
    #     detail_dict = {}
    #     for t, v in zip(product_detail.detail_attribute_name, product_detail.detail_attribute_value):
    #         evn = []
    #         for i in v:

    #             product = TBProductDetail(
    #                 detail_attribute=t, detail_value=i, product_id=product_detail.product_id)
    #             AddData._add_in_database(self,product)
    #             evn.append(i)
    #             if t in detail_dict:
    #                 detail_dict[t] = evn

    #             else:
    #                 detail_dict[t] = i
    #     detail_list.append(detail_dict)

    #     return detail_list
    def add_detail(self, product: Producti):
        for i, k in product.dict_type.items():

            if type(k) == list:
                for y in k:
                    detail = TBProductDetail(
                        detail_attribute=i,
                        detail_value=y,
                        product_id=product.product_id)
                    AddData._add_in_database(self, detail)

            else:
                detail = TBProductDetail(
                    detail_attribute=i,
                    detail_value=k,
                    product_id=product.product_id)
                AddData._add_in_database(self, detail)

        return product

    def add_into_cart(self, file1: UploadFile, product_name: str = Form(...), price: int = Form(...), quantity: int = Form(...), r_id: int = Form(...)):
        mapping_cart = CartDetail(
            product_name=product_name, product_price=price, quantity=quantity, r_id=r_id)

        total_price = quantity * price

        image_name = AddData.__rename_image_name(file1, "cart")
        cart = TBCart(product_name=mapping_cart.product_name,
                      product_price=mapping_cart.product_price,
                      quantity=mapping_cart.quantity,
                      total_price=total_price,
                      c_image=image_name,
                      r_id=mapping_cart.r_id)

        return AddData._add_in_database(self, cart)

    def add_in_place_order(self, in_place_order: PlaceOrder):
        place_order = TBPlaceOrder(username=in_place_order.username,
                                   email=in_place_order.email,
                                   products=in_place_order.products,
                                   total_price=in_place_order.total_price,
                                   address=in_place_order.address,
                                   delivery_type=in_place_order.delivery_type,
                                   r_id=in_place_order.r_id)

        return AddData._add_in_database(self, place_order)
