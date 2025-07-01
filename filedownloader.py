import requests

url =  'https://download.sysinternal.com/files/PSTools.zip '
r = requests.get(url , allow_redirects=True)
open('PSTools.zip' , 'wb').write(r.content)
