from fastapi import APIRouter
import fake.explorer as service

router = APIRouter(prefix="/explorer")


@router.get("/")
def home():
    return "explorer endpoint"


@router.get("/{name}")
def get_one(name: str):
    return service.get_one(name)
