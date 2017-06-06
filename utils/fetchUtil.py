import requests
from requests.auth import HTTPBasicAuth

bauth = HTTPBasicAuth('username', 'password')

def handleListRequestInner(url, processFunc, auth=bauth):
    
    print('processing ' + url)

    result = requests.get(url,  auth=auth)

    if result.status_code != 200:
        print(result.status_code, "requests failed :", url )
        return

    respJson = result.json()

    
    if not (respJson != None and respJson['list'] != None):
        print ( "not valid json result for contents call" )
        raise
    
    for item in respJson['list']:
        processFunc(item)
    
    if 'links' in respJson and 'next' in respJson['links']:
        return respJson['links']['next']
    else :
        return None    
    

def handleListRequest(url, processFunc, auth=bauth):
    print ('starting requests')
    
    targetUrl = url
    while targetUrl != None:
        targetUrl = handleListRequestInner( targetUrl, processFunc, auth )
    
    print ('requests finished')



