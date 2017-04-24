
import urllib.parse
import urllib.request

url = "http://www.maibiaoku.com/Trademark/lmVwlpdoa2s="

print('urlencode() :', urllib.parse.urlencode({'url': url}))
print('quote()     :', urllib.request.quote(url))
print('quote_plus():', urllib.request.quote(urllib.request.quote(url)))
