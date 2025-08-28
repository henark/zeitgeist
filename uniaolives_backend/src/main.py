from fastapi import FastAPI

from src.api.health.router import router as health_router
from src.api.depin.router import router as depin_router

app = FastAPI(
    title="UniaoLives API",
    version="0.1.0",
    description="Backend API for the UniaoLives Web3 live streaming platform.",
)

# Include routers
app.include_router(health_router, prefix="/api")
app.include_router(depin_router, prefix="/api")


@app.get("/")
async def root():
    return {"message": "UniaoLives API is running."}
