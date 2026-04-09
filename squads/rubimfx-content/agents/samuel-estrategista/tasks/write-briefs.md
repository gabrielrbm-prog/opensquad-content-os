---
task: write-briefs
order: 3
agent: samuel-estrategista
input:
  - output/strategy/01-calendario-editorial.md
output:
  - output/strategy/briefings/brief-{N}.md
  - output/strategy/02-metas-performance.md
---

# Task: Escrever Briefings por Pauta + Metas

## Objetivo
Gerar briefing individual para cada pauta fixa do calendário + definir metas de performance do período.

## Process

### Step 1 — Briefing por Pauta
Para cada slot fixo:
- Pilar, etapa funil, modelo visual sugerido
- Ângulo sugerido (das 16 categorias)
- Objetivo do post, emoção central
- Bridge macro→trading (se aplicável)
- CTA (tipo + alinhado com funil)
- Referências (temas que viralizam, posts similares)
- Meta de performance (métrica principal + benchmark)
- Restrições (compliance, vetos)

Salvar cada um em `output/strategy/briefings/brief-{N}.md`

### Step 2 — Metas de Performance
- Meta geral do período (objetivo + métrica de sucesso)
- Metas por etapa do funil
- Critério de winner (>1.5x média)
- Critério de underperformer (<0.8x média)

Salvar em `output/strategy/02-metas-performance.md`

## GATE: validacao-final (review)

## Quality Criteria
- [ ] Cada briefing tem: pilar, funil, ângulo, emoção, CTA, meta
- [ ] Metas mensuráveis por etapa
- [ ] Critérios de winner/under definidos
