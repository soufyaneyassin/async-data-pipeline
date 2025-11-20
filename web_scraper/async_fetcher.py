import asyncio, aiohttp




#1 walk through each link and asynchronously make a get request
async def fetch_data(session, link):
      async with session.get(link) as resp:
           return await resp.text()

async def walk_through_links(links):
    async with aiohttp.ClientSession() as session:
          tasks = [fetch_data(session, link) for link in links]
          return  await asyncio.gather(*tasks)
    
