from models.movimentacao import Movimentacao

from movimentacoes import (
    salvar_movimentacao,
    mostrar_movimentacoes,
    mostrar_saldo
)

while True:

    print("\n=== FINANCE MANAGER ===")
    print("\n1 - Adicionar movimentação")
    print("2 - Listar movimentações")
    print("3 - Mostrar saldo")
    print("4 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":

        tipo = input(
            "\nTipo (Receita/Despesa): "
        )

        valor = float(
            input(
                "\nValor: "
            )
        )

        categoria = input(
            "\nCategoria: "
        )

        descricao = input(
            "\nDescrição: "
        )

        movimentacao = Movimentacao(
            tipo,
            valor,
            categoria,
            descricao
        )

        salvar_movimentacao(
            movimentacao
        )

        print(
            "\n✅ Movimentação adicionada."
        )

    elif opcao == "2":

        mostrar_movimentacoes()

    elif opcao == "3":

        mostrar_saldo()
    
    elif opcao == "4":

        print(
            "\nEncerrando programa..."
        )

        break

    else:

        print(
            "\nOpção inválida."
        )