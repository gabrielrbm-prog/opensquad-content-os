---
task: find-news
order: 1
input:
  - pipeline/data/research-focus.md
output:
  - output/news-research.md
---

# Task: Find News — Busca Ampla de Noticias

## Objetivo
Varrer fontes brasileiras, internacionais E Twitter/X para retornar 10-15 noticias candidatas. O filtro principal nao e "relevancia para trading" — e "potencial de viralizar no Instagram de @rubimfx". Escopo: economia, politica, geopolitica, mercado financeiro, tech/IA disruptiva.

## Process

### Step 1 — Ler o Foco de Pesquisa
Abrir `pipeline/data/research-focus.md` e extrair:
- Topico principal (se definido) ou "cobertura geral do dia"
- Periodo de busca (padrao: ultimas 24 horas)
- Ativos ou temas em destaque
- Restricoes ou preferencias do usuario
- Fontes prioritarias indicadas

### Step 2 — Buscar no Twitter/X (PRIMEIRO)
Twitter/X e onde as noticias quebram primeiro. Buscar ANTES das fontes tradicionais:
- Termos trending no Brasil (politica, economia, escândalos)
- Threads virais com dados concretos (numeros, graficos, comparacoes)
- Breaking news de jornalistas BR (Lauro Jardim, Andréia Sadi, etc.)
- Contas de mercado global (@DeItaone, @unusual_whales, @zerohedge)
- Reacoes de politicos e economistas a eventos do dia
- Buscar: `site:twitter.com [tema]` ou `site:x.com [tema]`

### Step 3 — Buscar em Fontes Brasileiras
Priorizar veiculos que publicam rapido e com viés alinhado ao publico:
- **Breaking:** O Antagonista, Jovem Pan, Metropoles
- **Editorial:** Gazeta do Povo, Revista Oeste, Poder360
- **Financeiro:** InfoMoney, Valor Economico, Bloomberg Linea, Exame
- **Cobertura geral:** CNN Brasil, Folha, BBC Brasil
- Termos: escândalos do dia, decisoes STF, dados economicos, pesquisas eleitorais, crises politicas

### Step 4 — Buscar em Fontes Internacionais
Para macro global, geopolitica e mercados:
- Reuters, Bloomberg, Financial Times, CNBC, WSJ
- Termos em ingles: "FOMC", "Fed", "NFP", "CPI", "gold", "S&P500", "DXY", "tariffs", "Iran", "oil"
- Calendario economico: ForexFactory, Investing.com

### Step 5 — Avaliar Potencial Viral de Cada Noticia
Para CADA noticia encontrada, avaliar rapidamente:
- Tem numero impactante? (R$ bilhoes, %, ranking, recorde)
- Gera polemica/debate? (posicoes opostas, escandalo, hipocrisia)
- Tem "efeito WTF"? (surpresa, absurdo, inesperado)
- E comparavel? (antes vs depois, pais vs pais, politico vs politico)
- Afeta o bolso do brasileiro? (combustivel, alimentos, emprego, impostos)

Se a resposta for SIM para 2+ desses, a noticia entra na lista.

### Step 6 — Compilar Lista Bruta
Montar lista com 10-15 noticias. Descartar noticias que:
- Nao tem fonte verificavel
- Sao mais antigas que o periodo definido (salvo desdobramentos)
- Nao tem potencial viral NEM relevancia para o publico
- Sao paywalled sem resumo acessivel

### Step 7 — Salvar Output
Gravar resultado em `output/news-research.md` no formato abaixo.

## Output Format

```yaml
meta:
  search_date: "YYYY-MM-DD"
  period: "ultimas 24h | ultimas 48h | semana"
  focus: "topico do research-focus ou cobertura geral"
  total_found: 12
  sources_consulted:
    - Twitter/X
    - Gazeta do Povo
    - Reuters
    - InfoMoney

stories:
  - id: 1
    title: "Titulo da noticia"
    source: "Nome da Fonte"
    source_type: "twitter | editorial-br | financeiro-br | internacional | dados"
    date: "YYYY-MM-DD"
    url: "https://..."
    summary: "Resumo de 2-3 linhas com dados concretos."
    key_numbers:
      - "R$ 4,2 bilhoes"
      - "79,2% do PIB"
    category: "politica-br | economia-br | geopolitica | mercado | trading | tech-ia | escandalo"
    viral_signals:
      - "numero impactante"
      - "gera debate"
      - "afeta bolso"
    assets_impacted:
      - DXY
      - USD/BRL
```

## Quality Criteria

1. **Volume:** minimo 10, maximo 15 noticias na lista bruta.
2. **Diversidade de fontes:** pelo menos 5 fontes diferentes, incluindo Twitter/X.
3. **Diversidade tematica:** pelo menos 3 categorias diferentes representadas.
4. **Campos completos:** 100% com title, source, date, url, summary, key_numbers, category, viral_signals.
5. **Numeros obrigatorios:** cada summary deve conter pelo menos 1 dado numerico concreto.
6. **Twitter/X incluido:** pelo menos 2 noticias devem ter sido encontradas ou confirmadas via Twitter/X.

## Veto Conditions

1. **Fonte nao verificavel:** URL nao funciona ou fonte nao e identificavel — NAO entra.
2. **Sem numero:** noticia puramente narrativa sem nenhum dado concreto — deprioritizar (so entra se for escandalo viral).
3. **Duplicata:** mesma noticia em multiplas fontes — manter a de maior prioridade, citar demais como confirmacao.
4. **Velho sem novidade:** noticia de 48h+ sem desdobramento novo — NAO entra.
