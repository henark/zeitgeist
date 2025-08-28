import httpx
import asyncio
import json
import time
import os
import datetime
from colorama import Fore, Style, init
from dotenv import load_dotenv
import ast

init()
load_dotenv()

BASE_URL = "https://tg-bot-tap.laborx.io/api/v1"

async def make_api_request(session, method: str, url: str, success_codes: list[int], headers: dict = None, data: str = None):
    func_name = url.split('/')[-1] # For logging
    retries = 3
    while retries > 0:
        try:
            if method.upper() == 'POST':
                resp = await session.post(url, headers=headers, data=data)
            else:
                resp = await session.get(url, headers=headers)

            if resp.status_code in success_codes:
                return resp.json()

            # Also return the json for expected error messages, as the original code did
            if resp.status_code in [400, 403]:
                return resp.json()

            print(f"{func_name} received status code {resp.status_code}. Retrying...")
            retries -= 1
            await asyncio.sleep(1)
        except (httpx.HTTPError, json.decoder.JSONDecodeError) as e:
            print(f"Error in {func_name}: {e}. Retrying...")
            retries -= 1
            await asyncio.sleep(1)
    print(f"Failed to get data from {func_name} after multiple retries.")
    return None

async def getToken(session, query):
    url = f"{BASE_URL}/auth/validate-init/v2"
    payload = json.dumps({"initData": f"{query}", "platform": "tdesktop"})
    headers = {
        'accept': '*/*', 'accept-language': 'en-US,en;q=0.9', 'content-type': 'application/json',
        'origin': 'https://timefarm.app', 'priority': 'u=1, i', 'referer': 'https://timefarm.app/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128", "Microsoft Edge WebView2";v="128"',
        'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
    }
    return await make_api_request(session, 'POST', url, success_codes=[200], headers=headers, data=payload)

async def getInfoUser(session, token):
    url = f"{BASE_URL}/farming/info"
    headers = {'authorization': f'Bearer {token}'}
    return await make_api_request(session, 'GET', url, success_codes=[200], headers=headers)

async def getListTask(session, token):
    url = f"{BASE_URL}/tasks"
    headers = {'authorization': f'Bearer {token}'}
    return await make_api_request(session, 'GET', url, success_codes=[200], headers=headers)

async def getReffInfo(session, token):
    url = f"{BASE_URL}/referral/link"
    headers = {'authorization': f'Bearer {token}'}
    return await make_api_request(session, 'GET', url, success_codes=[200], headers=headers)

async def startFarming(session, token):
    url = f"{BASE_URL}/farming/start"
    headers = {'authorization': f'Bearer {token}', 'content-type': 'application/json'}
    return await make_api_request(session, 'POST', url, success_codes=[200, 403], headers=headers, data=json.dumps({}))

async def finishFarming(session, token):
    url = f"{BASE_URL}/farming/finish"
    headers = {'authorization': f'Bearer {token}', 'content-type': 'application/json'}
    return await make_api_request(session, 'POST', url, success_codes=[200, 403], headers=headers, data=json.dumps({}))

async def startTask(session, token, idtask):
    url = f"{BASE_URL}/tasks/{idtask}/submissions"
    headers = {'authorization': f'Bearer {token}'}
    return await make_api_request(session, 'POST', url, success_codes=[200, 400], headers=headers)

async def claimTask(session, token, idtask):
    url = f"{BASE_URL}/tasks/{idtask}/claims"
    headers = {'authorization': f'Bearer {token}'}
    return await make_api_request(session, 'POST', url, success_codes=[200, 400], headers=headers, data=json.dumps({}))

async def claimReff(session, token):
    url = f"{BASE_URL}/balance/referral/claim"
    headers = {'authorization': f'Bearer {token}', 'content-type': 'application/json'}
    return await make_api_request(session, 'POST', url, success_codes=[200, 403], headers=headers, data=json.dumps({}))

async def upgradeLevel(session, token):
    url = f"{BASE_URL}/me/level/upgrade"
    headers = {'authorization': f'Bearer {token}', 'content-type': 'application/json'}
    return await make_api_request(session, 'POST', url, success_codes=[200, 403], headers=headers, data=json.dumps({}))

async def runGetToken():
    try:
        with open('query.txt', 'r') as qf:
            querys = qf.readlines()

        valid_tokens = []
        async with httpx.AsyncClient() as session:
            for i, query in enumerate(querys):
                query = query.strip()
                if not query:
                    continue

                print(f"Processing query {i+1}...")
                get_token = await getToken(session, query)

                if get_token and 'token' in get_token:
                    levelnow = get_token.get('info', {}).get('level')
                    token = get_token['token']
                    level = get_token.get('levelDescriptions')
                    valid_tokens.append(f"{levelnow}|{token}|{level}\n")
                    print(f"Token created for query {i+1}.")
                else:
                    print(f"Failed to create token for query {i+1}. Skipping.")

        with open('tokens.txt', 'w+') as tf:
            tf.writelines(valid_tokens)

        if valid_tokens:
            print("Create token success!")
        else:
            print("No valid tokens were created. Please check your query.txt file.")

    except FileNotFoundError:
        with open('query.txt', 'w') as qf:
            print("Fill the query.txt first!")
            qf.write("query1\nquery2\ndst...")
        exit()

