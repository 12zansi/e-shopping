from typing import Optional
from fastapi import FastAPI, Depends, UploadFile, File, Form
from backend.database.connection import connection, Base
from backend.database.session import start_session
from requests import Session
from backend.dependencies.add_data import AddData
from backend.dependencies.delete_data import DeleteData
from backend.dependencies.get_data import GetData
from backend.dependencies.login import LoginUser
from backend.dependencies.registration import NewUser, TBRegister
from backend.dependencies.update_data import UpdateData
from backend.models.database.product_detail import TBProductDetail
from backend.models.database.product_electronic import TBDelivery
from backend.models.database.status import TBStatus
from backend.models.database.tb_brand import TBBrand
from backend.models.database.tb_category import TBCategory
from backend.models.database.tb_register import TBRegister
from backend.schemas.brand import BrandDetail
from backend.schemas.category import CategoryDetail
from backend.schemas.delete_model.delete_cart import DeleteCart
from backend.schemas.h_accessories import Producti
from backend.schemas.p_electronic import Delivery, Status
from backend.schemas.place_order import PlaceOrder
from backend.schemas.product import Product
from backend.schemas.product_details import ProductDetail
from backend.schemas.register import CreateUser, Login
from backend.schemas.updateModel.update_cart import UpdateQuantity
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
       title="e-Shopping",
       description="This is online shopping site for customer."
)

Base.metadata.create_all(bind=connection)
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/auth/registeration",tags=['auth'])
def create_user(user: CreateUser, db: Session = Depends(start_session), register_detail: NewUser = Depends(NewUser)):
    return register_detail.create_user(user, db)


@app.post("/auth/login",tags=['auth'])
def login(form_data: Login, db: Session = Depends(start_session), login_detail: LoginUser = Depends(LoginUser)):
    return login_detail.login_detail(form_data, db)


@app.post('/brand', tags=['brand'])
def add_brand(brand: BrandDetail, db: Session = Depends(start_session), brand_detail: NewUser = Depends(NewUser)):
    return brand_detail.add_brand(brand, db)


@app.post('/category', tags=['category'])
def add_category(category: CategoryDetail, category_detail: AddData = Depends(AddData)):
    return category_detail.add_category(category)


@app.post('/product', tags=['product'])
def add_product(product: Product, product_detail: AddData = Depends(AddData)):

    return product_detail.add_product(product)


@app.post('/product/product1', tags=['product'])
def add(product: Producti, db: Session = Depends(start_session)):
    for i, k in product.dict_type.items():

        if type(k) == list:
            for y in k:
                product1 = TBProductDetail(
                    detail_attribute=i, detail_value=y, product_id=product.product_id)
                db.add(product1)
                db.commit()
                db.refresh(product1)
        else:
            product1 = TBProductDetail(
                detail_attribute=i, detail_value=k, product_id=product.product_id)
            db.add(product1)
            db.commit()
            db.refresh(product1)
    return product


@app.get('/product')
def search_product(search_for: str = '', name: Optional[str] = '', id: Optional[int] = None, get_product_detail: GetData = Depends(GetData)):
    return get_product_detail.get_data(search_for, name, id)


@app.get('/product/get_brand', tags=['product'])
def get_brand(db: Session = Depends(start_session)):

    brand = db.query(TBBrand).all()
    category = db.query(TBCategory).all()

    return brand, category


@app.post('/product/add_product_images', tags=['product'])
def add_produck_stock(file1: list[UploadFile] = File(...), product_id: int = Form(...), color: str = Form(...), total_product: int = Form(...), add_images: AddData = Depends(AddData)):
    return add_images.add_produck_images(file1, product_id, color, total_product, db)


@app.post('/product/add_product_details', tags=['product'])
def add_product_detail(product: ProductDetail, db: Session = Depends(start_session), product_detail: AddData = Depends(AddData)):

    return product_detail.add_product_detail(product, db)


@app.post('/cart/add_cart', tags=['cart'])
def add_cart(file1: UploadFile = File(...), product_name: str = Form(...), price: int = Form(...), quantity: int = Form(...), r_id: int = Form(...), cart_detail: AddData = Depends(AddData)):

    return cart_detail.add_cart(file1, product_name, price, quantity, r_id)


@app.put('/cart/update_quantity', tags=['cart'])
def update_cart_quantity(details: UpdateQuantity, db: Session = Depends(start_session), update_cart: UpdateData = Depends(UpdateData)):
    return update_cart.update_cart(details, db)


@app.delete('/cart/delete', tags=['cart'])
def delete_cart(cart: DeleteCart, db: Session = Depends(start_session), delete_cart_detail: DeleteData = Depends(DeleteData)):
    return delete_cart_detail.delete_cart(cart, db)


@app.post('/place_order/in_place_order', tags=['place_order'])
def in_place_order(place_order: PlaceOrder, place_order_detail: AddData = Depends(AddData)):
    return place_order_detail.add_in_place_order(place_order)


@app.post('/delivery')
def file_upload(status:Delivery,db: Session = Depends(start_session)):
    statu = TBDelivery(delivery_type = status.delivery_type, status_id = status.status_id)
    db.add(statu)
    db.commit()
    db.refresh(statu)
    return statu

@app.get('/delivery')
def get_delivery(db: Session = Depends(start_session)):
    defd = db.query(TBStatus,TBDelivery).join(TBDelivery,TBStatus.status_id == TBDelivery.status_id).all()
    return defd