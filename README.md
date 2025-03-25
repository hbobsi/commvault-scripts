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
   python check_jobs.py --timeframe "24h"
   ```

> **Dica:** Confira cada script na pasta `scripts/` para detalhes específicos!

---

## 📋 Exemplos Práticos

### Verificar Jobs
```bash
python check_jobs.py --timeframe "24h"
```
*Retorna o status dos jobs das últimas 24 horas.*

### Gerar Relatório
```bash
python client_report.py --output relatorio.csv
```
*Cria um relatório em CSV com dados dos clientes.*

---

## 🌟 Estrutura do Projeto

```
commvault-scripts/
├── scripts/          # Onde a mágica acontece! ✨
│   ├── check_jobs.py    # Verifica status de jobs
│   └── client_report.py # Gera relatórios
├── docs/            # Documentação extra (em breve!)
├── examples/        # Exemplos de uso
└── README.md        # Este arquivo bonitão 😍
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

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 💬 Contato

Dúvidas? Sugestões? Abra uma **issue** ou me encontre no GitHub como [hbobsi](https://github.com/hbobsi). Vamos conversar! 😄

<div align="center">
  <i>Feito por hbobsi</i>
</div>
