from fastapi import APIRouter

router = APIRouter()

@router.get("/items/")
async def read_items():
    return {"message": "Items"}
