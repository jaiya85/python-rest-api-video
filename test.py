import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 65, "name": "ping", "views": 900},
        {"likes":11, "name": "ding", "views": 33},
        {"likes": 7, "name": "yoyo", "views": 87}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.status_code)

response_del = requests.delete(BASE + "video/del/1")
print("del" + str(response_del.status_code))

response_patch = requests.patch(BASE + "video/patch/2", {"likes": 777})
print("patch" + str(response_patch.status_code))

