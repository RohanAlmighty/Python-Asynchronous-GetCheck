import asyncio
import time
import json

from async_utils import fetch_urls


def main() -> None:
    start_time = time.time()

    try:
        with open("urls.json", "r") as json_file:
            urls = json.load(json_file)

        asyncio.run(fetch_urls(urls))

    except Exception as e:
        print(f"An Error Occurred: {e}")

    end_time = time.time()
    print(f"Total Time Taken: {round(end_time - start_time, 4)} Seconds")


if __name__ == "__main__":
    main()
