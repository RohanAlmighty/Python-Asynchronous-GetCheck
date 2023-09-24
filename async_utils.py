import asyncio
import aiohttp
import time

TIMEOUT = 10


async def get_url_response(session: aiohttp.ClientSession, url: str) -> str:
    try:
        start_time = time.time()

        async with session.get(url, timeout=TIMEOUT) as response:
            response_status = response.status

        end_time = time.time()

        return f"URL: '{url}' -> Done \nStatus: {response_status}, Time Taken: {round(end_time - start_time, 4)} Seconds"

    except asyncio.TimeoutError:
        return f"URL: '{url}' -> Timeout"


async def fetch_urls(urls: dict) -> None:
    async with aiohttp.ClientSession() as session:
        pending_tasks = set()

        for url in urls.values():
            pending_tasks.add(asyncio.create_task(get_url_response(session, url)))

        while len(pending_tasks) > 0:
            done_tasks, pending_tasks = await asyncio.wait(
                pending_tasks, return_when="FIRST_COMPLETED"
            )

            for done_task in done_tasks:
                print(await done_task)


if __name__ == "__main__":
    asyncio.run(fetch_urls(urls={"Flipkart": "https://www.flipkart.com"}))
