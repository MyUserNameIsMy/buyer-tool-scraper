from fastapi import APIRouter

from routers import claires

router = APIRouter()


def include_api_routes():
    ''' Include to router all api rest routes with version prefix '''
    router.include_router(claires.router)


include_api_routes()
