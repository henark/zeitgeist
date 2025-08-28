import asyncio, json, os, time
from pathlib import Path
from fastapi import FastAPI
from tools.bus import BusClient
from tools.ledger import Ledger
from tools.github import open_pr
from planner import next_task

app = FastAPI()
ROOT = Path(__file__).parent.parent.parent
LEDGER_FILE = ROOT / "data" / "empathy-ledger.jsonl"

@app.on_event("startup")
async def start_loop():
    bus = BusClient()
    ledger = Ledger(LEDGER_FILE)
    while True:
        print("Waiting for next coherence signal...")
        coh = await bus.next_coherence()
        task = next_task(coh, ledger)

        if task:
            print(f"Task selected: {task.id}. Generating patch...")
            patch = task.generate_patch()
            print("Patch generated. Opening PR...")
            pr = open_pr(task.title, patch, task.rationale)
            ledger.append({"coh": coh, "task": task.id, "pr": pr})
            print(f"PR opened and action logged: {pr}")
        else:
            print("No task selected for this coherence signal. Continuing.")

        # Sleep to prevent busy-waiting
        await asyncio.sleep(1)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
