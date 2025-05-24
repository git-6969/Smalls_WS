import aiohttp
import asyncio
import ssl
import requests

BOT_TOKEN = '5994386382:AAGM0b3mKFwIjXfSGHhscJCg8FCX7oIu8yM'

async def get_chat_id():
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates'
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=ssl_context) as resp:
            data = await resp.json()
            print(data)

asyncio.run(get_chat_id())


def get_chat_id():
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates'
    response = requests.get(url)
    print(response.json())

get_chat_id()