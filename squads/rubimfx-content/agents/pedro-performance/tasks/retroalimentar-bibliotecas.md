---
task: retroalimentar-bibliotecas
order: 3
agent: pedro-performance
input:
  - output/performance/checkpoint-7d-{data}.md
output:
  - _memory/memories.md
---

# Task: Retroalimentar Bibliotecas

## Objetivo
Atualizar memories.md e bibliotecas com dados reais de performance. Fechar o loop.

## Process

### Step 1 — Atualizar memories.md
Seções a atualizar:
- "Modelos que mais engajam" → com dados reais do ciclo
- "Conteúdo que funciona" → padrões confirmados
- "Temas com alto potencial viral" → validados ou removidos
- "Posts marcantes" → winners adicionados
- "Erros recorrentes a evitar" → novos aprendizados

### Step 2 — Atualizar Bibliotecas (se dados relevantes)
- `knowledge/biblioteca/hooks-campeoes.md` → hooks que performaram com dados reais
- `knowledge/biblioteca/estruturas-invisiveis.md` → scores de recorrência atualizados

### Step 3 — Confirmar
Sinalizar ao operador que memories e bibliotecas foram atualizados.

## Quality Criteria
- [ ] memories.md atualizado com dados reais (não inventados)
- [ ] Winners registrados com métricas
- [ ] Padrões com nível de confiança (1 ciclo = hipótese, 2+ = confirmado)
