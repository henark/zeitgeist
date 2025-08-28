import uuid
from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class NodeStatus(str, Enum):
    """Enum for DePIN node status."""
    ACTIVE = "active"
    INACTIVE = "inactive"
    JAILED = "jailed"


class DePINNodeBase(BaseModel):
    """Base Pydantic model for a DePIN node."""
    owner_address: str = Field(..., description="Wallet address of the node operator.")
    location: str = Field(..., description="Geographic location of the node (e.g., 'US-East').")


class DePINNodeCreate(DePINNodeBase):
    """Model for creating a new DePIN node."""
    pass


class DePINNode(DePINNodeBase):
    """Model representing a DePIN node in the system."""
    id: uuid.UUID = Field(..., description="Unique identifier for the node.")
    status: NodeStatus = Field(default=NodeStatus.INACTIVE, description="Current status of the node.")
    uptime_percentage: float = Field(default=0.0, description="Percentage of time the node has been online.")
    bandwidth_provided_mb: float = Field(default=0.0, description="Total data relayed in megabytes.")
    last_seen_at: datetime = Field(default_factory=datetime.utcnow, description="Timestamp of the last heartbeat.")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Timestamp when the node was registered.")

    class Config:
        orm_mode = True


class NetworkStats(BaseModel):
    """Model for overall DePIN network statistics."""
    total_nodes: int = Field(..., description="Total number of registered nodes.")
    active_nodes: int = Field(..., description="Number of currently active nodes.")
    total_bandwidth_relayed_gb: float = Field(..., description="Total bandwidth relayed by the network in gigabytes.")
    unique_countries: int = Field(..., description="Number of unique countries where nodes are operating.")
