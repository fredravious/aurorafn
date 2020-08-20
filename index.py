from sanic import Sanic
from sanic import response as res

import routes
from gv import gv

gv.exchangeCodes={}
gv.clientTokens=[]
gv.accessTokens=[]
gv.xmppClients={}
gv.parties=[]
gv.invites=[]
gv.pings=[]

app=Sanic('Server')

app.blueprint(routes.account)

@app.route('/')
async def root(req):
	return res.text('/ root !')
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000)