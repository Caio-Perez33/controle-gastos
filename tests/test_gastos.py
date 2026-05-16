import sys
import os
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import carregar, salvar, cotacao_dolar

ARQUIVO = "gastos.json"


def limpar():
    if os.path.exists(ARQUIVO):
        os.remove(ARQUIVO)


# ✅ 1. Caso correto (caminho feliz)
def test_adicionar_gasto():
    limpar()

    dados = []
    dados.append({"descricao": "Teste", "valor": 10})

    salvar(dados)

    resultado = carregar()

    assert len(resultado) == 1
    assert resultado[0]["descricao"] == "Teste"
    assert resultado[0]["valor"] == 10


# ❌ 2. Caso inválido (arquivo inexistente)
def test_lista_vazia():
    limpar()

    resultado = carregar()

    assert resultado == []


# ⚠️ 3. Caso limite (valor zero)
def test_valor_zero():
    limpar()

    dados = [{"descricao": "Zero", "valor": 0}]

    salvar(dados)

    resultado = carregar()

    assert resultado[0]["valor"] == 0


# 🌐 4. Teste da API de cotação
def test_cotacao_dolar(capsys):
    resposta_mock = {
        "USDBRL": {
            "bid": "5.43"
        }
    }

    with patch("src.main.requests.get") as mock_get:
        mock_get.return_value.json.return_value = resposta_mock

        cotacao_dolar()

        saida = capsys.readouterr()

        assert "Cotação atual do dólar" in saida.out
        assert "5.43" in saida.out