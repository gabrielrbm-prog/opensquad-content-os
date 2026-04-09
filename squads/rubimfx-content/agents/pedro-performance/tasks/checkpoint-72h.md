---
task: checkpoint-72h
order: 1
agent: pedro-performance
input:
  - output/posts/
  - output/strategy/02-metas-performance.md
  - _memory/memories.md
output:
  - output/performance/checkpoint-72h-{data}.md
---

# Task: Checkpoint 72h — Análise Tática

## Objetivo
Analisar performance de posts com 72h+ de publicação. Confirmar winners, avaliação granular, primeira retroalimentação.

## Process

### Step 1 — Coletar Métricas
Para cada post publicado há 72h+:
- Likes, comments, saves, shares, reach
- Calcular engagement rate: (likes + comments + saves + shares) ÷ reach × 100

### Step 2 — Classificar
- Winner: >1.5x média engajamento
- Acima da média: 1.1x - 1.5x
- Normal: 0.8x - 1.1x
- Underperformer: <0.8x

### Step 3 — Avaliação Granular (por post)
Avaliar 7 dimensões: modelo visual, ângulo (16 categorias), hook (5 fundamentos), pilar, etapa funil, horário, tipo de foto.

### Step 4 — Winners → Ação
Extrair tudo (hook, modelo, ângulo, pilar, fotos, horário). Sugerir repurpose.

### Step 5 — Underperformers → Hipótese
Isolar variável provável. Comparar com posts similares que performaram.

### Step 6 — Comparar com Metas de Samuel
Ler `output/strategy/02-metas-performance.md`. Métrica real vs meta.

### Step 7 — Salvar
`output/performance/checkpoint-72h-{data}.md`

## GATE: validacao-72h (review)

## Quality Criteria
- [ ] Engagement rate calculado
- [ ] Classificação com critério quantitativo
- [ ] Avaliação granular por 7 dimensões
- [ ] Winners com ação de repurpose
- [ ] Underperformers com hipótese
