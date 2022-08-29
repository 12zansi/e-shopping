from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, FastAPI, HTTPException, Header, status
from requests import Session
from backend.database.session import start_session
from jose import jwt, JWTError
from passlib.context import CryptContext
from backend.models.database.tb_register import  TBRegister
from backend.schemas.register import Login
class LoginUser:
    _JWT_SECRET = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    Algorithm = "HS256"
   
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return PWD_CONTEXT.verify(plain_password, hashed_password)

    def authenticate(
        *,
        username: str,
        password: str,
        db: Session,

    ) -> Optional[TBRegister]:
        user = db.query(TBRegister).filter(TBRegister.username == username).first()
        if not user:
            return None
        if not LoginUser.verify_password(password, user.password):
            return None

        return user

    def create_access_token(data: dict, expire_delta: timedelta | None = None):
        to_encode = data.copy()
        if expire_delta:
            expire = datetime.utcnow() + expire_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, LoginUser._JWT_SECRET, algorithm = LoginUser.Algorithm)
        
        return encoded_jwt

    def login_detail(self,form_data: Login, db: Session = Depends(start_session)):
        user = LoginUser.authenticate(username=form_data.username,
                            password=form_data.password, db=db)
        if not user:
            raise HTTPException(
                status_code=400, detail="incorrect username or password")
                
        access_token_expires = timedelta(minutes = LoginUser.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = LoginUser.create_access_token(
            data={"sub": user.username}, expire_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer","is_admin":user.is_admin}