from models.movimentacao import Movimentacao
from armazenamento import obter_movimentacoes
from datetime import datetime

def ordenar_movimentacoes():

    movimentacoes = obter_movimentacoes()

    if movimentacoes is None:
        return
    
    print("\n=== ORDENAÇÃO ===")

    print("\n1 - Valor")
    print("2 - Data")
    print("3 - Categoria")

    try:

        opcao = int(
            input(
                "\nEscolha uma opção: "
            )
        )
    
    except ValueError:
        
        print("\n❌ Escolha uma opção válida.")
        return
    
    if opcao == 1:

        movimentacoes_ordenadas = sorted(
            movimentacoes,
            key=lambda movimentacao: movimentacao["valor"],
            reverse=True
        )

    elif opcao == 2:

        movimentacoes_ordenadas = sorted(
            movimentacoes,
            key=lambda movimentacao: 
                 datetime.strptime(
                    movimentacao["data"],
                    "%d/%m/%Y %H:%M:%S"
                ),
            reverse=True
        )

    elif opcao == 3:

        movimentacoes_ordenadas = sorted(
            movimentacoes,
            key=lambda movimentacao: movimentacao["categoria"]
        )

    else:
        
        print("\n❌ Opção inválida.")
        return
    
    for dados in movimentacoes_ordenadas:

        movimentacao = Movimentacao.from_dict(
            dados
        )

        movimentacao.exibir()