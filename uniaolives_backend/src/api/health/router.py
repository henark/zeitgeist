from fastapi import APIRouter

from .schemas import HealthCheck

router = APIRouter()


@router.get("/health", response_model=HealthCheck, tags=["Health"])
async def health_check():
    """
    Endpoint to check the health of the service.
    """
    return HealthCheck(status="OK")
