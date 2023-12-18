import requests
import json

url = 'https://trader.wisniowski.pl/api/v1.0/ora/trader/zamowienia/pozycje/7881608/wylicz_cene_z_logami'
headers = {
	'Authorization' : 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjA3MDBERDc4MTIwNDVCODJFNkUwNzc1QTQ4MTI5NzFBNDM5OUI2NDQiLCJ0eXAiOiJKV1QiLCJ4NXQiOiJCd0RkZUJJRVc0TG00SGRhU0JLWEdrT1p0a1EifQ.eyJuYmYiOjE3MDE3Njc5NTIsImV4cCI6MTcwMTgwMzk1MiwiaXNzIjoiaHR0cHM6Ly9vYXV0aC53aXNuaW93c2tpLnBsIiwiYXVkIjoiaHR0cHM6Ly9vYXV0aC53aXNuaW93c2tpLnBsL3Jlc291cmNlcyIsImNsaWVudF9pZCI6ImF3cHJvLndpc25pb3dza2kucGwiLCJzdWIiOiI4MiIsImF1dGhfdGltZSI6MTcwMTc2NzY3MSwiaWRwIjoibG9jYWwiLCJwaG9uZSI6Iis0ODE4NDQ3NzQ1MiIsInByZWZlcnJlZF91c2VybmFtZSI6IncuYmFyeWN6QHdpc25pb3dza2kucGwiLCJzY29wZSI6WyJvcGVuaWQiLCJwcm9maWxlIiwiZW1haWwiLCJhd3RyYWRlciJdLCJhbXIiOlsicHdkIl19.zhlI7IkLKTWUU9y5wh_MjPIM9nAhVsHPfW-ohJtdLZF4xURpptAXfu83AqwW70PrxBl5nHTlfpEVlKpK3lyVzxUt7ARppe9wE54q0KklFN_AWDNaB5bgbmamJFTgTTCJJ9ABhTkcvXHMy8ACfsV1fQKu8_gAeqBs56btdiZTCe1T4u3X3GA7n7pkNqHC3njK7wiic0oGO1f_r89u78j-VICw0irDUc1avOmdIoz2pVcZXhhPMM1oWJ6mCjo3wCU5GkWaHUhYs5GutVFkT8g2Nrsd14iffLxNjLDz4j3ghHJOpoAque74KvYn9IitWlsjizoiBbKMCjgURy0MhY8g4Q',
	'Accept' : 'application/json'
}

response = requests.get(
	url,
	headers=headers,
	timeout = 500

)
if response.status_code == 200:
	data = response.json()
	json_formatted = json.dumps(data,indent=2)
else:
	# Jeśli wystąpił błąd, wyświetl kod odpowiedzi
	print("Błąd w pobieraniu danych. Kod odpowiedzi:", response.status_code)
with open ("zrzut.json","w") as plik:
    plik.write(json_formatted)
    