"""

This Molotov script has 2 scenario
molotov 03_molotov.py -p 10 -w 200 -d 60 -qx
"""
from molotov import scenario


_API = 'http://127.0.0.1:5000'


@scenario(weight=40)
async def scenario_one(session):
    async with session.get(_API) as resp:
        res = await resp.json()
        assert res['result'] == 'OK'
        assert resp.status == 200


@scenario(weight=60)
async def scenario_two(session):
    async with session.get(_API) as resp:
        assert resp.status == 200