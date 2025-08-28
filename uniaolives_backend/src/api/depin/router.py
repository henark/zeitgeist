from typing import List

from fastapi import APIRouter, Depends, status

from .schemas import DePINNode, DePINNodeCreate
from .service import DePINService, depin_service

router = APIRouter()


# This function can be used with Depends to get a service instance
def get_depin_service() -> DePINService:
    return depin_service


@router.get(
    "/depin/nodes",
    response_model=List[DePINNode],
    tags=["DePIN"],
    summary="Get a list of all DePIN nodes.",
)
async def get_all_nodes(
    service: DePINService = Depends(get_depin_service)
):
    """
    Retrieves a list of all registered Decentralized Physical Infrastructure (DePIN) nodes.
    """
    return service.get_all_nodes()


@router.post(
    "/depin/nodes",
    response_model=DePINNode,
    status_code=status.HTTP_201_CREATED,
    tags=["DePIN"],
    summary="Register a new DePIN node.",
)
async def create_node(
    node_create: DePINNodeCreate,
    service: DePINService = Depends(get_depin_service)
):
    """
    Registers a new DePIN node with the network.
    """
    return service.create_node(node_create)
