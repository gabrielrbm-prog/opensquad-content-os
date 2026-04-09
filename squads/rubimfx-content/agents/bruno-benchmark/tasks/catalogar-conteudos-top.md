---
task: catalogar-conteudos-top
order: 2
agent: bruno-benchmark
input:
  - output/benchmark/scan-{data}.md
output:
  - knowledge/biblioteca/conteudos-top.md
---

# Task: Catalogar Conteúdos Top

## Objetivo
Transcrever slide a slide os carrosséis virais do nicho. Dar score. Identificar hook, estrutura, ângulo.

## Process

### Step 1 — Selecionar Conteúdos
Pegar os posts com engajamento acima da média identificados no scan.

### Step 2 — Transcrever
Para cada conteúdo top:
- Texto exato de cada slide
- Função de cada slide (HOOK, TENSÃO, REVELAÇÃO, PROVA, CTA)
- Gatilho psicológico dominante por slide

### Step 3 — Scorear (5 critérios, max 25)
1. Engajamento estimado (1-5)
2. Qualidade do hook (1-5)
3. Estrutura narrativa clara (1-5)
4. Relevância para @rubimfx (1-5)
5. Replicabilidade (1-5)

### Step 4 — Salvar
Adicionar em `knowledge/biblioteca/conteudos-top.md`

## Quality Criteria
- [ ] Transcrição slide a slide (não resumo)
- [ ] Score com 5 critérios
- [ ] Hook, estrutura e ângulo identificados
