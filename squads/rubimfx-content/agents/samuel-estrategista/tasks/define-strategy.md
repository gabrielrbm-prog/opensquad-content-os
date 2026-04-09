---
task: define-strategy
order: 1
agent: samuel-estrategista
input:
  - pipeline/data/research-focus.md
  - _memory/memories.md
  - _metadata.yaml
output:
  - output/strategy/00-briefing-estrategico.md
---

# Task: Definir Estratégia do Período

## Objetivo
Definir objetivo dos próximos 7-14 dias, avaliar capacidade de produção, e montar distribuição de funil orgânico adaptada.

## Process

### Step 1 — Ler Contexto
- Ler `pipeline/data/research-focus.md` (temas quentes)
- Ler `_memory/memories.md` (o que funciona, modelos que engajam, posts marcantes)
- Ler `_metadata.yaml` (histórico de produções)

### Step 2 — Definir Objetivo
Apresentar opções ao operador baseado no contexto:
- Aquecer conta (50% topo, 30% meio, 15% fundo)
- Crescer audiência (45% topo, 35% meio, 20% fundo)
- Construir autoridade (25% topo, 45% meio, 30% fundo)
- Gerar conversão (15% topo, 30% meio, 55% fundo)
- Testar e aprender (35% topo, 35% meio, 30% fundo)

### Step 3 — Avaliar Capacidade
- Quantos posts/semana é viável? (baseado em pipeline ~30min/carrossel)
- Tem evento importante? (FOMC, NFP, escândalo ativo)
- Algum veto ou tema obrigatório?

### Step 4 — Salvar Briefing Estratégico
Salvar em `output/strategy/00-briefing-estrategico.md` com: objetivo, métrica de sucesso, funil, capacidade, direcionamentos.

## GATE: aprovacao-objetivo (blocking)

## Quality Criteria
- [ ] Objetivo claro com métrica de sucesso
- [ ] Funil adaptado ao objetivo (não fixo)
- [ ] Capacidade real respeitada
