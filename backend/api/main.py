from typing import Optional
from fastapi import FastAPI, Depends, UploadFile, File, Form
from backend.database.connection import connection, Base
from backend.database.session import start_session
from requests import Session
from backend.dependencies.add_data import AddData
from backend.dependencies.delete_data import DeleteData
from backend.dependencies.get_data import GetData
from backend.dependencies.login import LoginUser
from backend.dependencies.registration import NewUser
from backend.dependencies.update_data import UpdateData
from backend.models.database.product_detail import TBProductDetail
from backend.schemas.brand import BrandDetail
from backend.schemas.category import CategoryDetail
from backend.schemas.delete_model.delete_cart import DeleteCart
from backend.schemas.h_accessories import Producti
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

Base.metadata.create_all(bind = connection)
app.add_middleware(
    CORSMiddleware,
    allow_credentials = True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/auth/registeration", tags = ['auth'])
def create_user(user: CreateUser, db: Session = Depends(start_session), register_detail: NewUser = Depends(NewUser)):
    
    return register_detail.create_user(user, db)


@app.post("/auth/login", tags = ['auth'])
def login(form_data: Login, db: Session = Depends(start_session), login_detail: LoginUser = Depends(LoginUser)):
    
    return login_detail.login_detail(form_data, db)


# Add Brand
@app.post('/brand', tags = ['brand'])
def add_brand(brand: BrandDetail, db: Session = Depends(start_session), brand_detail: NewUser = Depends(NewUser)):
    
    return brand_detail.add_brand(brand, db)

# Add Category
@app.post('/category', tags = ['category'])
def add_category(category: CategoryDetail, category_detail: AddData = Depends(AddData)):
    
    return category_detail.add_category(category)


# Add Product
@app.post('/product', tags = ['product'])
def add_product(product: Product, product_detail: AddData = Depends(AddData)):

    return product_detail.add_product(product)


# Add product details
@app.post('/product/details', tags = ['product'])
def add_product_details(product: Producti, detail: AddData = Depends(AddData)):

   return detail.add_detail(product)


# search for category , product and brand
@app.get('/product')
def search_product(search_for: str = '', name: Optional[str] = '', id: Optional[int] = None, get_product_detail: GetData = Depends(GetData)):
    return get_product_detail.get_data(search_for, name, id)


@app.post('/product/images', tags = ['product'])
def add_produck_images(file1: list[UploadFile] = File(...), product_id: int = Form(...), color: str = Form(...), total_product: int = Form(...), add_images: AddData = Depends(AddData)):

    return add_images.add_images(file1, product_id, color, total_product, db)


# add product details
@app.post('/product/details', tags = ['product'])
def add_product_detail(product: ProductDetail, db: Session = Depends(start_session), product_detail: AddData = Depends(AddData)):

    return product_detail.add_product_detail(product, db)


# add in to cart
@app.post('/cart', tags = ['cart'])
def add_in_cart(file1: UploadFile = File(...), product_name: str = Form(...), price: int = Form(...), quantity: int = Form(...), r_id: int = Form(...), cart_detail: AddData = Depends(AddData)):

    return cart_detail.add_into_cart(file1, product_name, price, quantity, r_id)


# update quantity
@app.put('/cart/quantity', tags = ['cart'])
def update_cart_quantity(details: UpdateQuantity, db: Session = Depends(start_session), update_cart: UpdateData = Depends(UpdateData)):
    return update_cart.update_cart(details, db)


# delete cart user
@app.delete('/cart', tags = ['cart'])
def delete_cart(cart: DeleteCart, db: Session = Depends(start_session), delete_cart_detail: DeleteData = Depends(DeleteData)):
    return delete_cart_detail.delete_cart(cart, db)


# add in to place order
@app.post('/place_order', tags = ['place_order'])
def add_in_placeorder(place_order: PlaceOrder, place_order_detail: AddData = Depends(AddData)):
    return place_order_detail.add_in_place_order(place_order)
