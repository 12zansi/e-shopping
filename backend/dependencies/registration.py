
from email_validator import validate_email, EmailNotValidError
from backend.models.database.tb_brand import TBBrand
from passlib.context import CryptContext
from backend.models.database.tb_register import  TBRegister
from backend.schemas.brand import  BrandDetail
from backend.schemas.register import CreateUser
from backend.database.session import start_session
from requests import Session
from fastapi import Depends,HTTPException

class NewUser:
    
    def create_user(self, user: CreateUser, db: Session = Depends(start_session) ):
        PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
        try:
         valid = validate_email(email = user.email)
         email = valid.email
        except EmailNotValidError:
          raise HTTPException(
            status_code=404, detail="please enter a valid email")

        db_user = db.query(TBRegister).filter(TBRegister.username == user.username and TBRegister.email == user.email).first()
        if db_user:
          raise HTTPException(status_code=400, detail="username or email already exists")
        hashed_password = PWD_CONTEXT.hash(user.password)
        
        new_user = TBRegister(username = user.username, email = email, password = hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
    
    def add_brand(self, brand: BrandDetail, db: Session = Depends(start_session)):
        new_brand = TBBrand(brand_name = brand.brand_name)
        db.add(new_brand)
        db.commit()
        db.refresh(new_brand)
        return new_brand


