from armazenamento import obter_movimentacoes
from datetime import datetime

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

def mostrar_estatisticas():

    movimentacoes = obter_movimentacoes()

    if movimentacoes is None:
        return
    
    total_movimentacoes = len(movimentacoes)
    receitas = 0
    despesas = 0

    qtd_receitas = 0
    qtd_despesas = 0

    for movimentacao in movimentacoes:

        if movimentacao["tipo"] == "Receita":

            receitas += movimentacao["valor"]
            qtd_receitas += 1

        else:

            despesas += movimentacao["valor"]
            qtd_despesas += 1
    
    saldo = receitas - despesas

    receitas_lista = [
        m
        for m in movimentacoes
        if m["tipo"] == "Receita"
    ]

    if receitas_lista:

        maior_receita = max(
            receitas_lista,
            key=lambda movimentacao:
                movimentacao["valor"]
        )

    else:

        maior_receita = None

    despesas_lista = [
        m
        for m in movimentacoes
        if m["tipo"] == "Despesa"
    ]

    if despesas_lista:

        maior_despesa = max(
            despesas_lista,
            key=lambda movimentacao:
                movimentacao["valor"]
        )

    else:

        maior_despesa = None
    
    primeira_movimentacao = min(
        movimentacoes,
        key=lambda m:
            datetime.strptime(
                m["data"],
                "%d/%m/%Y %H:%M:%S"
            )
    )

    ultima_movimentacao = max(
        movimentacoes,
        key=lambda m:
            datetime.strptime(
                m["data"],
                "%d/%m/%Y %H:%M:%S"
            )
    )

    print("\n=== ESTATÍSTICAS ===")

    print(f"\n💰 Total de receitas: R$ {receitas:.2f}")
    print(f"💸 Total de despesas: R$ {despesas:.2f}")
    print(f"📊 Saldo atual: R$ {saldo:.2f}")

    print(f"\n📋 Total de movimentações: {total_movimentacoes}")
    print(f"📥 Quantidade de receitas: {qtd_receitas}")
    print(f"📤 Quantidade de despesas: {qtd_despesas}")

    if maior_receita:

        print(
            f"\n🏆 Maior receita:"
            f"\n{maior_receita['categoria']}"
            f"\nR$ {maior_receita['valor']:.2f}"
        )

    else:

        print(
            "\n🏆 Nenhuma receita encontrada."
        )

    if maior_despesa:

        print(
            f"\n⚠️ Maior despesa:"
            f"\n{maior_despesa['categoria']}"
            f"\nR$ {maior_despesa['valor']:.2f}"
        )

    else:

        print(
            "\n⚠️ Nenhuma despesa encontrada."
        )

    gastos_por_categoria = {}

    for movimentacao in movimentacoes:

        if movimentacao["tipo"] == "Despesa":

            categoria = movimentacao["categoria"]

            if categoria not in gastos_por_categoria:

                gastos_por_categoria[categoria] = 0

            gastos_por_categoria[categoria] += (
                movimentacao["valor"]
            )

    print("\n=== GASTOS POR CATEGORIA ===\n")

    for categoria, valor in gastos_por_categoria.items():

        percentual = (
            valor / despesas
        ) * 100

        print(
            f"💸 {categoria}: "
            f"R$ {valor:.2f} "
            f"({percentual:.1f}%)"
        )

    if gastos_por_categoria:

        maior_categoria = max(
            gastos_por_categoria,
            key=gastos_por_categoria.get
        )

        valor_maior_categoria = (
            gastos_por_categoria[
                maior_categoria
            ]
        )

        print(
            f"\n🏆 Categoria com maior gasto:"
            f"\n{maior_categoria}"
            f"\nR$ {valor_maior_categoria:.2f}"
        )

    else:

        print(
            "\n🏆 Nenhum gasto registrado."
        )

    
    print(
        f"\n🕒 Primeira movimentação: \n{primeira_movimentacao['data']}"
    )

    print(
        f"\n🕒 Última movimentação: \n{ultima_movimentacao['data']}"
    )