import requests

API_KEY_WEATHER = "SUA_API_KEY_WEATHER_AQUI"
CIDADE = "Sao Paulo"
URL_WEATHER = f"https://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY_WEATHER}&units=metric&lang=pt_br"

try:
    # timeout previne que o código trave indefinidamente em conexões lentas
    resposta_tempo = requests.get(URL_WEATHER, timeout=10)
    resposta_tempo.raise_for_status() # Dispara erro se o status HTTP não for 200
    dados_tempo = resposta_tempo.json()
    
    temperatura = dados_tempo["main"]["temp"]
    descricao = dados_tempo["weather"][0]["description"]
    
    print("--- PREVISÃO DO TEMPO ---")
    print(f"Cidade: {CIDADE}")
    print(f"Temperatura atual: {temperatura}°C")
    print(f"Condição climática: {descricao.capitalize()}")

except requests.exceptions.RequestException as erro:
    print(f"Erro na conexão com a API do Tempo: {erro}")
except KeyError:
    print("Erro ao processar os dados do tempo recebidos (chave não encontrada).")