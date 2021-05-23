import requests

payload = {"before": open('./before1.png', 'rb'), "after": open('./after1.png', 'rb')}
resp = requests.post("http://localhost:5000/predict", files=payload)
print(resp.json())
