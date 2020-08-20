import requests
import json

r=requests.get('https://benbotfn.tk/api/v1/cosmetics/br').json()

cosmetics=[]
variants=[]

for i in r:
	cosmetics.append({
		"name":i.get('name', ''),
		"id":i['id'],
		"backendType":i['backendType']
	})
	
	if i['variants']:
		_variants=[]
		for j in i['variants']:
			_variants.append({
				"channel":j['channel'],
				"properties":[_j.get('tag', '') for _j in j['options']]
			})
		variants.append({
			"id":i['id'],
			"vtids":[],
			"variants":_variants
		})
		
with open('cosmetics.json', 'w') as f:
	json.dump(cosmetics, f, indent='\t')
	
with open('variants.json', 'w') as f:
	json.dump(variants, f, indent='\t')