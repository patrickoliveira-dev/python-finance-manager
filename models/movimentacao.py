from datetime import datetime

class Movimentacao:

    def __init__(
        self,
        id,
        tipo,
        valor,
        categoria,
        descricao,
        data=None,
        recorrente=False,
        frequencia=None
    ):
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.categoria = categoria
        self.descricao = descricao

        self.recorrente = recorrente
        self.frequencia = frequencia
        
        self.data = (
            data
            or datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )
        )

    def exibir(self):

        print(f"\n🆔 ID: {self.id}")
        print(f"📥 Tipo: {self.tipo}")
        print(f"💵 Valor: R$ {self.valor:.2f}")
        print(f"🏷️ Categoria: {self.categoria}")
        print(f"📝 Descrição: {self.descricao}")

        if self.recorrente:

            print(
                f"🔁 Recorrente: Sim "
                f"({self.frequencia})"
            )

        else:

            print(
                "🔁 Recorrente: Não"
            )

        print(f"🕒 Gerada em: {self.data}")

    def to_dict(self):

        return {
            "id": self.id,
            "tipo": self.tipo,
            "valor": self.valor,
            "categoria": self.categoria,
            "descricao": self.descricao,
            "data": self.data,
            "recorrente": self.recorrente,
            "frequencia": self.frequencia
        }
    
    @classmethod
    def from_dict(cls, dados):

        movimentacao = cls(
            dados["id"],
            dados["tipo"],
            dados["valor"],
            dados["categoria"],
            dados["descricao"],
            dados["data"],
            dados.get("recorrente", False),
            dados.get("frequencia")
        )

        return movimentacao