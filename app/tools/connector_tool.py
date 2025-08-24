from __future__ import annotations
import asyncio
from typing import Any
from .registry import Tool
from ..timekeeper import TimeKeeperClient
from ..connectors.base import BaseConnector
from ..connectors.bitcoin import BitcoinConnector
from ..connectors.ethereum import EthereumConnector
from ..connectors.arbitrum import ArbitrumConnector
from ..config import settings

class ConnectorTool(Tool):
    """
    A tool for interacting with various blockchain connectors.
    """
    name = "connector"

    def __init__(self):
        super().__init__()
        self._timekeeper = TimeKeeperClient()
        self._connectors: dict[str, BaseConnector] = self._register_connectors()
        self.actions = {
            "get_latest_block": self.get_latest_block,
        }

    def _register_connectors(self) -> dict[str, BaseConnector]:
        """Initializes and registers all available connectors."""
        connectors = {
            "bitcoin": BitcoinConnector(timekeeper=self._timekeeper),
            "ethereum": EthereumConnector(rpc_url=settings.ETH_RPC_URL, timekeeper=self._timekeeper),
            "arbitrum": ArbitrumConnector(rpc_url=settings.ARBITRUM_RPC_URL, timekeeper=self._timekeeper),
        }
        return connectors

    def get_latest_block(self, chain: str) -> dict[str, Any]:
        """
        Gets the latest block for a specified chain.
        """
        chain_lower = chain.lower()
        connector = self._connectors.get(chain_lower)

        if not connector:
            raise ValueError(f"Connector for chain '{chain}' not found.")

        # The connector methods are async, but the tool action is called synchronously.
        # We'll run the async method in a new event loop.
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        block_info = loop.run_until_complete(connector.get_latest_block())
        return block_info
