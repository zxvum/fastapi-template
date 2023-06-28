from fastapi import APIRouter
from starlette.responses import FileResponse

main_router = APIRouter()


@main_router.get("/")
def test():
    return FileResponse("index.html")

# Тут подключение других роутеров
