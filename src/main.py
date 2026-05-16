import json
import os
import requests

ARQUIVO = "gastos.json"


def carregar():
    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, "r") as f:
        return json.load(f)


def salvar(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)


def adicionar():
    try:
        descricao = input("Descrição: ")
        valor = float(input("Valor: "))

        if valor <= 0:
            print("Valor inválido")
            return

        dados = carregar()
        dados.append({"descricao": descricao, "valor": valor})

        salvar(dados)

        print("Gasto adicionado com sucesso!")

    except Exception:
        print("Erro ao adicionar")


def listar():
    dados = carregar()

    if not dados:
        print("Nenhum gasto registrado.")
        return

    print("\n--- Lista de Gastos ---")

    for i, item in enumerate(dados):
        print(f"{i} - {item['descricao']} : R${item['valor']}")


def total():
    dados = carregar()

    soma = sum(item["valor"] for item in dados)

    print(f"\nTotal: R${soma}")


def alterar_valor():
    dados = carregar()

    if not dados:
        print("Nenhum gasto para alterar.")
        return

    listar()

    try:
        indice = int(input("Escolha o índice do gasto: "))

        if indice < 0 or indice >= len(dados):
            print("Índice inválido")
            return

        valor_remover = float(input("Quanto deseja remover desse gasto: "))

        if valor_remover <= 0:
            print("Valor inválido")
            return

        if valor_remover >= dados[indice]["valor"]:
            dados.pop(indice)
            print("Gasto removido completamente.")
        else:
            dados[indice]["valor"] -= valor_remover
            print("Valor atualizado com sucesso.")

        salvar(dados)

    except Exception:
        print("Erro na operação")


def cotacao_dolar():
    try:
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

        resposta = requests.get(url, timeout=5)

        dados = resposta.json()

        valor = dados["USDBRL"]["bid"]

        print(f"\nCotação atual do dólar: R$ {valor}")

    except Exception:
        print("Erro ao buscar cotação do dólar.")


def menu():
    while True:
        print("\n=== Controle de Gastos ===")
        print("1 - Adicionar")
        print("2 - Listar")
        print("3 - Total")
        print("4 - Alterar valor (remover parcial)")
        print("5 - Ver cotação do dólar")
        print("6 - Sair")

        op = input("Escolha: ")

        if op == "1":
            adicionar()

        elif op == "2":
            listar()

        elif op == "3":
            total()

        elif op == "4":
            alterar_valor()

        elif op == "5":
            cotacao_dolar()

        elif op == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida")


if __name__ == "__main__":
    menu()
    