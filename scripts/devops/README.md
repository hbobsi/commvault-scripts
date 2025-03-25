# Documentação dos scripts e como utilizá-los

## Script (get-client-configs.py)
```
Visão Geral [Br]
Este script em Python recupera informações de clientes de um servidor Commvault usando sua API e exporta os dados para um arquivo CSV. Ele filtra clientes com um tipo específico e extrai detalhes de configuração chave.

Funcionalidades
- Recupera uma lista de clientes da API do Commvault.
- Filtra clientes com um tipo específico (_type_ 106 (Virtual Agent)).
- Obtém detalhes de configuração para cada cliente.
- Salva os dados extraídos em um arquivo CSV (`clients_info.csv`).
```

