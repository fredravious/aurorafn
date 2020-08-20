import json

def getKeychain():
	with open('../cache/keychain.json', 'r') as f:
		return json.load(f)

def getCosmetics():
	with open('../cache/cosmetics.json', 'r') as f:
		return json.load(f)

def getBanners():
	with open('../cache/banners.json', 'r') as f:
		return json.load(f)

def getBannerColors():
	with open('../cache/colors.json', 'r') as f:
		return json.load(f)

def getVariants():
	with open('../cache/variants.json', 'r') as f:
		return json.load(f)