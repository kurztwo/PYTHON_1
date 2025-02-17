
import json





# Przykładowy obiekt JSON
json_data = '''
{
    "name": "John",
    "dane": {
                        "lp": 0,
                        "akronim": "AW : NAGŁOWEK ZAMÓWIENIA - JEDN. ORG. KONTRqqqqAHENTA",
                        "nazwa": "AW : NAGŁOWEK ZAMÓWIENIA - JEDN. ORG. KONTRAHENTA",
                        "typ_wartosci": 0,
                        "zmienna": "awN_JO",
                        "czy_parametr": true,
                        "czy_zakres": false,
                        "czy_zaszyta": false,
                        "czy_wyliczana": false,
                        "wzor_wyliczeniowy": null,
                        "zaokraglenie": 0,
                        "czy_hurtownik": false,
                        "czy_widoczna": false,
                        "czy_zawsze_widoczna": false,
                        "wypelnia": 0,
                        "czy_inne_wart": false,
                        "czy_z_polki": false,
                        "czy_wplywa_na_wer_hand": false,
                        "kryterium": "",
                        "wartosc": "50183",
                        "wlasciwosc_z_1": null,
                        "typ_wartosci_z_1": 0,
                        "czy_zakres_z_1": false,
                        "wlasciwosc_z_2": null,
                        "typ_wartosci_z_2": 0,
                        "czy_zakres_z_2": false,
                        "wlasciwosc_z_3": null,
                        "typ_wartosci_z_3": 0,
                        "czy_zakres_z_3": false,
                        "wlasciwosc_z_4": null,
                        "typ_wartosci_z_4": 0,
                        "czy_zakres_z_4": false,
                        "wlasciwosc_z_5": null,
                        "typ_wartosci_z_5": 0,
                        "czy_zakres_z_5": false
                       
                        },
    "city": "New York",
    "tags": ["python", "json", "data"]
}
'''
kstala='90'
# Analiza danych JSON do obiektu Pythona
parsed_data = json.loads(json_data)

# Wypisanie wszystkich obiektów
for key, value in parsed_data['dane'].items():
    print(f"{key} : {value}")
    

