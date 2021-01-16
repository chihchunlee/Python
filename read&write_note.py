
with open("test.txt", "r", encoding="utf-8") as fp:

read()
readline()
readlines()

r rb
w wb
a

ast.literal_eval(data)#字串轉字典

rstrip('\n')#去除右邊字元

json.load(file)

from urllib.parse import urlparse
from urllib.request import urlopen

domin = "{}://{}".format(urlparse(url).scheme, urlparse(url).hostname)
print(domin+t)

img = urlopen(url)


find_all('span', {'id':'xxx'})

import requests
import hashlib

r = requests.get('http://target.web.site.page')
sig = hashlib.md5(r.text.encode('utf-8')).hexdigest()


