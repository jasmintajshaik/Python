import requests

response=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
all_pulls=response.json()
for i in range(len(all_pulls)):
    print(all_pulls[i]["user"]["login"])