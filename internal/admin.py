from fastapi import APIRouter

router = APIRouter()

@router.get("/admin/")
async def admin_dashboard():
    return {"message": "Admin dashboard"}
