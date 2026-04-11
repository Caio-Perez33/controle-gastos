import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import os
from src.main import carregar, salvar

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