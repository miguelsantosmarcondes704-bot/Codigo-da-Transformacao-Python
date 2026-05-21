import requests

API_KEY_WEATHER = "SUA_API_KEY_WEATHER_AQUI"
CIDADE = "Sao Paulo"
URL_WEATHER = f"https://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY_WEATHER}&units=metric&lang=pt_br"

API_KEY_TMDB = "SUA_API_KEY_TMDB_AQUI"
FILME = "Inception"
URL_TMDB = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY_TMDB}&query={FILME}&language=pt-BR"

try:
    resposta_tempo = requests.get(URL_WEATHER, timeout=10)
    resposta_tempo.raise_for_status()
    dados_tempo = resposta_tempo.json()
    
    temperatura = dados_tempo["main"]["temp"]
    descricao = dados_tempo["weather"][0]["description"]
    
    print("--- PREVISÃO DO TEMPO ---")
    print(f"Cidade: {CIDADE}")
    print(f"Temperatura atual: {temperatura}°C")
    print(f"Condição climática: {descricao.capitalize()}\n")

except requests.exceptions.RequestException as erro:
    print(f"Erro na conexão com a API do Tempo: {erro}\n")
except KeyError:
    print("Erro ao processar os dados do tempo recebidos.\n")

try:
    resposta_filme = requests.get(URL_TMDB, timeout=10)
    resposta_filme.raise_for_status()
    dados_filme = resposta_filme.json()
    
    if dados_filme["results"]:
        primeiro_filme = dados_filme["results"][0]
        titulo = primeiro_filme["title"]
        sinopse = primeiro_filme["overview"]
        
        print("--- BUSCA DE FILME (DESAFIO EXTRA) ---")
        print(f"Título: {titulo}")
        print(f"Sinopse: {sinopse}")
    else:
        print("Nenhum filme encontrado com esse nome.")

except requests.exceptions.RequestException as erro:
    print(f"Erro na conexão com a API do TMDB: {erro}")
except KeyError:
    print("Erro ao processar os dados do filme recebidos.")