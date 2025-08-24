from __future__ import annotations
import httpx
from .base import BaseConnector, BlockInfo
from ..timekeeper import TimeKeeperClient

class BitcoinConnector(BaseConnector):
    """Adapter for the Bitcoin blockchain using the blockstream.info public API."""

    def __init__(self, timekeeper: TimeKeeperClient, timeout: int = 10):
        self._api_url = "https://blockstream.info/api"
        self._client = httpx.AsyncClient(timeout=timeout)
        self._timekeeper = timekeeper

    @property
    def name(self) -> str:
        return "Bitcoin"

    async def get_latest_block(self) -> BlockInfo:
        # Step 1: Get the hash of the latest block
        tip_hash_response = await self._client.get(f"{self._api_url}/blocks/tip/hash")
        tip_hash_response.raise_for_status()
        latest_hash = tip_hash_response.text

        # Step 2: Get the full details of that block
        block_details_response = await self._client.get(f"{self._api_url}/block/{latest_hash}")
        block_details_response.raise_for_status()
        block_data = block_details_response.json()

        # Step 3: Get the current TimeKeeper chronon for temporal context
        chronon = await self._timekeeper.get_current_chronon()

        return BlockInfo(
            number=block_data["height"],
            hash=block_data["id"],
            chronon_id=chronon["id"]
        )
