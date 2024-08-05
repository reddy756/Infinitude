from pydantic import BaseModel
import copy
class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    nickname: str 
    address : int
