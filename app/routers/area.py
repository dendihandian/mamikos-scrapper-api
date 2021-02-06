from fastapi import APIRouter

router = APIRouter()

@router.get("/area")
async def area_list():
    return {"message": "area list"}