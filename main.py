from fastapi import FastAPI
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from config import API_PREFIX, ALLOWED_HOSTS
from handlers.http_error import http_error_handler
from routers.api import router as router_api


def build_application() -> FastAPI:
    ''' Configure, start and return application '''
    application = FastAPI()

    application.include_router(router_api, prefix=API_PREFIX)

    application.add_exception_handler(HTTPException, http_error_handler)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return application


app = build_application()
