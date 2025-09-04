# BruteForce 1.0v (Subdomain Finder)

Este é um **script Python** para testar subdomínios ou caminhos em uma URL base usando uma wordlist.

---

## 📌 Funcionalidades

- Testa cada palavra da wordlist como caminho/subdomínio na URL fornecida.
- Mostra status code das respostas:
  - `200 OK` – caminho encontrado
  - `403 Forbidden` – acesso negado
  - `301/302 Redirect` – redirecionamento
- Permite informar o caminho completo da wordlist.
- Ignora erros de conexão automaticamente.

---

## ⚙️ Requisitos

- Python 3.x
- wordlist
- Biblioteca `requests`

Instale o `requests`:

```bash
pip install requests
