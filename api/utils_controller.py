from fastapi.routing import APIRouter

route = APIRouter(prefix="/utils", tags=["utils"])


@route.get("/health")
async def health():
    return {"message": "OK"}
