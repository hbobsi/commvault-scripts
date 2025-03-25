<div align="center">

# Commvault Scripts 🚀

**Uma coleção de scripts incríveis para automação no Commvault!**

![GitHub repo size](https://img.shields.io/github/repo-size/hbobsi/commvault-scripts?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/hbobsi/commvault-scripts?style=for-the-badge)
![License](https://img.shields.io/github/license/hbobsi/commvault-scripts?style=for-the-badge)

</div>

---

## 📜 Sobre o Projeto

Bem-vindo ao `commvault-scripts`! Aqui você encontra scripts práticos e eficientes para automatizar tarefas no **Commvault**, como backups, relatórios e monitoramento de jobs. Criado para simplificar a vida de administradores e entusiastas da ferramenta. Vamos tornar o gerenciamento de dados mais fácil! 😎

---

## 🛠️ Pré-requisitos

Antes de começar, certifique-se de ter:
- **Commvault** instalado (v11 ou superior) ✅
- **Python 3.8+** 🐍
- Dependências listadas (se houver):
  ```bash
  pip install -r requirements.txt
  ```
- Credenciais do Commvault configuradas 🔑

---

## 🚀 Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/hbobsi/commvault-scripts.git
   ```
2. Entre na pasta:
   ```bash
   cd commvault-scripts
   ```
3. Execute um script (exemplo):
   ```bash
   python get-client-configs.py
   ```

> **Dica:** Confira cada script nos sub-diretórios para detalhes específicos!

---

## 📋 Exemplos Práticos

### Verificar Configurações
```bash
python get-client-configs.py
```
*Retorna configurações dos clientes do Commvault e gera um relatório em CSV.*

---

## 🌟 Estrutura do Projeto

```
commvault-scripts/
├── scripts/                        # Onde a mágica acontece! ✨
│   ├── devops                      # Scripts gerais para realizar tarefas de administração no Commvault.
|   |   └── get-client-configs.py   # Consulta configurações dos clients
│   └── monitoramento-zabbix        # Scripts para monitorar o Commvault através do Zabbix
│       ├── get-commcell-info.py    # Coleta informações gerais do CommCell (nome, licença, versão, saúde) e envia para o Zabbix.
│       ├── get-failed-jobs.py      # Coleta informações sobre jobs com falha no Commvault e envia para o Zabbix para monitoramento e alertas.
│       ├── get-jobs.py             # Coleta informações sobre o status dos Jobs (concluídos, falha, etc) e envia para o Zabbix.
│       ├── get-library.py          # Coleta informações sobre as Libraries (descobre e monitora métricas) e envia para o Zabbix.
│       └── get-ma.py               # Coleta informações sobre os MediaAgents (descobre e monitora status) e envia para o Zabbix.
├── docs/                           # Documentação extra (em breve!)⌛
├── examples/                       # Exemplos de uso (em breve!) ⌛
└── README.md                       # Este arquivo! 😍
```

---

## 🤝 Como Contribuir

Quer ajudar a melhorar? Adoraria! Siga esses passos:
1. Faça um **fork** 🍴
2. Crie uma branch: `git checkout -b minha-feature`
3. Commit suas mudanças: `git commit -m "Adiciona algo legal"`
4. Envie um **Pull Request** 🚀

---

## 📝 Licença

Este projeto está sob a licença **GLP-3.0**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 💬 Contato

Dúvidas? Sugestões? Abra uma **issue** ou me encontre no GitHub como [hbobsi](https://github.com/hbobsi). Vamos conversar! 😄

<div align="center">
  
  <i>Feito por [Heitor Oliveira](https://www.credly.com/users/heitor-oliveira.e2a59c29)</i>
  
  ![Commvault Expert](https://images.credly.com/images/748e9f47-7ce8-4d7b-b6be-81bb142b2896/linkedin_thumb_image.png)

</div>
