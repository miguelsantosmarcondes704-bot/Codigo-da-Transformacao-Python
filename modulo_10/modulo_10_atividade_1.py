import requests

# Configurações de acesso
API_KEY_WEATHER = "SUA_API_KEY_WEATHER_AQUI"
CIDADE = "Sao Paulo"
URL_WEATHER = f"https://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY_WEATHER}&units=metric&lang=pt_br"

# Realizando a requisição básica
resposta_tempo = requests.get(URL_WEATHER)
dados_tempo = resposta_tempo.json()

print("Dados recebidos com sucesso!")