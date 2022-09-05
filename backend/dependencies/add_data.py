
from webbrowser import get
from backend.interfaces.interfaces_class import AddDataInterface
from backend.models.database.tb_favorite import Cate, Detail, Item, ItemDetail, Pro
from backend.models.database.tb_address import TBAddress
from backend.models.database.tb_cart import TBCart
from backend.models.database.tb_place_order import TBPlaceOrder
from backend.models.database.tb_product import TBProduct
from backend.models.database.tb_product_detail import TBProductDetail
from backend.models.database.tb_product_images import TBProductImages
from backend.models.database.tb_status import TBStatus
from backend.schemas.address import Address
from backend.schemas.cart import CartDetail
from backend.schemas.category import CategoryDetail
from backend.models.database.tb_category import TBCategory
from backend.database.session import start_session
from requests import Session
from fastapi import Depends, UploadFile, File, Form
from backend.schemas.favorite import Favorite
from backend.schemas.product_detail import ProductDetail
from backend.schemas.place_order import OrderDetail
import random
from backend.schemas.product import Product
from backend.schemas.product_image import ProductImage
from backend.schemas.status import Status


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
            parent_id = category.parent_id)

        return AddData._add_in_table(self, new_category)


    def add_address(self, address: Address):
        new_address = TBAddress(mobile_no = address.mobile_no,
            address_line = address.address_line, 
            city = address.city,
            pincode = address.pincode,
            state = address.state,
            address_type = address.address_type,
            user_id = address.user_id)

        return AddData._add_in_table(self, new_address)

    def add_product(self, product: Product):
        new_product = TBProduct(name = product.name,
                                description = product.description,
                                mrp = product.mrp,
                                price = product.price,
                                model_name = product.model_name,
                                brand_id = product.brand_id,
                                category_id = product.category_id,
                                return_policy = product.return_policy)


        product = AddData._add_in_table(self,new_product)

        return product

    def add_images(self, images_list: list[UploadFile] = File(...), product_id: int = Form(...)):
        image_list = []
        for image in images_list:

            image_name = AddData.__rename_image_name(image, "product_images")

            data = ProductImage(image = image_name,
                                product_id = product_id
                                )

            images = TBProductImages(
                image_name = data.image,
                product_id = data.product_id)

            AddData._add_in_table(self, images)
            image_list.append(data)
            
        get_data = self.db.query(TBProductImages).filter(TBProductImages.product_id == images.product_id).limit(1).all()
      
        # only = Image(image_id = get_data[0].image_id, product_id = get_data[0].product_id)
        # only_table = TBImages(image_id = only.image_id, product_id = only.product_id)
        # AddData._add_in_table(self, only_table)

        return get_data

    
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

        # total_price = cart_detail.quantity * cart_detail.produ

        cart = TBCart(
                      quantity = cart_detail.quantity,
                      image_id = cart_detail.image_id,
                      product_id = cart_detail.product_id,
                      user_id = cart_detail.user_id)

        return AddData._add_in_table(self, cart)


    def add_in_place_order(self, in_place_order: OrderDetail):

        place_order = TBPlaceOrder(
                                   total_price = in_place_order.total_price,
                                   address_id = in_place_order.address_id,
                                   delivery_type = in_place_order.delivery_type,
                                   user_id = in_place_order.user_id)

        return AddData._add_in_table(self, place_order)

    def add_favorite(self, item:Favorite):
        favorite = ItemDetail(product_id = item.product_id, user_id = item.user_id)
        AddData._add_in_table(self, favorite)
        return favorite

    def add_in_status(self, status: Status):
        status = TBStatus(status_name = status.status_name)
        AddData._add_in_table(self, status)
        return status

    # def add_pro(self, item: Bpro):
    #     add_cate = Pro(name = item.name, cate_id = item.c_id)
    #     AddData._add_in_table(self, add_cate)
    #     return add_cate

