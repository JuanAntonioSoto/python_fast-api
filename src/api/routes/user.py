from fastapi import APIRouter
from src.schemas.user import User

router = APIRouter()

users = [
    User(name="Juan", address="Murcia", age=40, comment="test"),
    User(name="Angel", address="Alicante", age=40, comment="fdgsdf"),
    User(name="Imad", address="Paris", age=40, comment="ermwsr"),
    User(name="Taoufi", address="Paris", age=40, comment="tewarghbeazhbst"),
    User(name="Dani", address="Barcelona", age=40, comment="aedtnhaezthn"),
]


@router.get("/get_users/")
def get_users() -> list[User]:
    return users


@router.post("/create_users/")
def create_user(user: User) -> None:    
    return users.append(user)
