from typing import Optional
from fastapi import FastAPI, Depends, UploadFile, File, Form, Header
from backend.database.connection import connection, Base
from backend.database.session import start_session
from requests import Session
from backend.dependencies.add_data import AddData
from backend.dependencies.delete_data import DeleteData
from backend.dependencies.get_data import GetData
from backend.dependencies.login import LoginUser
from backend.dependencies.registration import NewUser
from backend.dependencies.update_data import UpdateData
from backend.schemas.address import Address
from backend.schemas.brand import BrandDetail
from backend.schemas.cart import CartDetail
from backend.schemas.category import CategoryDetail
from backend.schemas.detail import BItemDetail, Bcate, Bpro
from backend.schemas.favorite import Favorite
from backend.schemas.product_detail import ProductDetail
from backend.schemas.place_order import OrderDetail
from backend.schemas.product import Product
from backend.schemas.register import CreateUser, Login
from backend.schemas.status import Status
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


@app.post("/auth/register", tags = ['auth'])
def create_user(user: CreateUser, register_detail: NewUser = Depends(NewUser)):
    
    return register_detail.create_user(user)


@app.post("/auth/login", tags = ['auth'])
def login(user: Login, db: Session = Depends(start_session), login_detail: LoginUser = Depends(LoginUser)):
    
    return login_detail.login_detail(user, db)

@app.get("/user", tags = ['user'])
def get_user(token: str | None = Header(None), user: GetData = Depends(GetData)):
   return user.get_user_by_token(token)
        

@app.put("/user", tags = ['user'])
def forgot_password(user:Login,password_data: UpdateData = Depends(UpdateData)):
    return password_data.update_password(user)

@app.post("/user", tags = ['user'])
def add_address(address: Address, address_detail: AddData = Depends(AddData)):
    
    return address_detail.add_address(address)


# Add Brand
@app.post('/brand', tags = ['brand'])
def add_brand(brand: BrandDetail, brand_detail: NewUser = Depends(NewUser)):
    
    return brand_detail.add_brand(brand)

# Add Category
@app.post('/category', tags = ['category'])
def add_category(category: CategoryDetail, category_detail: AddData = Depends(AddData)):
    
    return category_detail.add_category(category)

@app.get('/category',tags=['category'])
def get_child_category(parent_id:int, category: GetData = Depends(GetData)):
    return category.get_cate(parent_id)


# Add Product
@app.post('/product', tags = ['product'])
def add_product(product: Product, product_detail: AddData = Depends(AddData)):

    return product_detail.add_product(product)


# search for category , product and brand
@app.get('/product')
def search_product(search_for: str = '', name: Optional[str] = '', id: Optional[int] = None, get_product_detail: GetData = Depends(GetData)):
    return get_product_detail.get_data(search_for, name, id)


@app.post('/product/images', tags = ['product'])
def add_produck_images(file1: list[UploadFile] = File(...), product_id: int = Form(...), add_images: AddData = Depends(AddData)):

    return add_images.add_images(file1, product_id)


# Add product details
@app.post('/product/details', tags = ['product'])
def product_details(product: ProductDetail, detail: AddData = Depends(AddData)):

   return detail.add_detail(product)


# add in to cart
@app.post('/cart', tags = ['cart'])
def add_in_cart(cart: CartDetail, cart_detail: AddData = Depends(AddData)):

    return cart_detail.add_into_cart(cart)


# update quantity
@app.put('/cart/quantity', tags = ['cart'])
def update_cart_quantity(details: UpdateQuantity, db: Session = Depends(start_session), update_cart: UpdateData = Depends(UpdateData)):
  
    return update_cart.update_cart(details, db)


# delete cart user
@app.delete('/cart', tags = ['cart'])
def delete_cart(register_id: int,cart_id: Optional[int] = None, db: Session = Depends(start_session), delete_cart: DeleteData = Depends(DeleteData)):
    
    return delete_cart.delete_cart(cart_id, register_id, db)


# add in to place order
@app.post('/place_order', tags = ['place_order'])
def add_in_placeorder(place_order: OrderDetail, place_order_detail: AddData = Depends(AddData)):
    return place_order_detail.add_in_place_order(place_order)

@app.post('/favorite', tags = ['favorite'])
def add_in_favorite(favorite: Favorite, detail: AddData = Depends(AddData)):
    return detail.add_favorite(favorite)

# @app.get('/favorite')
# def item(id:int,db: Session = Depends(start_session), get_product_detail: GetData = Depends(GetData)):
#     return get_product_detail.get_cate(id,db)

@app.post('/status')
def add_status(status:Status,detail: AddData = Depends(AddData)):
    return detail.add_in_status(status)

# @app.post('/pro')
# def pro(item:Bpro,detail: AddData = Depends(AddData)):
#     return detail.add_pro(item)

