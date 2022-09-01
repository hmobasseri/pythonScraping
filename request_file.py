import requests as r

response = r.get('https://www.easyshopever.com')
print(response.status_code)

response.headers