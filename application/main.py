from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from application.api.routes import main_router
# config
from application.config.settings import settings

app = FastAPI()
app.include_router(main_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=settings.host, port=settings.port, workers=1, reload=True)
