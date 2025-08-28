import pytest
from httpx import ASGITransport, AsyncClient

from src.main import app
from src.api.depin.service import DePINService
from src.api.depin.router import get_depin_service

# Mark all tests in this file as `anyio` tests
pytestmark = pytest.mark.anyio


@pytest.fixture(autouse=True)
def override_depin_service():
    """
    Pytest fixture to override the DePIN service dependency for each test.
    This ensures that each test function gets a fresh, isolated service instance,
    preventing state leakage between tests.
    """
    service = DePINService()
    app.dependency_overrides[get_depin_service] = lambda: service
    yield
    # Clean up the override after the test is done
    app.dependency_overrides.clear()


async def test_get_all_nodes_empty():
    """
    Tests that fetching nodes returns an empty list initially.
    """
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/api/depin/nodes")
    assert response.status_code == 200
    assert response.json() == []


async def test_create_and_get_node():
    """
    Tests creating a node and then fetching it to ensure it was created.
    """
    node_data = {
        "owner_address": "0x1234567890abcdef1234567890abcdef12345678",
        "location": "US-West"
    }

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        # POST to create a new node
        response_post = await ac.post("/api/depin/nodes", json=node_data)

        assert response_post.status_code == 201
        created_node = response_post.json()
        assert created_node["owner_address"] == node_data["owner_address"]
        assert created_node["location"] == node_data["location"]
        assert "id" in created_node
        assert "status" in created_node

        # GET to verify the node is in the list
        response_get = await ac.get("/api/depin/nodes")

        assert response_get.status_code == 200
        nodes_list = response_get.json()
        assert len(nodes_list) == 1
        assert nodes_list[0]["id"] == created_node["id"]
        assert nodes_list[0]["owner_address"] == node_data["owner_address"]
