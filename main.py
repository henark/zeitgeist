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

async def getToken(session, query):
    url = "https://tg-bot-tap.laborx.io/api/v1/auth/validate-init/v2"
    payload = json.dumps({"initData": f"{query}", "platform": "tdesktop"})
    headers = {
        'accept': '*/*', 'accept-language': 'en-US,en;q=0.9', 'content-type': 'application/json',
        'origin': 'https://timefarm.app', 'priority': 'u=1, i', 'referer': 'https://timefarm.app/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128", "Microsoft Edge WebView2";v="128"',
        'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
    }
    retries = 3
    while retries > 0:
        try:
            resp = await session.post(url, headers=headers, data=payload)
            if resp.status_code == 200:
                return resp.json()
            else:
                print(f"getToken received status code {resp.status_code}. Retrying...")
                retries -= 1
                await asyncio.sleep(1)
        except httpx.HTTPError as e:
            print(f"Error in getToken: {e}. Retrying...")
            retries -= 1
            await asyncio.sleep(1)
    print("Failed to get token after multiple retries.")
    return None

async def getInfoUser(session, token):
    url = "https://tg-bot-tap.laborx.io/api/v1/farming/info"
    headers = {'authorization': f'Bearer {token}'}
    retries = 3
    while retries > 0:
        try:
            resp = await session.get(url, headers=headers)
            if resp.status_code == 200:
                return resp.json()
            else:
                print(f"getInfoUser received status code {resp.status_code}. Retrying...")
                retries -= 1
                await asyncio.sleep(1)
        except httpx.HTTPError as e:
            print(f"Error in getInfoUser: {e}. Retrying...")
            retries -= 1
            await asyncio.sleep(1)
    return None

async def getListTask(session, token):
    url = "https://tg-bot-tap.laborx.io/api/v1/tasks"
    headers = {'authorization': f'Bearer {token}'}
    retries = 3
    while retries > 0:
        try:
            resp = await session.get(url, headers=headers)
            if resp.status_code == 200:
                return resp.json()
            else:
                print(f"getListTask received status code {resp.status_code}. Retrying...")
                retries -= 1
                await asyncio.sleep(1)
        except httpx.HTTPError as e:
            print(f"Error in getListTask: {e}. Retrying...")
            retries -= 1
            await asyncio.sleep(1)
    return None

async def getReffInfo(session, token):
    url = "https://tg-bot-tap.laborx.io/api/v1/referral/link"
    headers = {'authorization': f'Bearer {token}'}
    retries = 3
    while retries > 0:
        try:
            resp = await session.get(url, headers=headers)
            if resp.status_code == 200:
                return resp.json()
            else:
                print(f"getReffInfo received status code {resp.status_code}. Retrying...")
                retries -= 1
                await asyncio.sleep(1)
        except httpx.HTTPError as e:
            print(f"Error in getReffInfo: {e}. Retrying...")
            retries -= 1
            await asyncio.sleep(1)
    return None

async def startFarming(session, token):
    url = "https://tg-bot-tap.laborx.io/api/v1/farming/start"
    headers = {'authorization': f'Bearer {token}', 'content-type': 'application/json'}
    retries = 3
    while retries > 0:
        try:
            resp = await session.post(url, headers=headers, data=json.dumps({}))
            if resp.status_code == 200 or resp.status_code == 403:
                return resp.json()
            else:
                print(f"startFarming received status code {resp.status_code}. Retrying...")
                retries -= 1
                await asyncio.sleep(1)
        except httpx.HTTPError as e:
            print(f"Error in startFarming: {e}. Retrying...")
            retries -= 1
            await asyncio.sleep(1)
    return None

async def finishFarming(session, token):
    url = "https://tg-bot-tap.laborx.io/api/v1/farming/finish"
    headers = {'authorization': f'Bearer {token}', 'content-type': 'application/json'}
    retries = 3
    while retries > 0:
        try:
            resp = await session.post(url, headers=headers, data=json.dumps({}))
            if resp.status_code == 200 or resp.status_code == 403:
                return resp.json()
            else:
                print(f"finishFarming received status code {resp.status_code}. Retrying...")
                retries -= 1
                await asyncio.sleep(1)
        except httpx.HTTPError as e:
            print(f"Error in finishFarming: {e}. Retrying...")
            retries -= 1
            await asyncio.sleep(1)
    return None

async def startTask(session, token, idtask):
    url = f"https://tg-bot-tap.laborx.io/api/v1/tasks/{idtask}/submissions"
    headers = {'authorization': f'Bearer {token}'}
    retries = 3
    while retries > 0:
        try:
            resp = await session.post(url, headers=headers)
            if resp.status_code == 200 or resp.status_code == 400:
                return resp.json()
            else:
                print(f"startTask received status code {resp.status_code}. Retrying...")
                retries -= 1
                await asyncio.sleep(1)
        except (httpx.HTTPError, json.decoder.JSONDecodeError) as e:
            print(f"Error in startTask: {e}. Retrying...")
            retries -= 1
            await asyncio.sleep(1)
    return None

async def claimTask(session, token, idtask):
    url = f"https://tg-bot-tap.laborx.io/api/v1/tasks/{idtask}/claims"
    headers = {'authorization': f'Bearer {token}'}
    retries = 3
    while retries > 0:
        try:
            resp = await session.post(url, headers=headers, data=json.dumps({}))
            if resp.status_code == 200 or resp.status_code == 400:
                return resp.json()
            else:
                print(f"claimTask received status code {resp.status_code}. Retrying...")
                retries -= 1
                await asyncio.sleep(1)
        except (httpx.HTTPError, json.decoder.JSONDecodeError) as e:
            print(f"Error in claimTask: {e}. Retrying...")
            retries -= 1
            await asyncio.sleep(1)
    return None

async def claimReff(session, token):
    url = "https://tg-bot-tap.laborx.io/api/v1/balance/referral/claim"
    headers = {'authorization': f'Bearer {token}', 'content-type': 'application/json'}
    retries = 3
    while retries > 0:
        try:
            resp = await session.post(url, headers=headers, data=json.dumps({}))
            if resp.status_code == 200 or resp.status_code == 403:
                return resp.json()
            else:
                print(f"claimReff received status code {resp.status_code}. Retrying...")
                retries -= 1
                await asyncio.sleep(1)
        except (httpx.HTTPError, json.decoder.JSONDecodeError) as e:
            print(f"Error in claimReff: {e}. Retrying...")
            retries -= 1
            await asyncio.sleep(1)
    return None

async def upgradeLevel(session, token):
    url = "https://tg-bot-tap.laborx.io/api/v1/me/level/upgrade"
    headers = {'authorization': f'Bearer {token}', 'content-type': 'application/json'}
    retries = 3
    while retries > 0:
        try:
            resp = await session.post(url, headers=headers, data=json.dumps({}))
            if resp.status_code == 200 or resp.status_code == 403:
                return resp.json()
            else:
                print(f"upgradeLevel received status code {resp.status_code}. Retrying...")
                retries -= 1
                await asyncio.sleep(1)
        except (httpx.HTTPError, json.decoder.JSONDecodeError) as e:
            print(f"Error in upgradeLevel: {e}. Retrying...")
            retries -= 1
            await asyncio.sleep(1)
    return None

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
