import json

def carregar_movimentacoes():

    try:

        with open(
            "dados/movimentacoes.json",
            "r",
            encoding="utf-8"
        ) as arquivo:
            
            movimentacoes = json.load(arquivo)

            for movimentacao in movimentacoes:

                movimentacao.setdefault(
                    "recorrente",
                    False
                )

                movimentacao.setdefault(
                    "frequencia",
                    None
                )

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

def salvar_movimentacao(movimentacao):
    
    nova_movimentacao = movimentacao.to_dict()

    movimentacoes = carregar_movimentacoes()

    movimentacoes.append(nova_movimentacao)

    salvar_movimentacoes(movimentacoes)

def obter_movimentacoes():

    movimentacoes = carregar_movimentacoes()

    if not movimentacoes:

        print(
            "\nNenhuma movimentação encontrada."
        )

        return None
    
    return movimentacoes