
from webbrowser import get
from backend.interfaces.interfaces_class import AddDataInterface
from backend.models.database.tb_favorite import Cate, Detail, Item, ItemDetail, Pro
from backend.models.database.tb_address import TBAddress
from backend.models.database.tb_cart import TBCart
from backend.models.database.tb_place_order import TBPlaceOrder
from backend.models.database.tb_product import TBProduct
from backend.models.database.tb_product_detail import TBProductDetail
from backend.models.database.tb_product_images import TBProductImages,TBImages
from backend.schemas.address import Address
from backend.schemas.cart import CartDetail
from backend.schemas.category import CategoryDetail
from backend.models.database.tb_category import TBCategory
from backend.database.session import start_session
from requests import Session
from fastapi import Depends, UploadFile, File, Form
from backend.schemas.detail import BDetail, BItem, BItemDetail, Bcate, Bpro
from backend.schemas.product_detail import ProductDetail
from backend.schemas.place_order import PlaceOrder
import random
from backend.schemas.product import Product
from backend.schemas.product_image import ProductImage, Image


class AddData(AddDataInterface):
    def __init__(self, db: Session = Depends(start_session)):
        self.db = db

    def _add_in_table(self, add_new_data):
        self.db.add(add_new_data)
        self.db.commit()
        self.db.refresh(add_new_data)

        return add_new_data


    def __rename_image_name(image1, name: str):
        print(image1)
        txt = image1.filename
        split_image_name = txt.split(".")
       
        split_image_name[0] = name+str(random.randint(0, 999))
        image_name = '.'.join(split_image_name)
        print(image_name)
        with open(f'backend/images/{name}/{image_name}', "wb") as buffer:
            buffer.write(image1.file.read())
        
        return image_name


    def add_category(self, category: CategoryDetail):
        new_category = TBCategory(category_name = category.category_name, 
            b_id = category.b_id)

        return AddData._add_in_table(self, new_category)


    def add_address(self, address: Address):
        new_address = TBAddress(area = address.area, 
            city = address.city,
            pincode = address.pincode,
            state = address.state,
            r_id = address.r_id)

        return AddData._add_in_table(self, new_address)

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

        product = AddData._add_in_table(self,new_product)

        return product

    def add_images(self, images_list: list[UploadFile] = File(...), product_id: int = Form(...), color: str = Form(...), total_stock: int = Form(...),  db: Session = Depends(start_session)):
        image_list = []
        for image in images_list:

            image_name = AddData.__rename_image_name(image, "product_images")

            data = ProductImage(image = image_name,
                                color = color,
                                total_stock = total_stock,
                                product_id = product_id
                                )

            images = TBProductImages(
                product_id = data.product_id,
                image_name = data.image,
                color = data.color,
                total_stock = data.total_stock)

            AddData._add_in_table(self, images)
            image_list.append(data)
            
        get_data = self.db.query(TBProductImages).filter(TBProductImages.product_id == images.product_id).limit(1).all()
      
        only = Image(image_id = get_data[0].image_id, product_id = get_data[0].product_id)
        only_table = TBImages(image_id = only.image_id, product_id = only.product_id)
        AddData._add_in_table(self, only_table)


        return only_table

    
    def add_detail(self, product: ProductDetail):
        for i, k in product.dict_type.items():

            if type(k) == list:
                for y in k:
                    detail = TBProductDetail(
                        attribute_name = i,
                        attribute_value = y,
                        product_id = product.product_id)
                    AddData._add_in_table(self, detail)

            else:
                detail = TBProductDetail(
                    attribute_name = i,
                    attribute_value = k,
                    product_id = product.product_id)
                AddData._add_in_table(self, detail)

        return product


    def add_into_cart(self,cart_detail: CartDetail):

        total_price = cart_detail.quantity * cart_detail.product_price

        cart = TBCart(product_name = cart_detail.product_name,
                      product_price = cart_detail.product_price,
                      quantity = cart_detail.quantity,
                      total_price = total_price,
                      image_id = cart_detail.image_id,
                      detail_id = cart_detail.detail_id,
                      r_id = cart_detail.r_id)

        return AddData._add_in_table(self, cart)


    def add_in_place_order(self, in_place_order: PlaceOrder):

        place_order = TBPlaceOrder(username=in_place_order.username,
                                   email=in_place_order.email,
                                   products=in_place_order.products,
                                   total_price=in_place_order.total_price,
                                   address=in_place_order.address,
                                   delivery_type=in_place_order.delivery_type,
                                   r_id=in_place_order.r_id)

        return AddData._add_in_table(self, place_order)

    def add_y(self, item: BItemDetail):
        add_y = ItemDetail(itemId = item.item_id, detailId = item.detail_id)
        AddData._add_in_table(self, add_y)
        return add_y

    def add_cate(self, item: Bcate):
        add_cate = Cate(name = item.name, cate_id = item.cate_id)
        AddData._add_in_table(self, add_cate)
        return add_cate

    def add_pro(self, item: Bpro):
        add_cate = Pro(name = item.name, cate_id = item.c_id)
        AddData._add_in_table(self, add_cate)
        return add_cate

