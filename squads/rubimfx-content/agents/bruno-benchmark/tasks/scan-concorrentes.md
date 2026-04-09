---
task: scan-concorrentes
order: 1
agent: bruno-benchmark
input:
  - knowledge/biblioteca/concorrentes.md
output:
  - knowledge/biblioteca/concorrentes.md
  - output/benchmark/scan-{data}.md
---

# Task: Scan de Concorrentes

## Objetivo
Monitorar as contas de referência semanalmente. Coletar: últimos posts, formato dominante, frequência, mudanças de estilo.

## Process

### Step 1 — Ler Biblioteca Existente
Ler `knowledge/biblioteca/concorrentes.md` para não reprocessar o que já foi analisado.

### Step 2 — Scannear Contas por Tier
Para cada conta monitorada (Tier 1 Direto, Tier 2 Indireto, Tier 3 Referência):
1. Buscar últimos 5-10 posts via web_search/web_fetch
2. Identificar post com mais engajamento
3. Registrar formato dominante e frequência
4. Notar mudanças de estilo vs scan anterior

### Step 3 — Atualizar Biblioteca
Adicionar dados novos em `knowledge/biblioteca/concorrentes.md` (nunca apagar dados antigos).

### Step 4 — Salvar Relatório
Salvar relatório do scan em `output/benchmark/scan-{data}.md`

## Quality Criteria
- [ ] Todas as contas monitoradas foram checadas
- [ ] Dados com data de observação
- [ ] Biblioteca atualizada (acumulada, não substituída)
