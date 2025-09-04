import requests
import os

os.system("cls")

print("""
 __  __ ___ _  __ ___ 
|  \/  |_ _| |/ /|_ _|
| |\/| || || ' <  | | 
|_|  |_|___|_|\_\|___|
BruteForce 1.0v (Only Subdomins)\n""")
# Pede a URL base
url_base = input("Digite a URL (ex: http://localhost:8080): ").rstrip("/")

# Pede o caminho da wordlist
caminho_wordlist = input("Digite o caminho completo da wordlist: ")

# Verifica se o arquivo existe
while not os.path.exists(caminho_wordlist):
    print("❌ Wordlist não encontrada!")
    caminho_wordlist = input("Digite o caminho completo da wordlist: ")

# Carrega a wordlist
with open(caminho_wordlist, "r", encoding="utf-8") as f:
    lista = f.read().splitlines()

print(f"🔎 Testando {len(lista)} caminhos...\n")

# Testa cada caminho
for palavra in lista:
    url_teste = f"{url_base}/{palavra}"
    try:
        resposta = requests.get(url_teste, timeout=3)
        if resposta.status_code == 200:
            print(f"[200 OK] {url_teste}")
        elif resposta.status_code == 403:
            print(f"[403 Forbidden] {url_teste}")
        elif resposta.status_code in (301, 302):
            print(f"[Redirect {resposta.status_code}] {url_teste}")
    except requests.exceptions.RequestException:
        pass  # ignora erros de conexão
