from __future__ import annotations

import asyncio
import json
import logging

from aiohttp import web
from pydantic import BaseModel

import api

logging.basicConfig(filename='.log')
loop = asyncio.get_event_loop()

app = web.Application()
ads_queue: asyncio.Queue[Ad] = asyncio.Queue()


class Ad(BaseModel):
    chat_title: str
    text: str
    photo_url: str


async def post_ad(request: web.Request):
    data = await request.json()
    ad = Ad(**json.loads(data))
    await ads_queue.put(ad)
    return web.Response(text='ok')


async def post_ads_forever():
    while True:
        ad = await ads_queue.get()

        try:
            api.post_ad(ad.chat_title, ad.text, ad.photo_url)
        except Exception as e:
            logging.exception(e)
        finally:
            await asyncio.sleep(3)


loop.create_task(post_ads_forever())
app.router.add_post('/', post_ad)
web.run_app(app, host='localhost', port=8081)
