from typing import Optional
from fastapi import Depends
from backend.database.session import start_session
from requests import Session
from backend.models.database.tb_cart import TBCart

class DeleteData:
  
    def delete_cart(self,register_id: int, cart_id: Optional[int] = None, db:Session = Depends(start_session)):
         
        if cart_id != None:
            cart = db.query(TBCart).filter(TBCart.cart_id == cart_id and TBCart.r_id == register_id)
        else:
           cart = db.query(TBCart).filter(TBCart.r_id == register_id)

        cart.delete()
        db.commit()

        return "true"