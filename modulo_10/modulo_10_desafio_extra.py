import requests

# Configurações do TMDB
API_KEY_TMDB = "SUA_API_KEY_TMDB_AQUI"
FILME = "Inception"
URL_TMDB = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY_TMDB}&query={FILME}&language=pt-BR"

try:
    resposta_filme = requests.get(URL_TMDB, timeout=10)
    resposta_filme.raise_for_status()
    dados_filme = resposta_filme.json()
    
    # Verifica se a API retornou algum resultado válido
    if dados_filme.get("results"):
        primeiro_filme = dados_filme["results"][0]
        titulo = primeiro_filme["title"]
        sinopse = primeiro_filme["overview"]
        
        print("--- BUSCA DE FILME (DESAFIO EXTRA) ---")
        print(f"Título: {titulo}")
        print(f"Sinopse: {sinopse}")
    else:
        print(f"Nenhum filme encontrado com o nome '{FILME}'.")

except requests.exceptions.RequestException as erro:
    print(f"Erro na conexão com a API do TMDB: {erro}")
except KeyError:
    print("Erro ao processar os dados do filme recebidos.")