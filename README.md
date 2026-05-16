# Controle de Gastos para Usuários

## Problema Real

Muitas pessoas têm dificuldade em controlar seus gastos do dia a dia, o que pode gerar desorganização financeira, falta de controle do dinheiro e até dívidas por não saber exatamente quanto está sendo gasto.

## Solução

Uma aplicação simples via linha de comando (CLI) que permite registrar, visualizar, alterar e remover gastos, ajudando no controle financeiro de forma prática.

Nesta etapa intermediária foi adicionada uma integração com API pública para consulta da cotação atual do dólar em relação ao real.

## Tecnologias

- Linguagem: Python
- Testes: Pytest
- Qualidade: Flake8 (Linting)
- CI: GitHub Actions
- API Pública: AwesomeAPI

## API Utilizada

A aplicação consome a API pública AwesomeAPI para buscar a cotação atual do dólar:

https://economia.awesomeapi.com.br/json/last/USD-BRL

## Como usar

### 1. Instale as dependências

```bash
pip install -r requirements.txt
```

### 2. Rode o aplicativo

```bash
python src/main.py
```

### 3. Rode os testes

```bash
pytest
```

### 4. Verifique o lint

```bash
flake8
```

## Funcionalidades Principais

- Cadastro de gastos.
- Remoção de gastos (total ou parcial).
- Alteração de valores.
- Cálculo automático do total.
- Armazenamento em arquivo JSON.
- Consulta da cotação atual do dólar via API pública.

## Entrega Intermediária

Nesta entrega foram implementados:

- Integração com API pública de cotação do dólar.
- Teste automatizado da integração utilizando mock.
- Workflow de CI com GitHub Actions.
- Desenvolvimento em branch dedicada (`entrega-intermediaria`).
- Controle de demanda utilizando GitHub Issues.
- Pull Request para integração com a branch principal.

---

Autor: Caio de Almeida Perez  
Versão: 1.1.0
