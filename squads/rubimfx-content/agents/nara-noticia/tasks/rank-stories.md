---
task: rank-stories
order: 2
input:
  - output/news-research.md
output:
  - output/news-research.md
---

# Task: Rank Stories — Ranking por Viralidade e Relevancia

## Objetivo
Receber a lista bruta de 10-15 noticias do find-news e aplicar um sistema de pontuacao calibrado para VIRALIDADE NO INSTAGRAM. Selecionar as top 5-8 e sugerir angulo de carrossel para cada.

## Process

### Step 1 — Carregar e Validar Lista Bruta
Validar que:
- Ha pelo menos 8 noticias na lista
- Todos os campos obrigatorios estao preenchidos
- As noticias estao dentro do periodo definido
Se a lista tiver menos de 8, sinalizar e prosseguir com o disponivel.

### Step 2 — Pontuar Cada Noticia (5 criterios, total maximo 25)

**Criterio 1: Potencial Viral no Instagram (peso 1-5) — MAIS IMPORTANTE**
- 5 = Numero impactante + polemica + afeta bolso + comparacao possivel
- 4 = Tem 3 dos 4 sinais virais
- 3 = Tem 2 sinais virais
- 2 = Tem 1 sinal viral
- 1 = Noticia relevante mas sem gancho viral

**Criterio 2: Debate e Polarizacao (peso 1-5)**
- 5 = Tema que divide opinioes fortemente (politica, economia vs governo)
- 4 = Gera discussao nos comentarios com certeza
- 3 = Provoca reflexao mas nao necessariamente debate
- 2 = Informativo puro, pouca reacao
- 1 = Tecnico demais para gerar interacao

**Criterio 3: Numeros e Dados Visualizaveis (peso 1-5)**
- 5 = Multiplos dados impactantes, facil de fazer grafico/comparacao
- 4 = Tem 2-3 numeros fortes
- 3 = Tem 1 numero relevante
- 2 = Dados existem mas sao complexos de visualizar
- 1 = Noticia narrativa sem dados concretos

**Criterio 4: Relevancia para o Publico @rubimfx (peso 1-5)**
- 5 = Afeta diretamente: trading, bolso do brasileiro, politica que impacta mercado
- 4 = Muito relevante para trader/investidor brasileiro
- 3 = Relevante para contexto macro geral
- 2 = Interessante mas distante do dia-a-dia
- 1 = Tangencial

**Criterio 5: Atualidade e Timing (peso 1-5)**
- 5 = Acontecendo AGORA ou ultimas 6 horas
- 4 = Ultimas 12 horas
- 3 = Ultimas 24 horas
- 2 = Ultimas 48 horas
- 1 = Mais antigo (so com desdobramento novo)

### Step 3 — Selecionar Top 5-8 e Sugerir Angulos
Ordenar por pontuacao total (desempate pelo Criterio 1 — viral). Selecionar top 5-8 e para cada:
- Definir angulo de carrossel em 1 frase
- Sugerir formato visual (dados, timeline, vs., checklist, mapa, thread-style)
- Criar hook para o primeiro slide (especifico, nunca generico)
- Indicar tom recomendado (analitico, provocativo, urgente, educacional)

### Step 4 — Verificar Diversidade
Antes de salvar, checar:
- Pelo menos 3 categorias diferentes nas top 5
- Nao mais que 2 noticias do mesmo tema/ativo
- Pelo menos 1 noticia de politica brasileira (se houver algo relevante)
- Se 3+ noticias sao do mesmo tema, substituir a de menor nota por outra categoria

### Step 5 — Salvar Briefing Final
Atualizar `output/news-research.md` adicionando section `## Ranked Stories` no formato abaixo.

## Output Format

