import random
from src.seed.data import *
from decimal import Decimal
from src.models.movimentacao import Movimentacao
from datetime import date, timedelta

class SeedGenerator:
    """Gerar dados fictícios"""

    def __init__(self):
        self.movimentacoes = []
        self.quantidade = 10000
    
    def gerar_tipo(self):
        tipos, pesos = zip(*TIPOS)
        return random.choices(tipos, weights=pesos, k=1)[0]

    def gerar_categoria(self, tipo):
        categorias, pesos = zip(*CATEGORIAS[tipo])
        return random.choices(categorias, weights=pesos, k=1)[0]
    
    def gerar_descricao(self, categoria):
        return random.choice(DESCRICOES[categoria])
    
    def gerar_valor(self, categoria):
        minimo, maximo = VALORES[categoria]
        return Decimal(
            str(round(random.uniform(minimo, maximo), 2))
        )
    
    def gerar_data(self):

        dias_atras = random.randint(0, 365)

        return date.today() - timedelta(days=dias_atras)
    
    def gerar_movimentacao(self):

        tipo = self.gerar_tipo()
        categoria = self.gerar_categoria(tipo)
        descricao = self.gerar_descricao(categoria)
        valor = self.gerar_valor(categoria)

        return Movimentacao(
            descricao=descricao,
            valor=valor,
            tipo=tipo,
            categoria=categoria,
            data=self.gerar_data(),
            recorrente=False,
            frequencia=None,
            ativa=True
        )

    def gerar(self):
        for _ in range(self.quantidade):
            mov = self.gerar_movimentacao()
            self.movimentacoes.append(mov)
    
    def exportar_sql(self, caminho="sql/seed.sql"):
        with open(caminho, "w", encoding="utf-8") as f:

            f.write("-- Seed gerado automaticamente\n")
            f.write("-- Finance Manager\n\n")

            for mov in self.movimentacoes:
                f.write(mov.to_sql())
                f.write("\n")