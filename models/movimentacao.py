from datetime import datetime

class Movimentacao:

    def __init__(
        self,
        tipo,
        valor,
        categoria,
        descricao,
        data=None
    ):
        self.tipo = tipo
        self.valor = valor
        self.categoria = categoria
        self.descricao = descricao
        
        self.data = (
            data
            or datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )
        )

    def exibir(self):

        print(f"\n Tipo: {self.tipo}")
        print(f" Valor: {self.valor}")
        print(f" Categoria: {self.categoria}")
        print(f" Descrição: {self.descricao}")
        print(f" Gerada em: {self.data}")
    
    def to_dict(self):

        return {
            "tipo": self.tipo,
            "valor": self.valor,
            "categoria": self.categoria,
            "descricao": self.descricao,
            "data": self.data
        }
    
    @classmethod
    def from_dict(cls, dados):

        movimentacao = cls(
            dados["tipo"],
            dados["valor"],
            dados["categoria"],
            dados["descricao"],
            dados["data"]
        )

        return movimentacao