```yaml
meta:
  brief_date: "YYYY-MM-DD"
  stories_evaluated: 13
  stories_selected: 6
  focus: "topico do research-focus"

ranked_stories:
  - rank: 1
    title: "Titulo da noticia"
    source: "Fonte"
    date: "YYYY-MM-DD"
    url: "https://..."
    summary: "Resumo com dados concretos."
    key_numbers:
      - "R$ 4,2 bi"
      - "79,2% PIB"
    scores:
      viral_potential: 5
      debate_polarization: 4
      data_visual: 5
      audience_relevance: 5
      timeliness: 4
      total: 23
    carousel_angle: "Descricao do angulo em 1 frase"
    visual_format: "dados | timeline | versus | checklist | mapa | thread"
    hook_suggestion: "Frase de hook para o primeiro slide"
    recommended_tone: "analitico | provocativo | urgente | educacional"
    category: "politica-br | economia-br | geopolitica | mercado | trading | tech-ia | escandalo"
```

## Output Example

```yaml
ranked_stories:
  - rank: 1
    title: "Lula: 'Senador com mandato de 8 anos pensa que e Deus'"
    source: "CNN Brasil / O Antagonista"
    date: "2026-04-01"
    url: "https://cnnbrasil.com.br/..."
    summary: "Lula atacou senadores em entrevista no Ceara. Declaracao irritou lideres do Senado em momento critico — governo precisa de votos para aprovar indicacao ao STF."
    key_numbers:
      - "8 anos de mandato"
      - "18 ministros saindo pra eleicao"
    scores:
      viral_potential: 5
      debate_polarization: 5
      data_visual: 3
      audience_relevance: 4
      timeliness: 5
      total: 22
    carousel_angle: "Frase bomba de Lula sobre senadores — o que esta por tras da briga"
    visual_format: "thread"
    hook_suggestion: "'Senador pensa que e Deus.' Lula acabou de declarar guerra ao Senado."
    recommended_tone: "urgente"
    category: "politica-br"

  - rank: 2
    title: "Dolar cai pra R$ 5,16 — Real e a melhor moeda do mundo em 2026"
    source: "Valor Economico / Bloomberg Linea"
    date: "2026-04-01"
    url: "https://valor.globo.com/..."
    summary: "Real valorizou 5,65% no Q1 2026, melhor performance global. Ibovespa +16,35% no trimestre, melhor desde 2020. Dolar na minima desde marco."
    key_numbers:
      - "R$ 5,16"
      - "-5,65% no trimestre"
      - "Ibovespa +16,35%"
      - "Melhor moeda do mundo"
    scores:
      viral_potential: 5
      debate_polarization: 4
      data_visual: 5
      audience_relevance: 5
      timeliness: 5
      total: 24
    carousel_angle: "Real e a melhor moeda do mundo em 2026 — os numeros que ninguem esta mostrando"
    visual_format: "dados"
    hook_suggestion: "O real e a melhor moeda do mundo em 2026. Voce sabia?"
    recommended_tone: "provocativo"
    category: "economia-br"
```

## Quality Criteria

1. **Viral primeiro:** pelo menos 3 das top 5 devem ter viral_potential >= 4.
2. **Diversidade tematica:** top 5 com pelo menos 3 categorias diferentes.
3. **Angulos acionaveis:** cada carousel_angle deve ser especifico o suficiente para o roteirista comecar.
4. **Hook concreto:** NUNCA hooks genericos como "Veja o que aconteceu". Deve conter o dado ou a polemica.
5. **Numeros no hook:** sempre que possivel, o hook deve ter um numero (R$, %, ranking).

## Veto Conditions

1. **Nota inflada:** total acima de 20 sem dados concretos no resumo — revisar notas.
2. **Monocultura:** 3+ noticias do mesmo tema nas top 5 — substituir a de menor nota.
3. **Hook generico:** "Veja o que aconteceu no mercado" e similar — VETADO. Reescrever.
4. **Sem numero no resumo:** se key_numbers esta vazio e nao e escandalo/polemica pura — perder 2 pontos no data_visual.
