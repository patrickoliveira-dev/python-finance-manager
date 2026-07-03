from models.movimentacao import Movimentacao
from armazenamento import obter_movimentacoes
from movimentacoes import escolher_categoria

def filtrar_movimentacoes():

    movimentacoes = obter_movimentacoes()

    if movimentacoes is None:
        return
    
    print("\n=== FILTROS ===")

    print("\n1 - Todas")
    print("2 - Receitas")
    print("3 - Despesas")
    print("4 - Categoria")

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

        movimentacoes_filtradas = movimentacoes

    elif opcao == 2:

        movimentacoes_filtradas = [
            movimentacao
            for movimentacao in movimentacoes
            if movimentacao["tipo"] == "Receita"
        ]
    
    elif opcao == 3:

        movimentacoes_filtradas = [
            movimentacao
            for movimentacao in movimentacoes
            if movimentacao["tipo"] == "Despesa"
        ]
    
    elif opcao == 4:

        print("\nDeseja filtrar receitas ou despesas?")
        print("1 - Receita")
        print("2 - Despesa")

        tipo = input("\nEscolha uma opção: ")

        if tipo == "1":
            tipo = "Receita"
        elif tipo == "2":
            tipo = "Despesa"
        else:
            print("\n❌ Tipo inválido.")
            return

        categoria = escolher_categoria(tipo)
        if categoria is None:
            return

        movimentacoes_filtradas = [
            m for m in movimentacoes
            if m["tipo"] == tipo and m["categoria"] == categoria
        ]
    
    else:

        print(
            "\nOpção inválida."
        )

        return
    
    if not movimentacoes_filtradas:

        print(
            "\nNenhuma movimentação encontrada."
        )

        return
    
    for dados in movimentacoes_filtradas:

        movimentacao = Movimentacao.from_dict(
            dados
        )

        movimentacao.exibir()