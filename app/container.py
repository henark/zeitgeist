from litestar import Provide
from .config import settings
from .connectors.base import BaseConnector
from .connectors.ethereum import EthereumConnector
from .connectors.bitcoin import BitcoinConnector
from .timekeeper import TimeKeeperClient

_connector_registry: dict[str, BaseConnector] = {}

def _register_builtin_connectors(timekeeper: TimeKeeperClient) -> None:
    # Register Ethereum Connector
    _connector_registry["ethereum"] = EthereumConnector(
        rpc_url=settings.ETH_RPC_URL,
        timekeeper=timekeeper
    )
    # Register Bitcoin Connector
    _connector_registry["bitcoin"] = BitcoinConnector(
        timekeeper=timekeeper
    )

async def get_connector(chain: str) -> BaseConnector | None:
    return _connector_registry.get(chain.lower())

def create_container() -> dict:
    timekeeper = TimeKeeperClient()
    _register_builtin_connectors(timekeeper)
    return {
        "timekeeper": Provide(lambda: timekeeper, sync_to_thread=False),
        "get_connector": Provide(get_connector, sync_to_thread=False)
    }
