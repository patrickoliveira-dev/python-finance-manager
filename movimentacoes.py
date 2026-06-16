import json
from models.movimentacao import Movimentacao
from datetime import datetime

TIPOS = ["Receita", "Despesa"]

CATEGORIAS_RECEITA = [
    "Salário",
    "Freelance",
    "Investimentos",
    "Outros"
]

CATEGORIAS_DESPESA = [
    "Moradia",
    "Contas",
    "Transporte",
    "Alimentação",
    "Saúde",
    "Lazer",
    "Educação",
    "Internet",
    "Telefonia",
    "Compras",
    "Pets",
    "Assinaturas",
    "Vestuário",
    "Presentes",
    "Impostos e Taxas",
    "Manutenção",
    "Investimentos",
    "Outros"
]

def salvar_movimentacao(movimentacao):
    
    nova_movimentacao = movimentacao.to_dict()

    movimentacoes = carregar_movimentacoes()

    movimentacoes.append(nova_movimentacao)

    salvar_movimentacoes(movimentacoes)

def adicionar_movimentacao():

    tipo = escolher_tipo()

    if tipo is None:
        return

    while True:

        try:

            valor = float(
                input("\nValor: ")
            )

            if valor <= 0:

                print(
                    "\n❌ O valor deve ser maior que zero."
                )

                continue

            break

        except ValueError:

            print(
                "\n❌ Valor inválido."
            )

    categoria = escolher_categoria(tipo)

    if categoria is None:
        return

    descricao = input(
        "\nDescrição: "
    )

    id = gerar_id()

    movimentacao = Movimentacao(
        id,
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

def mostrar_movimentacoes():

    movimentacoes = obter_movimentacoes()

    if movimentacoes is None:
        return
    
    print ("\n=== MOVIMENTAÇÕES ===")

    for dados in movimentacoes:

        movimentacao = Movimentacao.from_dict(
            dados
        )

        movimentacao.exibir()

def carregar_movimentacoes():

    try:

        with open(
            "dados/movimentacoes.json",
            "r",
            encoding="utf-8"
        ) as arquivo:
            
            movimentacoes = json.load(arquivo)

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

def obter_movimentacoes():

    movimentacoes = carregar_movimentacoes()

    if not movimentacoes:

        print(
            "\nNenhuma movimentação encontrada."
        )

        return None
    
    return movimentacoes

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

def excluir_movimentacao():

    movimentacoes = obter_movimentacoes()

    if movimentacoes is None:
        return
    
    indice = escolher_movimentacao(movimentacoes)

    if indice is None:
        return
    
    removida = movimentacoes.pop(indice)

    salvar_movimentacoes(movimentacoes)

    print(
        f"\n🗑️ Movimentação ID "
        f"{removida['id']} "
        f"({removida['descricao']}) "
        f"removida com sucesso."
    )

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

def editar_movimentacao():

    movimentacoes = obter_movimentacoes()

    if movimentacoes is None:
        return
    
    indice = escolher_movimentacao(movimentacoes)

    if indice is None:
        return
    
    movimentacao = movimentacoes[indice]

    print(
        f"\nEditando movimentação "
        f"ID {movimentacao['id']}"
    )

    print(
        f"\nTipo atual: "
        f"{movimentacao['tipo']}"
    )

    novo_tipo = escolher_tipo()

    movimentacao["tipo"] = novo_tipo

    print(
        f"\nValor atual: "
        f"{movimentacao['valor']:.2f}"
    )

    while True:

        try:

            novo_valor = float(
                input("\nValor: ")
            )

            if novo_valor <= 0:

                print(
                    "\n❌ O valor deve ser maior que zero."
                )

                continue

            break

        except ValueError:

            print(
                "\n❌ Valor inválido."
            )

    movimentacao["valor"] = novo_valor

    print(
        f"\nCategoria atual: "
        f"{movimentacao['categoria']}"
    )

    nova_categoria = escolher_categoria(
        novo_tipo
    )

    if nova_categoria is None:
        return

    movimentacao["categoria"] = nova_categoria

    print(
        f"\nDescrição atual: "
        f"{movimentacao['descricao']}"
    )

    nova_descricao = input(
        "\nNova descrição: "
    )

    if nova_descricao:

        movimentacao["descricao"] = nova_descricao

    salvar_movimentacoes(movimentacoes)

    print(
        "\n✅ Movimentação editada com sucesso."
    )
    

def listar_movimentacoes_resumidas(movimentacoes):
    
    print("\n=== MOVIMENTAÇÕES ===")
    
    for indice, movimentacao in enumerate(
        movimentacoes,
        start=1
    ):

        print(
            f"{indice} - "
            f"ID {movimentacao['id']} | "
            f"{movimentacao['categoria']} | "
            f"R$ {movimentacao['valor']:.2f}"
        )

def escolher_movimentacao(movimentacoes):

    listar_movimentacoes_resumidas(movimentacoes)

    try:

        numero = int(
            input(
                "\nDigite o número da movimentação: "
            )
        )
    
    except ValueError:
        
        print("\n❌ Digite um número válido.")
        return

    if numero < 1 or numero > len(movimentacoes):

        print(
            "\n❌ Número inválido."
        )

        return None
    
    return numero - 1

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
    
def escolher_categoria(tipo):

    if tipo == "Receita":

        categorias = CATEGORIAS_RECEITA

    else:

        categorias = CATEGORIAS_DESPESA

    print("\n=== CATEGORIAS ===")

    for indice, categoria in enumerate(
        categorias,
        start=1
    ):

        print(
            f"{indice} - "
            f"{categoria}"
        )

    try:

        opcao = int(
            input(
                "\nEscolha uma categoria: "
            )
        )

    except ValueError:

        print(
            "\n❌ Categoria inválida."
        )

        return None

    if opcao < 1 or opcao > len(categorias):

        print(
            "\n❌ Categoria inválida."
        )

        return None

    return categorias[opcao - 1]

def escolher_tipo(prompt="\nTipo (Receita/Despesa): "):

    while True:

        tipo = input(prompt).strip().capitalize()

        if tipo in TIPOS:
            return tipo
        
        print("\n❌ Tipo inválido. Digite Receita ou Despesa.")
    
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

def gerar_id():

    movimentacoes = carregar_movimentacoes()

    if not movimentacoes:
        return 1
    
    maior_id = max(
        movimentacao["id"]
        for movimentacao in movimentacoes
    )

    return maior_id + 1

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