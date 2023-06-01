import aiohttp
import time
import asyncio
from get_book import get_book_request
import os

urls=[""]

async def main():
    print("test")
    async with aiohttp.ClientSession() as session:
        result=await asyncio.gather(*[get_book_request(session,url) for url in urls])
    return True
if __name__=="__main__":
    start = time.time()
    asyncio.run(main())
    print("실행시간 :", time.time() - start,"seconds")
    