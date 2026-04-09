---
task: build-calendar
order: 2
agent: samuel-estrategista
input:
  - output/strategy/00-briefing-estrategico.md
  - pipeline/data/research-focus.md
  - _memory/memories.md
output:
  - output/strategy/01-calendario-editorial.md
---

# Task: Montar Calendário Editorial

## Objetivo
Selecionar pautas e montar calendário com slots fixos (~70%) e flexíveis (~30%).

## Process

### Step 1 — Selecionar Pautas
- Cruzar: research-focus (temas quentes) + memories (temas que viralizam) + pilares de conteúdo
- Para cada pauta: pilar, etapa funil, ângulo sugerido (das 16 categorias)
- Priorizar por potencial viral

### Step 2 — Montar Calendário
- Distribuir slots fixos no calendário (dia + pauta + pilar + funil + modelo visual sugerido)
- Reservar ~30% de slots flexíveis para conteúdo reativo
- Respeitar capacidade definida no briefing

### Step 3 — Salvar
Salvar em `output/strategy/01-calendario-editorial.md`

## GATE: aprovacao-pautas (blocking) + aprovacao-calendario (blocking)

## Quality Criteria
- [ ] Pautas selecionadas com justificativa (não feeling)
- [ ] Pilares distribuídos intencionalmente
- [ ] ~30% slots flexíveis
- [ ] Capacidade real respeitada
