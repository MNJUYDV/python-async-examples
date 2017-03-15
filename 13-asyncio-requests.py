import time
import uvloop
import asyncio
import aiohttp
import requests


search_terms = [
    "house", "flash", "game of thrones", "doctor who"
]

def sync_requests(search_terms):
    status_codes = []
    for s in search_terms:
        u = "https://google.co.in/?q=" + s
        resp = requests.get(u)
        status_codes.append(resp.text)
    return status_codes


async def fetch(url, session):
    async with session.get(url) as response:
        return await response.text()


async def async_requests(search_terms, loop=None):
    status_codes = []
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for s in search_terms:
            u = "https://google.co.in/?q=" + s
            task = asyncio.ensure_future(fetch(u, session))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)

    return status_codes


if __name__ == '__main__':

    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)

    st = time.time()
    sync_requests(search_terms)
    print("Time for Sync Requests %r sec" % ((time.time() - st)))

    st = time.time()

    future = asyncio.ensure_future(async_requests(search_terms, loop=loop))
    loop.run_until_complete(future)
    print("Time for Async Requests %r sec" % ((time.time() - st)))
