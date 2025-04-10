import requests
import json
from bs4 import BeautifulSoup

# URL do site com os avisos de segurança
url = "https://documentation.commvault.com/securityadvisories/"

# Fazendo a requisição HTTP para obter o conteúdo da página
response = requests.get(url)
response.raise_for_status()  # Levanta uma exceção se a requisição falhar

# Parseando o HTML com BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Criando uma lista para armazenar as vulnerabilidades
vulnerabilities = []

# Encontrando a tabela que contém os avisos de segurança
table = soup.find('table')

if table:
    # Extraindo as linhas da tabela
    rows = table.find_all('tr')
    
    # Iterando sobre as linhas e adicionando à lista
    for row in rows[1:]:  # Pulando o cabeçalho (primeira linha)
        cols = row.find_all('td')
        if len(cols) >= 3:  # Verificando se há colunas suficientes
            vulnerability = {
                "ID": cols[0].get_text(strip=True),
                "Título": cols[1].get_text(strip=True),
                "Data": cols[2].get_text(strip=True)
            }
            if cols[1].get_text(strip=True) != 'none':
                vulnerabilities.append(vulnerability)
else:
    print("Nenhuma tabela de avisos de segurança encontrada na página.")

with open("vulnerabilities.json", "w", encoding="utf-8") as f:
    json.dump(vulnerabilities, f, ensure_ascii=False, indent=4)
print("Lista salva em 'vulnerabilities.json'.")
# Exemplo de como acessar a lista
#if vulnerabilities:
#    for vuln in vulnerabilities:
#        print(f"ID: {vuln['ID']}")
#        print(f"Título: {vuln['Título']}")
#        print(f"Data: {vuln['Data']}")
#        print("-" * 50)
#else:
#    print("Nenhuma vulnerabilidade encontrada.")