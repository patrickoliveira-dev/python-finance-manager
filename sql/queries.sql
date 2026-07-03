-- Todas as movimentações (visão operacional)
SELECT *
FROM movimentacoes
ORDER BY data DESC;

-- Receitas vs Despesas
SELECT
    tipo,
    COUNT(*) AS quantidade,
    SUM(valor) AS total
FROM movimentacoes
GROUP BY tipo;

-- Saldo geral
SELECT
    SUM(CASE WHEN tipo = 'RECEITA' THEN valor ELSE -valor END) AS saldo_total
FROM movimentacoes;

-- Despesas por categoria
SELECT
    categoria,
    SUM(valor) AS total_gasto
FROM movimentacoes
WHERE tipo = 'DESPESA'
GROUP BY categoria
ORDER BY total_gasto DESC;

-- Receita recorrente
SELECT
    recorrente,
    SUM(valor) AS total_receitas
FROM movimentacoes
WHERE tipo = 'RECEITA'
GROUP BY recorrente;

-- Movimentação por mês
SELECT
    DATE_TRUNC('month', data) AS mes,
    tipo,
    SUM(valor) AS total
FROM movimentacoes
GROUP BY mes, tipo
ORDER BY mes;

-- Top 5 despesas
SELECT *
FROM movimentacoes
WHERE tipo = 'DESPESA'
ORDER BY valor DESC
LIMIT 5;

-- KPIs gerais do sistema
SELECT
    (SELECT SUM(valor) FROM movimentacoes WHERE tipo='RECEITA') AS total_receitas,
    (SELECT SUM(valor) FROM movimentacoes WHERE tipo='DESPESA') AS total_despesas,
    (SELECT SUM(CASE WHEN tipo='RECEITA' THEN valor ELSE -valor END)
     FROM movimentacoes) AS saldo_final;