# Commvault Client Information Retrieval (Consultar Informações de Configurações de Clients)

## Overview [En]

This Python script retrieves client information from a Commvault server using its API and exports the data to a CSV file. It filters out clients with a specific type and extracts key configuration details.

## Features

- Retrieves a list of clients from the Commvault API.
- Filters out clients with a specific type (*type* 106 (Virtual Agent)).
- Fetches configuration details for each client.
- Saves the extracted data in a CSV file (`clients_info.csv`).

## Prerequisites

- Python 3.x
- Required dependencies listed in `requirements.txt`
- API access to the Commvault server
- `.env` file with the following variables:
  ```plaintext
  COMMVAULT_SERVER=<your_commvault_server>
  API_TOKEN=<your_api_token>
  ```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/hbobsi/commvault-scripts.git
   ```
2. Navigate to the project directory:
   ```bash
   cd commvault-scripts/get-client-configs
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure the `.env` file contains the correct API credentials.
2. Run the script:
   ```bash
   python script.py
   ```
3. The client information will be saved in `clients_info.csv`.

## Dependencies

- `requests`
- `python-dotenv`
- `urllib3`

## Notes

- This script disables SSL warnings (`urllib3.disable_warnings`) due to the use of self-signed certificates in some environments.
- Ensure that the API token has the required permissions to retrieve client details.

## License

This project is licensed under the GLP-3.0 License. See `LICENSE` for details.

## Visão Geral [Br]
Este script em Python recupera informações de clientes de um servidor Commvault usando sua API e exporta os dados para um arquivo CSV. Ele filtra clientes com um tipo específico e extrai detalhes de configuração chave.

## Funcionalidades
- Recupera uma lista de clientes da API do Commvault.
- Filtra clientes com um tipo específico (_type_ 106 (Virtual Agent)).
- Obtém detalhes de configuração para cada cliente.
- Salva os dados extraídos em um arquivo CSV (`clients_info.csv`).

## Pré-requisitos
- Python 3.x
- Dependências listadas em `requirements.txt`
- Acesso à API do servidor Commvault
- Arquivo `.env` com as seguintes variáveis:
  ```plaintext
  COMMVAULT_SERVER=<seu_servidor_commvault>
  API_TOKEN=<seu_token_api>
  ```

## Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/hbobsi/commvault-getConfigClients.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd commvault-scripts/get-client-configs
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso
1. Certifique-se de que o arquivo `.env` contém as credenciais corretas da API.
2. Execute o script:
   ```bash
   python script.py
   ```
3. As informações dos clientes serão salvas em `clients_info.csv`.

## Dependências
- `requests`
- `python-dotenv`
- `urllib3`

## Notas
- Este script desativa avisos de SSL (`urllib3.disable_warnings`) devido ao uso de certificados autoassinados em alguns ambientes.
- Certifique-se de que o token da API possui as permissões necessárias para recuperar detalhes dos clientes.

## Licença
Este projeto é licenciado sob a Licença GLP-3.0. Consulte `LICENSE` para mais detalhes.

