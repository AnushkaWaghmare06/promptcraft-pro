from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class userout(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True

class ProjectCreate(BaseModel):
    name: str
    description: str 

class Projectout(BaseModel):
    id: int
    name: str
    description: str
    generated_code: str

    class Config:
        orm_mode = True