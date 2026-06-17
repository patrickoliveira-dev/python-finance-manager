from dashboard import mostrar_dashboard
from estatisticas import (
    mostrar_saldo,
    mostrar_estatisticas
)
from exportacao import exportar_movimentacoes
from filtros import filtrar_movimentacoes
from movimentacoes import (
    adicionar_movimentacao,
    mostrar_movimentacoes,
    editar_movimentacao,
    excluir_movimentacao
)
from ordenacao import ordenar_movimentacoes
from recorrencias import (
    listar_recorrencias,
    mostrar_proximas_ocorrencias
)

def executar_menu():

    while True:

        print("\n=== FINANCE MANAGER ===")
        print("\n1 - Adicionar movimentação")
        print("2 - Listar movimentações")
        print("3 - Mostrar saldo")
        print("4 - Editar movimentação")
        print("5 - Excluir movimentação")
        print("6 - Filtrar movimentações")
        print("7 - Ordenar movimentações")
        print("8 - Exportar movimentações")
        print("9 - Estatísticas")
        print("10 - Dashboard")
        print("11 - Listar recorrências")
        print("12 - Mostrar próximas ocorrências")
        print("13 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":

            adicionar_movimentacao()

        elif opcao == "2":

            mostrar_movimentacoes()

        elif opcao == "3":

            mostrar_saldo()
        
        elif opcao == "4":

            editar_movimentacao()

        elif opcao == "5":

            excluir_movimentacao()

        elif opcao == "6":

            filtrar_movimentacoes()

        elif opcao == "7":

            ordenar_movimentacoes()

        elif opcao == "8":

            exportar_movimentacoes()

        elif opcao == "9":

            mostrar_estatisticas()

        elif opcao == "10":

            mostrar_dashboard()

        elif opcao == "11":

            listar_recorrencias()

        elif opcao == "12":

            mostrar_proximas_ocorrencias()

        elif opcao == "13":

            print(
                "\nEncerrando programa..."
            )

            break

        else:

            print(
                "\nOpção inválida."
            )