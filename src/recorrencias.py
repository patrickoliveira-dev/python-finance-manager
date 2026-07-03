from src.armazenamento import (
    obter_movimentacoes,
    salvar_movimentacoes
)
from src.movimentacoes import (
    mostrar_lista_movimentacoes,
    escolher_movimentacao,
    escolher_categoria,
    escolher_frequencia
)
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def menu_recorrencias():

    while True:

        print("\n=== GERENCIAR RECORRÊNCIAS ===\n")
        print("1 - Listar recorrências")
        print("2 - Editar recorrência")
        print("3 - Ativar/Desativar recorrência")
        print("4 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":

            listar_recorrencias()

        elif opcao == "2":

            editar_recorrencias()

        elif opcao == "3":

            definir_recorrencia_ativa()

        elif opcao == "4":

            return

        else:

            print(
                "\nOpção inválida."
            )

def listar_recorrencias():

    recorrencias = obter_recorrencias()

    if recorrencias is None:
        return

    mostrar_lista_movimentacoes(recorrencias)
    
def editar_recorrencias():

    recorrencias = obter_recorrencias()

    if recorrencias is None:
        return

    mostrar_lista_movimentacoes(recorrencias)

def definir_recorrencia_ativa(movimentacao, ativa):

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

        status = (
            "Ativa"
            if movimentacao.get("ativa", True)
            else "Inativa"
        )

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

    for movimentacao in movimentacoes_recorrentes:

        if movimentacao["id"] == id_movimentacao:

            movimentacao["ativa"] = not movimentacao.get("ativa", True)
            encontrada = True
            break
    
    if not encontrada:
        print("\n❌ ID não encontrado.")
        return

    salvar_movimentacoes(movimentacoes)

    print (
        "\n✅ Recorrência ativada com sucesso."
        if movimentacao["ativa"]
        else "\n✅ Recorrência desativada com sucesso."
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

def obter_recorrencias():

    movimentacoes = obter_movimentacoes()

    if movimentacoes is None:
        return None

    return [
        movimentacao
        for movimentacao in movimentacoes
        if movimentacao.get("recorrente", False)
        and movimentacao.get("ativa", True)
    ]

def escolher_recorrencia():

    recorrencias = obter_recorrencias()

    if recorrencias is None:
        return None

    indice = escolher_movimentacao(recorrencias)

    if indice is None:
        return None

    return recorrencias, indice