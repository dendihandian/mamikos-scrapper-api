from fastapi import APIRouter

router = APIRouter()

@router.get("/kost")
async def kost_list():
    return {"message": "kost list"}