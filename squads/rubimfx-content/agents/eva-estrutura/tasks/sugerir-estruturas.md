---
task: sugerir-estruturas
order: 3
agent: eva-estrutura
input:
  - output/estruturas/padroes-recorrentes.md
output:
  - output/estruturas/sugestoes-criacao.md
  - knowledge/biblioteca/estruturas-invisiveis.md
---

# Task: Sugerir Estruturas para Criação

## Objetivo
Organizar top 3-5 estruturas por formato com instruções diretas para Iago.

## Process

### Step 1 — Top 3 por Formato
Para carrossel (formato principal):
- Nome descritivo da estrutura
- Blocos na ordem
- Tamanho ideal (slides)
- Gatilhos dominantes
- Exemplo real com score
- Quando usar (tipo de tema/objetivo)
- Como adaptar para @rubimfx

### Step 2 — Salvar Sugestões
`output/estruturas/sugestoes-criacao.md`

### Step 3 — Atualizar Biblioteca
Adicionar/atualizar estruturas em `knowledge/biblioteca/estruturas-invisiveis.md`

## Quality Criteria
- [ ] Top 3 com instruções acionáveis para Iago
- [ ] Cada estrutura com exemplo real
- [ ] Biblioteca atualizada (acumulada)
