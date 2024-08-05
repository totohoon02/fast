from fastapi import APIRouter
import fake.creature as service
router = APIRouter(prefix="/creature")


@router.get("/")
def home():
    return "creature endpoint"


@router.get("/{name}")
def get_one(name: str):
    return service.get_one(name)

