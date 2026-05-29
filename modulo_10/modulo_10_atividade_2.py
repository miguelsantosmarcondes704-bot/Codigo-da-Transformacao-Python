import requests

API_KEY_WEATHER = "SUA_API_KEY_WEATHER_AQUI"
CIDADE = "Sao Paulo"
URL_WEATHER = f"https://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY_WEATHER}&units=metric&lang=pt_br"

resposta_tempo = requests.get(URL_WEATHER)
dados_tempo = resposta_tempo.json()

# Filtrando e extraindo as informações específicas
temperatura = dados_tempo["main"]["temp"]
descricao = dados_tempo["weather"][0]["description"]

# Exibição organizada
print("--- PREVISÃO DO TEMPO ---")
print(f"Cidade: {CIDADE}")
print(f"Temperatura atual: {temperatura}°C")
print(f"Condição climática: {descricao.capitalize()}")