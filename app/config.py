from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # General
    DEBUG: bool = Field(False, description="Run in debug mode")
    # Ethereum specifics (example)
    ETH_RPC_URL: str = Field(
        "https://mainnet.infura.io/v3/YOUR_PROJECT_ID",
        description="Ethereum JSON‑RPC endpoint"
    )
    TIMEKEEPER_ENDPOINT: str = Field(
        "http://localhost:9000",
        description="TimeKeeper OS SDK endpoint"
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
