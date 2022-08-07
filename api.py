import genshin
from fastapi import FastAPI

app = FastAPI()

cookies = {"ltuid": 119480035, "ltoken": "cnF7TiZqHAAvYqgCBoSPx5EjwezOh1ZHoqSHf7dT"}


async def get_partial(uid):
    client = genshin.Client(cookies)
    return await client.get_partial_genshin_user(uid)


async def get_full(uid):
    client = genshin.Client(cookies)
    return await client.get_full_genshin_user(uid)


async def get_abyss(uid):
    client = genshin.Client(cookies)
    user = await client.get_full_genshin_user(uid)
    abyss = user.abyss.current if user.abyss.current.floors else user.abyss.previous
    return abyss


@app.get("/")
async def read_root():
    return 200


@app.get("/partial/{uid}")
async def read_item(uid: int):
    data = await get_partial(uid)
    return {"uid": uid, "data": data}


@app.get("/full/{uid}")
async def read_item(uid: int):
    data = await get_full(uid)
    return {"uid": uid, "data": data}


@app.get("/abyss/{uid}")
async def read_item(uid: int):
    data = await get_abyss(uid)
    return {"uid": uid, "data": data}
