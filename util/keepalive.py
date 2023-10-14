# .
# Please Don't remove credit.
# 
#Share Us R_MvzZ 
# 🥰  Thank you for giving me r  🥰
# for any error please contact me -> Telegram:- @R_MvzZ Join:- @REQUEST_MOvizZ 
# rip paid developers 🤣 - >> No need to Join telegram:- @R_MvzZ 😍😍
import asyncio
import logging
import aiohttp
import traceback
from info import *


async def ping_server():
    sleep_time = PING_INTERVAL
    while True:
        await asyncio.sleep(sleep_time)
        try:
            async with aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=10)
            ) as session:
                async with session.get(URL) as resp:
                    logging.info("Pinged server with response: {}".format(resp.status))
        except TimeoutError:
            logging.warning("Couldn't connect to the site URL..!")
        except Exception:
            traceback.print_exc()
