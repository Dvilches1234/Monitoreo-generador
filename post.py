import requests
r = requests.post("http://localhost:5000/data", data={'i': 10, 'v': 100})
print(r.status_code, r.reason)
