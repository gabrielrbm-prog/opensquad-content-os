---
task: desconstruir-conteudos
order: 1
agent: eva-estrutura
input:
  - knowledge/biblioteca/conteudos-top.md
  - _memory/memories.md
output:
  - output/estruturas/analises/
---

# Task: Desconstruir Conteúdos

## Objetivo
Pegar conteúdos top (transcritos por Bruno) e posts do @rubimfx que viralizaram (memories) e desconstruir a psicologia slide a slide.

## Process

### Step 1 — Priorizar
1. Posts do @rubimfx que viralizaram (memories → "Posts marcantes")
2. Conteúdos score 90-100 (conteudos-top.md)
3. Conteúdos score 70-89

### Step 2 — Desconstruir Slide a Slide
Para cada conteúdo:

| Slide | Texto Exato | Bloco Funcional | Gatilho | Por que funciona |
|-------|------------|-----------------|---------|-----------------|

Identificar: tipo de hook, estrutura em blocos, progressão, cliffhangers, cadência.

### Step 3 — Salvar
Uma análise por conteúdo em `output/estruturas/analises/{formato}-{perfil}-{id}.md`

## Quality Criteria
- [ ] Slide a slide (não resumo)
- [ ] Bloco funcional identificado por slide
- [ ] Gatilho psicológico por slide
