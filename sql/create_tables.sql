CREATE TABLE movimentacoes (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    descricao TEXT NOT NULL,
    valor NUMERIC(12,2) NOT NULL CHECK (valor > 0),

    tipo TEXT NOT NULL CHECK (tipo IN ('RECEITA','DESPESA')),

    categoria TEXT,

    data DATE NOT NULL,

    recorrente BOOLEAN NOT NULL DEFAULT FALSE,
    frequencia TEXT,
    ativa BOOLEAN NOT NULL DEFAULT TRUE
);