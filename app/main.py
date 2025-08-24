from litestar import Litestar
from .router import router
from .container import create_container

def create_app() -> Litestar:
    """Factory used by uvicorn or any ASGI server."""
    container = create_container()
    return Litestar(
        route_handlers=[router],
        dependencies=container,
        debug=True,          # toggle via config
    )

app = create_app()
