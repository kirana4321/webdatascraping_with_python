"""
author: Saikiran R
date: 4/24/2019
"""
import re
import requests
from bs4 import BeautifulSoup


webpage = requests.get("http://www.fabpedigree.com/james/mathmen.htm") # Get 100 Mathematicians data

soup = BeautifulSoup(webpage.content, 'html.parser') # Parse it and find the Parent in the Tree structure using Inspect
tb = soup.find_all('li')
res = []
for i in tb:
    res = res + re.findall(r'">(.*?)</a>', str(i))

res = list(set(res))   # Get Rid of duplicates in the list by using Set
final_data = []

for i in res:
    try:
        get_wikiurl = requests.get(
            "https://en.wikipedia.org/wiki/" + str(i)) # get the data from wiki by concatenating the string object(name of the Mathematician)

        json_data = requests.get(
            "https://xtools.wmflabs.org/api/page/articleinfo/" + str(get_wikiurl.url).replace("wiki/", "").replace(
                "https://", "")).json()             # API call for Xtools to get Json data in response

        if "error" in json_data:
            final_data.append({'name': i, "pageviews": 0, "error": "not found in xtool"})
        else:
            final_data.append({'name': i, "pageviews": json_data["pageviews"]})

    except Exception as e:
        print(e)

final_res = sorted(final_data, key=lambda k: k['pageviews'])[::-1]   # Sort function to sort data in Ascending order

top_5 = {}

for i in final_res[:5]:
    # print(i)
    top_5[i["name"]] = i["pageviews"]

print(top_5)
