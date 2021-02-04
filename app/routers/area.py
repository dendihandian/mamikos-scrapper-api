from fastapi import APIRouter

router = APIRouter()

@router.post("/area")
async def area_list():
    return {"message": "area list"}