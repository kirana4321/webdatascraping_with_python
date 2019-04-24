import re
import requests
from bs4 import BeautifulSoup


webpage = requests.get("http://www.fabpedigree.com/james/mathmen.htm")
soup = BeautifulSoup(webpage.content, 'html.parser')
tb = soup.find_all('li')
res = []
for i in tb:
    res = res+re.findall(r'">(.*?)</a>',str(i))
# print (res)
res = list(set(res))
print(res)
