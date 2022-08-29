from backend.database.session import start_session
from requests import Session
from fastapi import Depends,UploadFile,File,Form
from backend.models.database.cart import TBCart
from backend.schemas.delete_model.delete_cart import DeleteCart

class DeleteData:
    def delete_cart(self,delete_cart:DeleteCart,db:Session = Depends(start_session)):
         if delete_cart.cart_id != 0:
            cart = db.query(TBCart).filter(TBCart.cart_id == delete_cart.cart_id and TBCart.r_id == delete_cart.r_id)
         else:
           cart = db.query(TBCart).filter(TBCart.r_id == delete_cart.r_id)
         cart.delete()
         db.commit()
         return "delete"