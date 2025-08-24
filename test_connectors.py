import asyncio
from app.connectors.ethereum import EthereumConnector
from app.connectors.bitcoin import BitcoinConnector
from app.timekeeper import TimeKeeperClient
from app.config import settings

async def main():
    """
    A simple test script to verify that our connectors can fetch live data.
    """
    print("Initializing connectors...")

    # Create a mock TimeKeeper client, as our connectors need it
    timekeeper_client = TimeKeeperClient()

    # Instantiate the connectors
    eth_connector = EthereumConnector(rpc_url=settings.ETH_RPC_URL, timekeeper=timekeeper_client)
    btc_connector = BitcoinConnector(timekeeper=timekeeper_client)

    print("-" * 30)
    print("Fetching latest block from Ethereum...")

    try:
        eth_block = await eth_connector.get_latest_block()
        print(f"  Chain: {eth_connector.name}")
        print(f"  Block Number: {eth_block['number']}")
        print(f"  Block Hash: {eth_block['hash']}")
        print(f"  TimeKeeper Chronon ID: {eth_block['chronon_id']}")
    except Exception as e:
        print(f"  ERROR fetching Ethereum data: {e}")

    print("-" * 30)
    print("Fetching latest block from Bitcoin (the 'oldest chain')...")

    try:
        btc_block = await btc_connector.get_latest_block()
        print(f"  Chain: {btc_connector.name}")
        print(f"  Block Number: {btc_block['number']}")
        print(f"  Block Hash: {btc_block['hash']}")
        print(f"  TimeKeeper Chronon ID: {btc_block['chronon_id']}")
    except Exception as e:
        print(f"  ERROR fetching Bitcoin data: {e}")

    print("-" * 30)
    print("Test complete.")

if __name__ == "__main__":
    asyncio.run(main())
