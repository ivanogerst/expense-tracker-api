from pydantic import BaseModel

class ExpenseCreate(BaseModel):
    title: str
    amount: float
    user_id: int
    
class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: float
    
    class Config:
        from_attributes = True
        
        
class UserCreate(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True