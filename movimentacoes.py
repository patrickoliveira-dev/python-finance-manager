from models.movimentacao import Movimentacao
from armazenamento import *
from constantes import (
    TIPOS,
    CATEGORIAS_RECEITA,
    CATEGORIAS_DESPESA,
    FREQUENCIAS
)

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

    resposta = input(
        "\nÉ recorrente? (s/n): "
    ).strip().lower()

    if resposta == "s":

        recorrente = True
        frequencia = escolher_frequencia()

        if frequencia is None:
            return

    else:

        recorrente = False
        frequencia = None

    id = gerar_id()

    movimentacao = Movimentacao(
        id,
        tipo,
        valor,
        categoria,
        descricao,
        recorrente=recorrente,
        frequencia=frequencia,
        ativa=recorrente
    )

    salvar_movimentacao(
        movimentacao
    )

    print(
        "\n✅ Movimentação adicionada."
    )

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
    
    print(
        f"\nRecorrente atual: "
        f"{'Sim' if movimentacao['recorrente'] else 'Não'}"
    )

    resposta = input(
        "\nÉ recorrente? (s/n): "
    ).strip().lower()

    if resposta == "s":

        movimentacao["recorrente"] = True

        nova_frequencia = escolher_frequencia()

        if nova_frequencia is None:
            return

        movimentacao["frequencia"] = nova_frequencia

    else:

        movimentacao["recorrente"] = False
        movimentacao["frequencia"] = None

    salvar_movimentacoes(movimentacoes)

    print(
        "\n✅ Movimentação editada com sucesso."
    )

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

def escolher_tipo(prompt="\nTipo (Receita/Despesa): "):

    while True:

        tipo = input(prompt).strip().capitalize()

        if tipo in TIPOS:
            return tipo
        
        print("\n❌ Tipo inválido. Digite Receita ou Despesa.")
    
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

def escolher_frequencia():

    print("\n=== FREQUÊNCIA ===")

    for indice, frequencia in enumerate(
        FREQUENCIAS,
        start=1
    ):

        print(
            f"{indice} - {frequencia}"
        )

    try:

        opcao = int(
            input(
                "\nEscolha uma frequência: "
            )
        )

    except ValueError:

        print(
            "\n❌ Frequência inválida."
        )

        return None

    if opcao < 1 or opcao > len(FREQUENCIAS):

        print(
            "\n❌ Frequência inválida."
        )

        return None

    return FREQUENCIAS[opcao - 1]

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

def listar_movimentacoes_resumidas(movimentacoes):
    
    print("\n=== MOVIMENTAÇÕES ===\n")
    
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

def gerar_id():

    movimentacoes = carregar_movimentacoes()

    if not movimentacoes:
        return 1
    
    maior_id = max(
        movimentacao["id"]
        for movimentacao in movimentacoes
    )

    return maior_id + 1