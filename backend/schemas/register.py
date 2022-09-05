from pydantic import BaseModel


class CreateUser(BaseModel):
     username: str
     email: str
     password: str

class Login(BaseModel):
     username: str
     password: str

class TokenData(BaseModel):
     username: str