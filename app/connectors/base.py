from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TypedDict, Any

class BlockInfo(TypedDict):
    number: int
    hash: str
    chronon_id: int

class BaseConnector(ABC):
    """Common contract all concrete connectors must satisfy."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Human‑readable name, e.g. 'Ethereum'."""

    @abstractmethod
    async def get_latest_block(self) -> BlockInfo:
        """Return the most recent block on the chain."""
        ...

    async def get_block_by_number(self, number: int) -> BlockInfo | None:
        """Retrieve a block by its height. Default implementation raises NotImplemented."""
        raise NotImplementedError(f"{self.name} does not implement get_block_by_number")

    async def get_transaction(self, tx_hash: str) -> Any:
        """Retrieve a transaction payload."""
        raise NotImplementedError(f"{self.name} does not implement get_transaction")
