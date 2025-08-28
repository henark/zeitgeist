from __future__ import annotations
import asyncio
import httpx
from .base import BaseConnector, BlockInfo
from ..timekeeper import TimeKeeperClient

class CosmosConnector(BaseConnector):
    def __init__(self, rpc_url: str, timekeeper: TimeKeeperClient, timeout: int = 10):
        self._rpc_url = rpc_url
        self._lock = asyncio.Lock()
        self._timekeeper = timekeeper
        self._timeout = timeout

    @property
    def name(self) -> str:
        return "Cosmos"

    async def get_latest_block(self) -> BlockInfo:
        async with self._lock:
            async with httpx.AsyncClient(timeout=self._timeout) as client:
                response = await client.get(f"{self._rpc_url}/status")
                response.raise_for_status()
                data = response.json()
                latest_height = int(data["result"]["sync_info"]["latest_block_height"])
                # The /status endpoint doesn't return the block hash, so we'll use a placeholder.
                # This is not ideal, but it's the best we can do with this API.
                latest_hash = data["result"]["sync_info"]["latest_block_hash"]
                chronon = await self._timekeeper.get_current_chronon()
                return BlockInfo(
                    number=latest_height,
                    hash=latest_hash,
                    chronon_id=chronon["id"]
                )
