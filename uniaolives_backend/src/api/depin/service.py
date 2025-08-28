import uuid
from typing import List

from .schemas import DePINNode, DePINNodeCreate


class DePINService:
    """
    Service layer for managing DePIN nodes.
    This service uses an in-memory list as a mock database.
    """

    def __init__(self):
        self._nodes: List[DePINNode] = []

    def get_all_nodes(self) -> List[DePINNode]:
        """
        Retrieves all registered DePIN nodes.
        """
        return self._nodes

    def create_node(self, node_create: DePINNodeCreate) -> DePINNode:
        """
        Creates a new DePIN node and adds it to the list.

        Args:
            node_create: The data for the new node.

        Returns:
            The newly created DePINNode object.
        """
        new_node = DePINNode(
            id=uuid.uuid4(),
            **node_create.model_dump()
        )
        self._nodes.append(new_node)
        return new_node


# Create a singleton instance of the service to be used by the router.
# In a real application, this would be handled by a dependency injection system.
depin_service = DePINService()
