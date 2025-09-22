import requests
from datetime import datetime

def get_previsao(lat,lon):
    url= (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        "&hourly=temperatura_2m,precipitation,windspeed_10m"
        "&current_weather=true"
        "&timezone-auto"
    )

    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = requests.json()

        #Clima atual
        tempo_atual = dados.get("current_weather", {})
        temp_atual = tempo_atual.get("temperature")
        vento_atual = tempo_atual.get("windspeed")
        hora_atual = tempo_atual.get("time")

        print("=== TEMPO AGORA ===")
        print(f"Hora: {hora_atual}")
        print(f"Temperatura: {temp_atual} °C")
        print(f"Vento: {vento_atual}Km/h")
        print()

        else:
            print("Erro ao buscar previsão",resposta.status_code)

if__name__ == "__main__":
#Coordenadas de Campinas-SP
latitude = -22.9056
longitude = -47.0608
get_previsao(latitude, longitude)