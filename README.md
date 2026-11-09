# Automação de Testes E2E com Playwright e Python (POM)

[![Playwright Tests](https://github.com/charlesloesjr-cmd/playwright-course-pom/actions/workflows/playwright.yml/badge.svg)](https://github.com/charlesloesjr-cmd/playwright-course-pom/actions/workflows/playwright.yml)

Projeto de automação de testes End-to-End (E2E) utilizando **Python**, **Playwright**, **Pytest** e o padrão **Page Object Model (POM)**. Valida fluxos de uma aplicação financeira de demonstração: autenticação, Pix e contratação de empréstimos.

## Tecnologias

- Python 3.13 (versão utilizada no workflow)
- Playwright for Python
- Pytest e pytest-playwright
- pytest-html (geração de relatório HTML)
- GitHub Actions (execução automatizada dos testes)

## Como executar localmente

1. Clone o repositório e entre na pasta do projeto.
2. Crie e ative um ambiente virtual. No Windows PowerShell:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. Instale as dependências e o navegador Chromium:

   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   python -m playwright install chromium
   ```

4. Execute os testes:

   ```bash
   pytest
   ```

## Relatório HTML

O pacote `pytest-html` já está listado no `requirements.txt`. Após instalar as dependências, gere o relatório com:

```bash
pytest --html=relatorio.html --self-contained-html
```

O arquivo `relatorio.html` é gerado localmente e está excluído do Git pelo `.gitignore`.

## Cenários automatizados

| Arquivo | Cenário |
|---|---|
| `test_001_login_successful.py` | Login com sucesso |
| `test_002_fazer_pix.py` | Pix realizado, saldo atualizado e lançamento no extrato |
| `test_003_contratar_emprestimo_2000.py` | Contratação de empréstimo de R$ 2.000,00 |
| `test_004_bloquear_segundo_emprestimo.py` | Bloqueio de uma segunda contratação de empréstimo |
| `test_005_verificar_pix_acima_limite.py` | Bloqueio de Pix acima do limite configurado na aplicação de demonstração |

## Estrutura

```text
├── .github/workflows/       # Pipeline do GitHub Actions
├── pages/                   # Page Objects
├── tests/                   # Casos de teste
├── conftest.py              # Fixtures e configuração compartilhada
├── requirements.txt         # Dependências
└── .gitignore
```

## Integração contínua e traces

O GitHub Actions executa os testes em push e pull request. O Playwright está configurado com `--tracing=retain-on-failure`: os traces são preservados quando um teste falha e enviados como artefatos da execução do workflow.

Para consultar, acesse **Actions**, abra a execução desejada e procure a seção **Artifacts**. Os traces não precisam ser versionados no repositório. Para abri-los localmente, baixe o arquivo `trace.zip` e execute:

```bash
python -m playwright show-trace trace.zip
```

## Aplicação testada

Os testes utilizam o SimulaBank, uma aplicação de demonstração. Os dados e transações são fictícios; não utilize credenciais ou informações bancárias reais.
