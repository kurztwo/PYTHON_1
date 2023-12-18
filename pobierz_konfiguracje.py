import requests
import json

url = 'https://trader.wisniowski.pl/api/v5/trader/pozycje-zamowien/7894878/pobierz_konfiguracje_wyrobu_z_tlumaczeniami/'
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
with open ("pobrane.json","w") as plik:
    plik.write(json_formatted)
print("status: ",data["status"])
print (data['data']['konfig']['wyrob']['ktm'])
print(data['data']['konfig']['wyrob']['nazwa'])
print(data['data']['konfig']['wersja_wyrobu'])

key_list= data["data"].keys()

print(key_list)
print (len(data['data']['konfig']['wlasciwosci_wyrobu']))
print (data['data']['konfig']['wyrob']['ktm'])
parsed_data = json.loads(data)

for key, value in parsed_data['data']['konfig']['wlasciwosci_wyrobu']['AW : NAGŁOWEK ZAMÓWIENIA - JEDN. ORG. KONTRAHENTA']['dane']['tlumaczenia']['pl'].items():
    print(f"{key}")

i=1
# print(i,data['data']['konfig']['wlasciwosci_wyrobu'])
# for i in range(len(data['data']['konfig']['wlasciwosci_wyrobu'])):

    # print(i,data['data']['konfig']['wlasciwosci_wyrobu'][0], data['data']['konfig']['wlasciwosci_wyrobu']['AW : NAGŁOWEK ZAMÓWIENIA - JEDN. ORG. KONTRAHENTA']['dane']['wartosc'])


# sum = 0
# roznica = 0
# for i in range(len(data["data"][ktm]["log"])):
	# if "[ 74 ] - if cop[CEO_OD_WYLICZONEJ] == 0 and waluta == 0" in data["data"][ktm]["log"][i]:
		# print ("-----------------")
		# print("cena_pln:",data["data"][ktm]["log"][i-2]["[ 72 ] - cenniki_op"]["cop"]["CEO_PLN"],"nazwa opcji",data["data"][ktm]["log"][i-3]["[ 114 ] - "]["wartosc_wlasciwosci"]["akronim_wlasciwosci"])
		# #print ("OPCJA",data["data"][ktm]["log"][i-3]["[ 114 ] - "])
		# print ("WWW_TXT:",data["data"][ktm]["log"][i-3]["[ 114 ] - "]["cennik_opcja[WWW_TXT]"])
		# #print (data["data"][ktm]["log"][i-3]["[ 114 ] - "]," \n")
		# sum = data["data"][ktm]["log"][i]["[ 74 ] - if cop[CEO_OD_WYLICZONEJ] == 0 and waluta == 0"]["opcje_dodatkowe"]
		# #print(data["data"][ktm]["log"][i]["[ 72 ] - cenniki_op"]["cop"]["WWL_NAZWA"])
		# print("cena opcji razem: " + str(data["data"][ktm]["log"][i]["[ 74 ] - if cop[CEO_OD_WYLICZONEJ] == 0 and waluta == 0"]["opcje_dodatkowe"]))		
	# if "[ 90 ] - cena podsumowanie" in data["data"][ktm]["log"][i]:
		# print ("cena podsumowanie: ",data["data"][ktm]["log"][i]["[ 90 ] - cena podsumowanie"])
		# print ("Elementy wchodzące w skałd ceny: ",data["data"][ktm]["log"][i])

