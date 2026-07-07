import requests

url= "https://api.coingecko.com/api/v3/simple/price?ids=tether-gold,pax-gold&vs_currencies=usd&include_24hr_change=true"

response = requests.get(url)
data = response.json()
print(data)