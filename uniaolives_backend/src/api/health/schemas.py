from pydantic import BaseModel


class HealthCheck(BaseModel):
    """Response model for the health check endpoint."""
    status: str = "OK"
