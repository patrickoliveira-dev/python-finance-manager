import json
from models.movimentacao import Movimentacao
# from datetime import datetime

def salvar_movimentacao(movimentacao):
    
    nova_movimentacao = movimentacao.to_dict()

    movimentacoes = carregar_movimentacoes()

    movimentacoes.append(nova_movimentacao)

    salvar_movimentacoes(movimentacoes)

def mostrar_movimentacoes():

    movimentacoes = obter_movimentacoes()

    if movimentacoes is None:
        return
    
    print ("\n=== MOVIMENTAÇÕES ===")

    for dados in movimentacoes:

        movimentacao = Movimentacao.from_dict(
            dados
        )

        movimentacao.exibir()

def carregar_movimentacoes():

    try:

        with open(
            "dados/movimentacoes.json",
            "r",
            encoding="utf-8"
        ) as arquivo:
            
            movimentacoes = json.load(arquivo)

            return movimentacoes
        
    except FileNotFoundError:

        return []
    
    except json.JSONDecodeError:

        print(
            "\n❌ Histórico de movimentações corrompido."
        )

        return []
    
def salvar_movimentacoes(movimentacoes):

    with open(
        "dados/movimentacoes.json",
        "w",
        encoding="utf-8"
    ) as arquivo:
        
        json.dump(
            movimentacoes,
            arquivo,
            indent=4,
            ensure_ascii=False
        )

def obter_movimentacoes():

    movimentacoes = carregar_movimentacoes()

    if not movimentacoes:

        print(
            "\nNenhuma movimentação encontrada."
        )

        return None
    
    return movimentacoes

def mostrar_saldo():

    movimentacoes = obter_movimentacoes()

    if movimentacoes is None:
        return

    receitas = 0
    despesas = 0

    for movimentacao in movimentacoes:

        if movimentacao["tipo"] == "Receita":
            receitas += movimentacao["valor"]
        
        else:
            despesas += movimentacao["valor"]
    
    saldo = receitas - despesas

    print(f"\n💰 Receitas: R$ {receitas:.2f}")
    print(f"💸 Despesas: R$ {despesas:.2f}")
    print(f"📊 Saldo: R$ {saldo:.2f}")