from typing import Optional
from typing_extensions import Self
from backend.database.session import start_session
from requests import Session
from fastapi import Depends,Header, HTTPException, status
from jose import jwt, JWTError
from datetime import datetime,timedelta
from backend.dependencies.login import LoginUser
from backend.models.database.tb_favorite import Detail, Item, ItemDetail
from backend.models.database.tb_product import TBProduct
from backend.models.database.tb_brand import TBBrand
from backend.models.database.tb_category import TBCategory
from backend.models.database.tb_register import TBRegister
from backend.schemas.register import TokenData

# from sqlalchemy.orm import aliased


class GetData:
    def __init__(self, db: Session = Depends(start_session)):
        self.db = db
    
    def create_access_token(data: dict, expire_delta: timedelta | None = None):
        to_encode = data.copy()
        if expire_delta:
            expire = datetime.utcnow() + expire_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, LoginUser._JWT_SECRET, algorithm = LoginUser.Algorithm)
        return encoded_jwt
    
    # def authenticate(
    #         *,
    #         username: str,
    #         password: str,
    #         db: Session,

    #     ) -> Optional[TBRegister]:

    #         user = db.query(TBRegister).filter(TBRegister.username == username).first()
    #         if not user:
    #             return None
    #         if not verify_password(password, user.password):
    #             return None
    #         return user


    def get_user_by_token(self,token: str | None = Header(None)):
        credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, LoginUser._JWT_SECRET, algorithms=[LoginUser.Algorithm])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        token_data = TokenData(username = username)
        user = self.db.query(TBRegister.user_id, TBRegister.username, TBRegister.email, TBRegister.is_admin).filter(TBRegister.username == token_data.username).first()
        if user is None:
            raise credentials_exception

        return {
            "stud_id": user[0],
            "username": user[1],
            "email": user[2],
            "is_admin": user[3], }

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
            product_detail = self.db.query(TBCategory).filter(TBCategory.parent_id == 0).all()
            if name != '':
                product_detail = self.db.query(TBCategory).filter(
                    TBCategory.category_name.like(name)).all()

        elif search_for == 'brand':
            product_detail = self.db.query(TBBrand).all()

        else:
            product_detail = "please enter brand or category or product"

        return product_detail

    


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
    
    def get_cate(self,id:int):
        category = self.db.query(TBCategory).filter(TBCategory.parent_id == id).all()
        
        return category
        
