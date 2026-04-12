# Controle de Gastos para Usuários

## Problema Real

Muitas pessoas têm dificuldade em controlar seus gastos do dia a dia, o que pode gerar desorganização financeira, falta de controle do dinheiro e até dívidas por não saber exatamente quanto está sendo gasto.

## Solução

Uma aplicação simples via linha de comando (CLI) que permite registrar, visualizar, alterar e remover gastos, ajudando no controle financeiro de forma prática.

## Tecnologias

- Linguagem: Python  
- Testes: Pytest  
- Qualidade: Flake8 (Linting)  
- CI: GitHub Actions  

## Como usar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Rode o app:

```bash
python src/main.py
```

3. Rode os testes:

```bash
pytest
```

## Funcionalidades Principais

- Cadastro de gastos.
- Remoção de gastos (total ou parcial).
- Alteração de valores.
- Cálculo automático do total.
- Armazenamento em arquivo JSON.

---

Autor: Caio Perez  
Versão: 1.0.0  
