
import urllib.parse
import urllib.request

url = "http://sbcx.saic.gov.cn:9080/tmois/wszhcx_getLikeCondition.xhtml?appCnName=华为终端有限公司&intCls=&paiType=0"

print('urlencode() :', urllib.parse.urlencode({'url': url}))
print('quote()     :', urllib.request.quote(url))
print('quote_plus():', urllib.request.quote(urllib.request.quote(url)))
