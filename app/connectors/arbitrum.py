from __future__ import annotations
import asyncio
from web3 import AsyncWeb3, AsyncHTTPProvider
from web3.types import BlockData
from .base import BaseConnector, BlockInfo
from ..timekeeper import TimeKeeperClient

class ArbitrumConnector(BaseConnector):
    """Adapter for the Arbitrum blockchain (EVM-compatible)."""

    def __init__(self, rpc_url: str, timekeeper: TimeKeeperClient, timeout: int = 10):
        self._w3 = AsyncWeb3(AsyncHTTPProvider(rpc_url, request_kwargs={"timeout": timeout}))
        self._lock = asyncio.Lock()
        self._timekeeper = timekeeper

    @property
    def name(self) -> str:
        return "Arbitrum"

    async def get_latest_block(self) -> BlockInfo:
        async with self._lock:
            block: BlockData = await self._w3.eth.get_block("latest")
            chronon = await self._timekeeper.get_current_chronon()
            return BlockInfo(
                number=block["number"],
                hash=block["hash"].hex(),
                chronon_id=chronon["id"]
            )
