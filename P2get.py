import requests

url = "http://localhost:3000/users"
res = requests.get(url)

if res.status_code == 200:
    data = res.json()
    print(data)
else:
    print("failed to get data form API")
    