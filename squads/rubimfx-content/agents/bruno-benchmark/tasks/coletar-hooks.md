---
task: coletar-hooks
order: 3
agent: bruno-benchmark
input:
  - knowledge/biblioteca/conteudos-top.md
output:
  - knowledge/biblioteca/hooks-campeoes.md
---

# Task: Coletar Hooks

## Objetivo
Extrair hooks de todos os carrosséis catalogados. Classificar por gatilho neurológico.

## Process

### Step 1 — Extrair Hooks
Para cada conteúdo em conteudos-top.md, extrair o slide 1 (hook).

### Step 2 — Classificar
Para cada hook:
- Texto exato
- Conta de origem
- Gatilho dominante (dos 5 fundamentos neurológicos)
- Gatilhos secundários
- Fórmula headline (H01-H28 se aplicável)
- Score estimado (1-5)

### Step 3 — Salvar
Adicionar em `knowledge/biblioteca/hooks-campeoes.md` organizado por gatilho.

## Quality Criteria
- [ ] Cada hook tem gatilho identificado
- [ ] Organizado por fundamento neurológico
- [ ] Score estimado
