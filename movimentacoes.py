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
    "Alimentação",
    "Transporte",
    "Moradia",
    "Saúde",
    "Lazer",
    "Internet",
    "Educação",
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
        f"\n🗑️ Movimentação "
        f"'{removida['descricao']}' "
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