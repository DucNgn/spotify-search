import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from v1.routers.v1_main import v1_router

from config import NAME, HOST, PORT, VERSION


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=NAME,
        version=VERSION,
        description="An API service to retrive Spotify Music",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def add_test_endpoint(app: FastAPI):
    @app.get("/")
    async def home():
        return {
            "message": "Welcome to Spotify Search API!. Go to endpoint /docs to access the interactive documentation."
        }


def create_app():
    """
    Create the FastAPI instance and attach routers.
    """
    app = FastAPI()
    app.openapi = custom_openapi
    add_test_endpoint(app)
    app.include_router(v1_router)

    return app


if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host=HOST, port=PORT)
