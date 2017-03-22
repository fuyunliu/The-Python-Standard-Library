
import urllib.parse
import urllib.request

query_args = {'appCnName': '华为终端有限公司', 'foo': 'bar'}
encoded_args = urllib.parse.urlencode(query_args)
print('Encoded:', encoded_args)

url = 'http://localhost:8080/?' + encoded_args
print(url)
print()
print(urllib.request.quote(urllib.request.quote("华为终端有限公司")))
