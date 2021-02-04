from fastapi import APIRouter

router = APIRouter()

@router.post("/kost")
async def kost_list():
    return {"message": "kost list"}