# import json

# data = '''
# [
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Brent"
#   }
# ]'''

# info = json.loads(data)
# print('User count:', len(info))

# for item in info:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])

import json
import urllib.request, urllib.parse, urllib.error

url = "http://py4e-data.dr-chuck.net/comments_787834.json"

ur = urllib.request.urlopen(url)
data = ur.read()

info = json.loads(data)
count = 0
for item in info["comments"]:
    # print('Name', item['name'])
    num = int(item["count"])
    count = count + num
print(count)    