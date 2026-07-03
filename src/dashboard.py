from armazenamento import obter_movimentacoes

def mostrar_dashboard():

    movimentacoes = obter_movimentacoes()

    if movimentacoes is None:
        return
    
    gastos_por_categoria = {}

    for movimentacao in movimentacoes:

        if movimentacao["tipo"] == "Despesa":

            categoria = movimentacao["categoria"]

            if categoria not in gastos_por_categoria:

                gastos_por_categoria[categoria] = 0

            gastos_por_categoria[categoria] += (
                movimentacao["valor"]
            )

    total_despesas = sum(
        gastos_por_categoria.values()
    )

    print("\n=== DASHBOARD FINANCEIRO ===\n")

    categorias_ordenadas = sorted(
        gastos_por_categoria.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for categoria, valor in categorias_ordenadas:

        percentual = (
            valor / total_despesas
        ) * 100

        barra = "█" * int(percentual / 5)

        print(
            f"{categoria:<15} "
            f"{barra:<20} "
            f"{percentual:.1f}%"
        )
    
    print(
        f"\n💸 Total de despesas: "
        f"R$ {total_despesas:.2f}"
    )