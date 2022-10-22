from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api.v1 import api_router
from app.config import settings
from app.core.schemas import APIException
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_STR}/openapi.json"
)

app.include_router(api_router, prefix=settings.API_STR)


@app.exception_handler(APIException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"code": exc.code, "message": exc.message},
    )
