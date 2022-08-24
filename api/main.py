
from fastapi import FastAPI, Depends, UploadFile, File, Form,HTTPException
from typing import List, Optional
from passlib.context import CryptContext
from email_validator import validate_email, EmailNotValidError
from database.connection import connection, Base
from database.session import start_session
from requests import Session
from dependencies.add_data import AddData
from dependencies.login import LoginUser
from dependencies.registration import NewUser, TBRegister
from models.database.product_stock import TBProductStock
from models.database.tb_brand import TBBrand
from models.database.tb_register import TBRegister
from schemas.brand import Attribute1, BrandDetail
from schemas.cart import CartDetail
from schemas.category import CategoryDetail
from schemas.h_accessories import HAccessories
from schemas.product import Product
from schemas.product_details import ProductDetail
from schemas.register import CreateUser, Login

app = FastAPI()

Base.metadata.create_all(bind = connection)


@app.post("/auth/registeration")
def create_user(user: CreateUser, db: Session = Depends(start_session), register_detail: NewUser = Depends(NewUser)):
    return register_detail.create_user(user, db)

@app.post("/auth/login")
def login(form_data: Login, db: Session = Depends(start_session),login_detail: LoginUser = Depends(LoginUser)):
    return login_detail.login_detail(form_data,db)


@app.post('/product/brand',tags = ['product'])
def add_brand(brand: BrandDetail, db: Session = Depends(start_session), brand_detail: NewUser = Depends(NewUser)):
    return brand_detail.add_brand(brand, db)

@app.post('/product/category', tags = ['product'])
def add_category(category: CategoryDetail, db: Session = Depends(start_session), category_detail: AddData = Depends(AddData)):
    return category_detail.add_category(category,db)

@app.post('/product/add_product', tags = ['product'])
def add_product(product: Product,accessories: HAccessories, db: Session = Depends(start_session), product_detail: AddData = Depends(AddData)):

    return product_detail.add_product(product,accessories, db)


@app.get('/product/brand',tags = ['product'])
def get_brand(db: Session = Depends(start_session)):

    user1 = db.query(TBRegister, TBBrand).join(
        TBBrand, TBRegister.user_id == TBBrand.u_id).all()

    return user1



@app.post('/product/add_product_stcok', tags = ['product'] )
def add_produck_stock(product_column: str = Form(...), product_name:int = Form(...), attribute: Optional[str] = Form(None), db: Session = Depends(start_session), file1: List[UploadFile] = File(default = None)):


    list_image = []
    for i in file1:
        with open(f'images/{i.filename}',"wb") as buffer:
           buffer.write(i.file.read())
        list_image.append(i.filename)

    sql = ','.join(list_image)
    print(sql)
    print(list_image)
    # print(file1.filename)
    new = 2 * product_name
    print(new)
    if attribute != None:
        new_product_Stock = TBProductStock(attribute_name = product_column, attribute_value = attribute,p_id = product_name)
        db.add(new_product_Stock)
        db.commit()
        db.refresh(new_product_Stock)
    else:
        new_product_Stock = TBProductStock(attribute_name = product_column,p_id = product_name, attribute_value = sql)
        db.add(new_product_Stock)
        db.commit()
        db.refresh(new_product_Stock)

    return new_product_Stock

@app.post('/product/add_product_details', tags = ['product'])
def add_product_detail(product:ProductDetail,db: Session = Depends(start_session),product_detail:AddData = Depends(AddData)):
    
    return product_detail.add_product_detail(product, db)

@app.post('/cart/add_cart', tags=['cart'])
def add_cart(file1: UploadFile = File(...),product_name: str = Form(...), price: int = Form(...), quantity: int = Form(...), r_id: int = Form(...),  db: Session = Depends(start_session),cart_detail: AddData = Depends(AddData)):
    
    return cart_detail.add_cart(file1,product_name,price,quantity,r_id, db)

@app.put('/cart/update_quantity', tags=['cart'])
def add_cart(r_id: int = Form(...),  db: Session = Depends(start_session),cart_detail: AddData = Depends(AddData)):
    return 

@app.post('/place_order/in_place_order', tags=['place_order'])
def in_place_order():
    return 1