async def runAll(levelnow, token, index, upgradelist):
    async with httpx.AsyncClient() as session:
        info = await getInfoUser(session, token)
        if not info: return
        list_task = await getListTask(session, token)
        if not list_task: return
        reff_info = await getReffInfo(session, token)
        if not reff_info: return

        balance = float(info.get('balance', 0))
        farming_duration = int(info.get('farmingDurationInSec', 0)/3600)
        farming_reward = info.get('farmingReward', 0)
        total_reff = reff_info.get('userCount', 0)

        status_reff = f"{Fore.GREEN}{total_reff}{Style.RESET_ALL}" if total_reff > 0 else total_reff

        start_farm = await startFarming(session, token)
        claim_farm = await finishFarming(session, token)

        status_farm = f"{Fore.YELLOW}Farming{Style.RESET_ALL}" if start_farm and 'error' in start_farm else f"{Fore.GREEN}Farming started{Style.RESET_ALL}"

        if os.getenv("AUTO_TASKS", "false").lower() in ["true", "yes", "y"]:
            status_task = f"{Fore.GREEN}On{Style.RESET_ALL}"
            for i in list_task:
                idtask = i['id']
                await startTask(session, token, idtask)
                await claimTask(session, token, idtask)
            status_task = f"{Fore.GREEN}All task completed{Style.RESET_ALL}"
        else:
            status_task = "Off"

        if os.getenv("AUTO_CLAIM_REFF", "false").lower() in ["true", "yes", "y"]:
            status_autoclaimreff = f"{Fore.GREEN}On{Style.RESET_ALL}"
            claimreff_res = await claimReff(session, token)
            if claimreff_res and 'error' in claimreff_res:
                status_autoclaimreff = f"{Fore.YELLOW}{claimreff_res['error']['message']}{Style.RESET_ALL}"
            else:
                status_autoclaimreff = f"{Fore.GREEN}Success{Style.RESET_ALL}"
        else:
            status_autoclaimreff = "Off"

        if os.getenv("AUTO_UPGRADE", "false").lower() == "true":
            status_upgrade = f"{Fore.GREEN}On{Style.RESET_ALL}"
            if isinstance(upgradelist, list):
                for i in upgradelist:
                    if isinstance(i, dict) and 'price' in i and i['price'] != -1 and i['level'] > levelnow and balance > i['price']:
                        await upgradeLevel(session, token)
        else:
            status_upgrade = "Off"

        print(f"[Account {index:02d}] | Level: {levelnow} | Balance: {Fore.GREEN}{int(balance)}{Style.RESET_ALL} | Reward: {farming_reward}/{farming_duration}h | Status: {status_farm} | Tasks: {status_task} | Auto upgrade: {status_upgrade} | Referral: {status_reff}")

async def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("Create token started")
    await runGetToken()

    refresh_interval = int(os.getenv("REFRESH_CLAIM", 3600))
    token_refresh_time = int(os.getenv("REFRESH_TOKEN", 86400))
    next_token_refresh = time.time() + token_refresh_time

    while True:
        print("\n" + Fore.CYAN + "Starting new cycle..." + Style.RESET_ALL)
        start_cycle = time.time()

        try:
            with open('tokens.txt', 'r') as tf:
                tokens = [line.strip() for line in tf.readlines() if line.strip()]
        except FileNotFoundError:
            print("tokens.txt not found. Please run token generation first.")
            break

        if not tokens:
            print("No tokens found in tokens.txt. Exiting.")
            break

        schedules = []
        for i, token_line in enumerate(tokens):
            try:
                levelnow, token, upgradelist_str = token_line.split("|", 2)
                upgradelist = ast.literal_eval(upgradelist_str)
                schedules.append(asyncio.create_task(runAll(levelnow, token, i + 1, upgradelist)))
            except (ValueError, SyntaxError) as e:
                print(f"Error parsing token line {i+1}: {e}. Skipping.")

        if schedules:
            await asyncio.gather(*schedules)

        cycle_duration = time.time() - start_cycle
        print(f"\nCycle finished in {cycle_duration:.2f} seconds.")

        if time.time() > next_token_refresh:
            print("\nRefreshing tokens...")
            await runGetToken()
            next_token_refresh = time.time() + token_refresh_time
            print("Token refresh complete.")

        remaining_time = refresh_interval - cycle_duration
        if remaining_time > 0:
            print(f"Waiting for {remaining_time:.0f} seconds before next cycle...")
            await asyncio.sleep(remaining_time)

if __name__ == "__main__":
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
