from requests import Session
from fastapi import Depends
from backend.models.database.cart import TBCart
from backend.schemas.updateModel.update_cart import UpdateQuantity
from backend.database.session import start_session


class UpdateData:

    def update_cart(self,details: UpdateQuantity, db: Session = Depends(start_session)):

        erp = db.query(TBCart).filter(TBCart.cart_id == details.cart_id).update({TBCart.quantity: details.quantity,TBCart.total_price: TBCart.product_price * details.quantity})

        db.commit()
        return erp
