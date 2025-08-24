from litestar import Litestar
from .routers.connector import connector_router
from .routers.uploader import uploader_router
from .container import create_container

def create_app() -> Litestar:
    """Factory used by uvicorn or any ASGI server."""
    container = create_container()
    return Litestar(
        route_handlers=[connector_router, uploader_router],
        dependencies=container,
        debug=True,          # toggle via config
    )

app = create_app()
