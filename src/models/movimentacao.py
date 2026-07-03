from decimal import Decimal
from datetime import date

class Movimentacao:
    """Representa uma movimentação financeira do sistema."""
    
    def __init__(
        self,
        descricao: str,
        valor: Decimal,
        tipo: str,
        categoria: str,
        data: date,
        recorrente: bool,
        frequencia: str | None,
        ativa: bool
    ):

        self.descricao = descricao
        self.valor = valor
        self.tipo = tipo
        self.categoria = categoria
        self.data = data
        self.recorrente = recorrente
        self.frequencia = frequencia
        self.ativa = ativa

    def __str__(self):
        return (
            f"{self.tipo} | "
            f"{self.categoria} | "
            f"{self.descricao} | "
            f"R$ {self.valor:.2f}"
        )

    def to_sql(self):
        return f"""
        INSERT INTO movimentacoes (
            descricao,
            valor,
            tipo,
            categoria,
            data,
            recorrente,
            frequencia,
            ativa
        ) VALUES (
            '{self.descricao.replace("'", "''")}',
            {float(self.valor)},
            '{self.tipo}',
            '{self.categoria}',
            '{self.data.isoformat()}',
            {str(self.recorrente).upper()},
            {'NULL' if self.frequencia is None else f"'{self.frequencia}'"},
            {str(self.ativa).upper()}
        );
        """