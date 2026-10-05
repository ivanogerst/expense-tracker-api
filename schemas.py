from pydantic import BaseModel
from pydantic import ConfigDict

class ExpenseCreate(BaseModel):
    title: str
    amount: float
    user_id: int
    
class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: float
    
    model_config = ConfigDict(from_attributes=True)
        
        
class UserCreate(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str

    model_config = ConfigDict(from_attributes=True)
        

class LoginRequest(BaseModel):
    username: str
    password: str