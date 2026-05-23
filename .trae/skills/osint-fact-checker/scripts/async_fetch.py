import asyncio
import aiohttp

URLS = [
]

async def fetch(session, url):
    try:
        async with session.get(url, timeout=20) as response:
            text = await response.text()
            print(f"\n==== {url} ====\n")
            print(text[:2000])
    except Exception as e:
        print(f"[ERROR] {url}: {e}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in URLS]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
