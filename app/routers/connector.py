from litestar import Router, get
from litestar.exceptions import NotFoundException
from .container import get_connector
from .timekeeper import TimeKeeperClient

@get("/latest-block/{chain}")
async def latest_block(chain: str, timekeeper: TimeKeeperClient) -> dict:
    connector = await get_connector(chain.lower())
    if connector is None:
        raise NotFoundException(f"Connector for chain '{chain}' not registered")
    block = await connector.get_latest_block()
    # Corrected access to dictionary keys
    return {
        "chain": chain,
        "height": block['number'],
        "hash": block['hash'],
        "chronon_id": block['chronon_id']
    }

connector_router = Router(path="/connector", route_handlers=[latest_block])
