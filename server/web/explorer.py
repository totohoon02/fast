from fastapi import APIRouter

router = APIRouter(prefix="/explorer")


@router.get("/")
def home():
    return "explorer endpoint"
