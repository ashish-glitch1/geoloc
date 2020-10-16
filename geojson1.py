import urllib.request,urllib.parse,urllib.error
import json
api_key=False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
while True:
      address=input('enter address:')
      if len(address)<1:break
      parms=dict()
      parms['address']=address
      if api_key is not False:parms['key']=api_key
      url=serviceurl+urllib.parse.urlencode(parms)
      print('retrieving',url)
      uh=urllib.request.urlopen(url)
      fh=uh.read().decode()

      try:
          js=json.loads(fh)
      except:
          js=None
      if not js or 'status' not in js or js['status']!='OK':
           print(fh)
           continue
      print(fh)                 #this also prints the json of data
      print(json.dumps(js,indent=4))#this pretty prints json
      print(len(fh))
      print(js['results'][0]['place_id'])
