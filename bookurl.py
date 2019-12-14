import requests
import dlbase64
import dealNode
def bookur(url):
	r = requests.get(url)



	c = dlbase64.debase64_2(r.text).decode(encoding='utf-8')
	#print(c)

	spilted = c.split('vmess://') 
	
	i=0
	for i in range(0,len(spilted)):
		k=i+1
		if(k<len(spilted)):
			dealNode.decode_v2ray(spilted[k])
			
	#print(spilted[len(spilted)])

