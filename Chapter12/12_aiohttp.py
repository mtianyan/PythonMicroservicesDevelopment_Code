from aiohttp import web

"""
aiohttp & async 异步编程
"""
async def api(request):
	return web.json_response({'some': 'data'})

app = web.Application()
app.router.add_get('/api', api)
web.run_app(app)