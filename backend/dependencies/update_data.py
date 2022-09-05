from requests import Session
from fastapi import Depends
from backend.models.database.tb_cart import TBCart
from backend.models.database.tb_register import TBRegister
from backend.schemas.register import Login
from backend.schemas.updateModel.update_cart import UpdateQuantity
from backend.database.session import start_session
from passlib.context import CryptContext

class UpdateData:
    def __init__(self, db: Session = Depends(start_session)):
        self.db = db

    def update_password(self,user: Login):

        PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
        hashed_password = PWD_CONTEXT.hash(user.password)
        self.db.query(TBRegister).filter(TBRegister.username == user.username).update({TBRegister.password: hashed_password})

    #    db.add(user_obj)
        self.db.commit()
        return {"message": "student successfully updated"}



    def update_cart(self,details: UpdateQuantity):

        erp = self.db.query(TBCart).filter(TBCart.cart_id == details.cart_id).update({TBCart.quantity: details.quantity,TBCart.total_price: TBCart.product_price * details.quantity})

        self.db.commit()
        return erp
