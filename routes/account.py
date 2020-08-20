from sanic import Blueprint
from sanic import response as res

app=Blueprint('account', '/account')

@app.route('/')
async def root(req):
	return res.text('/account !')