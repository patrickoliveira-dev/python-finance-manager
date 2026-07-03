from armazenamento import obter_movimentacoes

def exportar_movimentacoes():

    movimentacoes = obter_movimentacoes()

    if movimentacoes is None:
        return

    receitas, despesas = 0, 0

    for movimentacao in movimentacoes:

        if movimentacao["tipo"] == "Receita":
            receitas += movimentacao["valor"]
        
        else:
            despesas += movimentacao["valor"]
        
    saldo = receitas - despesas
    
    with open(
        "relatorio_financeiro.txt",
        "w",
        encoding="utf-8"
    ) as arquivo:        

        arquivo.write(f"\n💰 Receitas: R$ {receitas:.2f}\n")
        arquivo.write(f"💸 Despesas: R$ {despesas:.2f}\n")
        arquivo.write(f"📊 Saldo: R$ {saldo:.2f}\n")
        arquivo.write(
                "\n" + "=" * 40 + "\n\n"
            )

        for dados in movimentacoes:

            arquivo.write(
                f"📥 Tipo: "
                f"{dados['tipo']}\n"
            )

            arquivo.write(
                f"💵 Valor: "
                f"R$ {dados['valor']:.2f}\n"
            )

            arquivo.write(
                f"🏷️ Categoria: "
                f"{dados['categoria']}\n"
            )

            arquivo.write(
                f"📝 Descrição: "
                f"{dados['descricao']}\n"
            )

            arquivo.write(
                f"🕒 Gerada em: "
                f"{dados['data']}\n"
            )
            
            arquivo.write(
                "\n" + "=" * 40 + "\n\n"
            )
    
    print(
        "\n📄 Relatório exportado "
        "com sucesso."
    )