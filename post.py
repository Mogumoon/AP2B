import requests

url = "http://localhost:3000/users"
json = {
               "id" : "3",
            "name" : "Mulyon",
            "hobi" : "Musik",
            "alamat" : "Bekasi" 
}

headers = {
    "Content-Type":"application; charset=utf-8"
}

res = requests.post(url=url, json=json, headers=headers)

if res.status_code == 201:
    data = res.json()
    print(data)
else:
    print("failed to get data form API")