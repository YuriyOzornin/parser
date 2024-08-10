import requests

url = 'https://gbcdn.mrgcdn.ru/uploads/asset/5560941/attachment/3d301a64e10439aca6d426e2739d6424.json'
response = requests.get(url)

if response.status_code == 200:
    with open('sem2.5.json', 'wb') as f:
        f.write(response.content)