from armazenamento import (
    obter_movimentacoes,
    salvar_movimentacoes
)
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def listar_recorrencias():

    movimentacoes = obter_movimentacoes()

    if movimentacoes is None:
        return

    print("\n=== RECORRÊNCIAS ===\n")

    movimentacoes_recorrentes = [
            movimentacao
            for movimentacao in movimentacoes
            if movimentacao.get(
                "recorrente",
                False
            ) and movimentacao.get(
                "ativa",
                True
            )
        ]
    
    if not movimentacoes_recorrentes:

        print(
            "\nNenhuma recorrência encontrada."
        )

        return
    
    for movimentacao in movimentacoes_recorrentes:

        print(
            f"ID {movimentacao['id']} | "
            f"{movimentacao['categoria']} | "
            f"{movimentacao['frequencia']}"
        )

def mostrar_proximas_ocorrencias():

    movimentacoes = obter_movimentacoes()

    if movimentacoes is None:
        return
    
    print("\n=== PRÓXIMAS OCORRÊNCIAS ===\n")

    movimentacoes_recorrentes = [
        m
        for m in movimentacoes
        if m.get("recorrente", False)
        and m.get("ativa", True)
    ]

    movimentacoes_recorrentes.sort(
        key=calcular_proxima_ocorrencia
    )

    hoje = datetime.now()

    for movimentacao in movimentacoes_recorrentes:

        proxima = calcular_proxima_ocorrencia(
            movimentacao
        )

        dias_restantes = (
            proxima.date() - hoje.date()
            ).days

        if dias_restantes == 0:
            quando = "Hoje"

        elif dias_restantes == 1:
            quando = "Amanhã"

        else:
            quando = f"Em {dias_restantes} dias"
    
        print(
            f"📅 {proxima.strftime('%d/%m/%Y')} "
            f"({quando}) | "
            f"{movimentacao['categoria']} | "
            f"{movimentacao['frequencia']} | "
            f"R$ {movimentacao['valor']:.2f}"
        )
    
    print("\n=== GERENCIAR RECORRÊNCIAS ===")
    print("\n1 - Listar recorrências")
    print("2 - Editar recorrência")
    print("3 - Ativar recorrência")
    print("4 - Desativar recorrência")
    print("5 - Voltar")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":

        print("Olá mundo!")

    elif opcao == "2":

        print("Olá mundo!")

    elif opcao == "3":

        print("Olá mundo!")
    
    elif opcao == "4":

        ativar_desativar_recorrencia()

    elif opcao == "5":

        return

    else:

        print(
            "\nOpção inválida."
        )

def calcular_proxima_ocorrencia(movimentacao):

    data_base = datetime.strptime(
        movimentacao["data"],
        "%d/%m/%Y %H:%M:%S"
    )

    frequencia = movimentacao["frequencia"]

    if frequencia == "Diária":

        proxima = data_base + timedelta(
            days=1
        )

    elif frequencia == "Semanal":

        proxima = data_base + timedelta(
            weeks=1
        )

    elif frequencia == "Mensal":

        proxima = data_base + relativedelta(
            months=1
        )
    
    elif frequencia == "Anual":

        proxima = data_base + relativedelta(
            years=1
        )
    
    return proxima

def ativar_desativar_recorrencia():

    movimentacoes = obter_movimentacoes()

    if movimentacoes is None:
        return

    print("\n=== RECORRÊNCIAS ===\n")

    movimentacoes_recorrentes = [
            movimentacao
            for movimentacao in movimentacoes
            if movimentacao.get(
                "recorrente",
                False
            )
        ]
    
    if not movimentacoes_recorrentes:

        print(
            "Nenhuma recorrência encontrada."
        )

        return
    
    for movimentacao in movimentacoes_recorrentes:

        if movimentacao.get("ativa", True):

            status = "Ativa"

        else:

            status = "Inativa"

        print(
            f"ID {movimentacao['id']} - {movimentacao['categoria']}"
            f"\nStatus: {status}"
        )

    while True:

        try:

            id_movimentacao = int(
                input("\nInforme o ID da recorrência: ")
            )

            if id_movimentacao <= 0:

                print(
                    "\n❌ O ID deve ser maior que zero."
                )

                continue

            break

        except ValueError:

            print(
                "\n❌ ID inválido."
            )

    encontrada = False

    for movimentacao in movimentacoes:

        if movimentacao["id"] == id_movimentacao:

            movimentacao["ativa"] = not movimentacao.get("ativa", True)
            encontrada = True
            break
    
    if not encontrada:
        print("\n❌ ID não encontrado.")
        return

    salvar_movimentacoes(movimentacoes)

    if movimentacao["ativa"]:

        print(
            "\n✅ Recorrência ativada com sucesso."
        )
    
    else:

        print(
            "\n✅ Recorrência desativada com sucesso."
        )