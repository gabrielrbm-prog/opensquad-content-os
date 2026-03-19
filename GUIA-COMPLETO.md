# 🚀 Guia Completo — Opensquad + Instagram Content OS

> Sistema completo de produção de carrosséis para Instagram usando IA.
> Criado por @rubimfx | Documentado em março 2026.

---

## 📋 Índice

1. [Visão Geral do Sistema](#1-visão-geral)
2. [Pré-requisitos](#2-pré-requisitos)
3. [Instalação e Setup](#3-instalação)
4. [Estrutura do Projeto](#4-estrutura)
5. [Configuração das APIs](#5-apis)
6. [Como Funciona o Opensquad](#6-opensquad)
7. [Squads e Agentes](#7-squads)
8. [Templates de Carrossel (6 Estilos)](#8-templates)
9. [Scripts de Automação](#9-scripts)
10. [Pipeline de Produção Completo](#10-pipeline)
11. [Geração de Imagens (Nano Banana)](#11-imagens)
12. [Clone de Pessoa (Consistência Facial)](#12-clone)
13. [Publicação no Instagram](#13-publicacao)
14. [Pesquisa de Notícias Virais](#14-pesquisa)
15. [Checklist de Qualidade](#15-qualidade)
16. [Troubleshooting](#16-troubleshooting)
17. [FAQ](#17-faq)

---

## 1. Visão Geral

### O que é este sistema?
Um framework de IA que produz carrosséis profissionais para Instagram de forma semi-automática:
- Pesquisa notícias virais do dia
- Gera imagens via IA (Nano Banana / Google Gemini)
- Clona fotos da pessoa mantendo consistência facial
- Cria 10 slides HTML com design profissional
- Renderiza PNGs 1080x1350 (4:5 Instagram)
- Publica direto no Instagram via Playwright

### Stack Tecnológica
| Componente | Tecnologia |
|---|---|
| Orquestração | Opensquad (multi-agent framework) |
| Slides | HTML/CSS → PNG (Playwright screenshot) |
| Imagens IA | Google Gemini API (gemini-2.5-flash-image) |
| Clone facial | clone_image.py (multi-referência + identity header) |
| Publicação | Playwright MCP (Chrome automatizado) |
| Pesquisa | WebSearch + Firecrawl MCP |
| Validação | preflight_check.py (26 checks) |
| Runtime | Python 3 + Node.js |

### Resultados
- 19 carrosséis publicados em 4 dias
- 6 estilos visuais diferentes testados
- Tempo médio por carrossel: ~15 minutos (pesquisa → publicação)

---

## 2. Pré-requisitos

### Software necessário
- macOS ou Linux
- Python 3.10+
- Node.js 18+
- npm
- Google Chrome instalado
- Claude Code (CLI) com modelo Opus

### Contas necessárias
- Instagram (conta profissional)
- Google AI Studio (para API key Gemini)
- Firecrawl (opcional, para screenshots limpos)

---

## 3. Instalação

### Passo 1: Clonar o repositório
```bash
git clone https://github.com/SEU-USUARIO/opensquad-content-os.git
cd opensquad-content-os
```

### Passo 2: Instalar dependências
```bash
npm install
pip3 install google-genai --break-system-packages
```

### Passo 3: Configurar .env
```bash
cp .env.example .env
# Edite o .env com suas chaves:
# GOOGLE_API_KEY=sua-chave-gemini
# INSTAGRAM_ACCESS_TOKEN=seu-token (opcional)
```

### Passo 4: Configurar Opensquad
```bash
# Abra o Claude Code nesta pasta
claude

# Execute o onboarding
/opensquad
```

O sistema vai pedir:
- Seu nome
- Idioma preferido
- Nome e URL da empresa
- Vai pesquisar automaticamente seu nicho

### Passo 5: Adicionar suas fotos de referência
```bash
mkdir -p squads/SEU-SQUAD/assets/fotos-referencia/
# Coloque 3-5 fotos suas (frontal, 3/4, perfil)
# Quanto melhor a qualidade, melhor o clone
```

---

## 4. Estrutura do Projeto

```
projeto/
├── _opensquad/           ← Framework core (NÃO editar)
│   ├── core/             ← Agentes e pipeline runner
│   ├── config/           ← Configuração Playwright
│   └── _memory/          ← Memória da empresa (gitignored)
├── squads/               ← Seus squads de conteúdo
│   └── rubimfx-content/  ← Exemplo de squad
│       ├── agents/       ← Agentes especializados
│       ├── assets/       ← Fotos e logos
│       ├── output/       ← Posts gerados (gitignored)
│       ├── pipeline/     ← Pipeline de produção
│       ├── scripts/      ← Automação Python
│       └── templates/    ← 18 templates HTML
├── skills/               ← Plugins reutilizáveis
├── dashboard/            ← Frontend 3D (opcional)
├── .env                  ← Chaves de API (gitignored)
├── CLAUDE.md             ← Instruções para o Claude
└── GUIA-COMPLETO.md      ← Este guia
```

---

## 5. Configuração das APIs

### Google Gemini (Nano Banana) — Obrigatório
1. Acesse https://aistudio.google.com/
2. Crie uma API key
3. Adicione ao .env: `GOOGLE_API_KEY=AIzaSy...`
4. Custo: ~US$0.07/imagem (~R$0.35)

### Firecrawl — Opcional (para screenshots limpos)
1. Acesse https://firecrawl.dev/
2. Crie uma conta e API key
3. Configure no .mcp.json

---

## 6. Como Funciona o Opensquad

### Comandos principais
| Comando | Ação |
|---|---|
| `/opensquad` | Menu principal |
| `/opensquad create` | Criar novo squad |
| `/opensquad run rubimfx-content` | Executar pipeline |
| `/opensquad list` | Listar squads |
| `/opensquad help` | Ver todos os comandos |

### Fluxo de trabalho
1. **Architect** cria o squad (agentes + pipeline)
2. **Pipeline Runner** executa step by step
3. **Checkpoints** pausam para aprovação humana
4. **Output** vai para `squads/nome/output/`

---

## 7. Squads e Agentes

### Squad: rubimfx-content
Produz carrosséis de 10 slides para Instagram.

### Agentes disponíveis
| Agente | Função |
|---|---|
| **Nara Notícia** | Pesquisa notícias virais do dia |
| **Iago Instagram** | Gera ângulos e seleciona temas |
| **Diana Design** | Cria os 10 slides HTML |
| **Iris Imagem** | Gera imagens via Nano Banana |
| **Leo Legenda** | Escreve captions otimizadas |
| **Renata Revisão** | Valida qualidade (preflight) |
| **Vitor Visual** | Pesquisa tendências visuais |

---

## 8. Templates de Carrossel (6 Estilos)

### Estilo 1: Twitter Dark (Padrão)
- 7 tipos de card diferentes por carrossel
- Fundo preto, cards #16181C, bordas #2F3336
- Headlines 52-80px, body 28-34px
- Referência: `templates/twitter-dark-reference.md`

### Estilo 2: Esteter Style
- Tweet thread numerado (1️⃣2️⃣3️⃣)
- Screenshots reais de reportagem
- Referência: `templates/esteter-style-reference.md`

### Estilo 3: Hollyfield News
- Fotos hero FULL BLEED (70-80% do slide)
- Header bar laranja no topo
- Headline sobre gradiente
- Template: `templates/template-11-hollyfield-news.html`

### Estilo 4: Kaique Epic ⭐ (FAVORITO)
- Capas cinematográficas com fotos IA épicas
- Headlines GIGANTES 80-96px uppercase
- Palavras-chave em AMARELO (#FFD600)
- Tweet cards brancos para slides internos
- Templates: `template-09-kaique-epic.html` + `template-10-kaique-tweet.html`

### Estilo 5: BrunoGPT Neon
- Covers neon vibrantes
- Templates: `template-12` e `template-13`

### Estilo 6: Minimal Clean
- Fundo branco/claro, ultra minimalista
- Ainda não testado em produção

### Regras universais (TODOS os estilos)
- Dimensão: 1080x1350px (4:5 Instagram)
- Fonte mínima: 22px (NADA abaixo de 20px)
- Português com acentos corretos
- profile-photo.jpeg apenas para avatar (48-52px)
- Sem URLs externas (Unsplash, CDN)
- Cada slide é HTML standalone

---

## 9. Scripts de Automação

### render_slides.py — Renderizar HTML → PNG
```bash
python3 scripts/render_slides.py output/posts/PASTA-DO-POST
```
- Inicia http.server na pasta html/
- Renderiza cada slide-XX.html como PNG 1080x1350
- Salva em png/

### pipeline.py — Pipeline completo
```bash
python3 scripts/pipeline.py output/posts/PASTA-DO-POST
```
- Copia profile-photo
- Valida fontes
- Valida acentos
- Renderiza
- Preflight check

### generate_image.py — Gerar imagem IA
```bash
python3 scripts/generate_image.py "prompt em inglês" output.png
```

### clone_image.py — Clonar pessoa
```bash
# Com preset:
python3 scripts/clone_image.py foto-ref.jpg trading-desk output.png

# Custom:
python3 scripts/clone_image.py foto-ref.jpg "cenário descrito" output.png

# Multi-referência (melhor resultado):
python3 scripts/clone_image.py foto1.jpg --multi foto2.jpg foto3.jpg preset output.png

# Batch (todos os 12 presets):
python3 scripts/clone_image.py foto-ref.jpg --batch clones/

# Listar presets:
python3 scripts/clone_image.py --list
```

### preflight_check.py — Validação
```bash
python3 scripts/preflight_check.py output/posts/PASTA-DO-POST
```
26 checks: estrutura, PNGs, dimensões, caption, acentos, fontes, placeholders, fotos, URLs

### validate_accents.py — Acentos PT-BR
```bash
python3 scripts/validate_accents.py output/posts/PASTA-DO-POST/html
```

### validate_fonts_html.py — Fontes mínimas
```bash
python3 scripts/validate_fonts_html.py output/posts/PASTA-DO-POST/html
```

---

## 10. Pipeline de Produção Completo

### Passo a passo para criar 1 carrossel:

#### 1. Pesquisar notícias
Peça ao Claude: "busca notícias virais de hoje"
- O agente pesquisa em 10+ fontes brasileiras
- Ranqueia por potencial viral (1-10)
- Sugere ângulos para carrossel

#### 2. Escolher tema e estilo
- Selecione a notícia ou tema
- Escolha o estilo (Twitter Dark, Esteter, Kaique Epic, etc.)

#### 3. Gerar imagens
O Claude automaticamente:
- Gera fotos IA via Nano Banana (prompts profissionais)
- Clona sua foto em cenários diferentes
- Baixa fotos editoriais reais das matérias (og:image)

#### 4. Criar slides
- Agente cria 10 HTMLs standalone
- Cada slide com layout único
- Fotos incorporadas com gradientes

#### 5. Renderizar
```bash
python3 scripts/render_slides.py output/posts/PASTA
```

#### 6. Verificar
O Claude verifica visualmente antes de mostrar.

#### 7. Publicar
Peça: "posta esse carrossel"
- Fecha Chrome
- Abre Instagram via Playwright
- Upload 10 slides → crop 4:5 → caption → Compartilhar

---

## 11. Geração de Imagens (Nano Banana)

### Estrutura do prompt perfeito
```
[STYLE] + [SUBJECT] + [COMPOSITION] + [LIGHTING] + [CAMERA] + [MOOD] + [ASPECT RATIO]
```

### 10 categorias de prompt pré-aprovadas
1. Trading / Mercado Financeiro
2. Breaking News / Urgência
3. Política / Poder
4. Economia / Dinheiro
5. Mindset / Psicologia
6. Tecnologia / IA
7. Crise / Caos
8. Escândalo / Investigação
9. Comparativo / Dados
10. CTA / Branding

### Dicas para foto viral
- Sempre especificar camera + lens (ex: "Shot on Canon EOS R5, 85mm f/1.4")
- Incluir iluminação específica (ex: "Rembrandt lighting", "golden hour")
- Film stock emulation (ex: "Kodak Portra 400", "Cinestill 800T")
- Anti-AI: "natural skin texture, visible pores, no airbrushing"
- Aspect ratio: "4:5 portrait"

---

## 12. Clone de Pessoa (Consistência Facial)

### Como funciona
1. Upload de 1-3 fotos de referência
2. Identity Header descreve a pessoa (rosto, barba, tatuagens, etc.)
3. Anti-AI block garante realismo
4. Prompt narrativo descreve o cenário
5. Gemini recria a pessoa no novo cenário

### Identity Header (editar para sua pessoa)
```
[IDENTITY — NOME]
Subject: Nome, nacionalidade, idade
Face: tom de pele, olhos, jaw, barba
Hair: cor, corte, textura
Build: tipo físico, ombros
Style: vestimenta padrão
Distinctive: tatuagens, cicatrizes, etc.
[END IDENTITY]
```

### 12 presets de cenário
trading-desk, office-ceo, podcast-studio, stage-speaker, casual-street, teaching-whiteboard, results-celebration, rooftop-night, home-content, thinking-window, market-stress, walking-office

### Dicas para melhor clone
- Use 3 fotos: frontal + 3/4 + ângulo diferente
- Fotos com boa luz e fundo limpo
- Resolução mínima 512x512
- Sem óculos escuros ou chapéu cobrindo rosto

---

## 13. Publicação no Instagram

### Via Playwright (método atual)
1. Fechar Chrome: `pkill -a "Google Chrome"`
2. O Claude abre Instagram via Playwright MCP
3. Loga automaticamente (sessão persistente)
4. Upload → Crop 4:5 → Sem filtro → Caption → Compartilhar

### Primeira vez
- O Playwright vai abrir o Chrome
- Você faz login manualmente no Instagram
- A sessão fica salva para próximas vezes

### Dicas
- SEMPRE fechar Chrome antes de abrir Playwright
- Se der erro, feche Chrome e tente de novo
- headless: false (precisa ver o browser)

---

## 14. Pesquisa de Notícias Virais

### Fontes recomendadas para público conservador
- Gazeta do Povo
- Revista Oeste
- Jovem Pan
- O Antagonista

### Fontes de mercado/economia
- InfoMoney
- Bloomberg Brasil
- Valor Econômico
- CNN Brasil

### Como pesquisar
Peça ao Claude: "busca notícias virais de hoje para @rubimfx"
- O agente usa WebSearch + research-analyst
- Busca em 10+ fontes simultaneamente
- Ranqueia por viral potential (1-10)
- Sugere ângulos de carrossel

### Dicas para viralizar
- Notícias com NÚMEROS ESPECÍFICOS (R$, %, quantidade)
- Escândalos com NOMES de pessoas/instituições
- Temas que conectam MACRO ao BOLSO do seguidor
- Screenshots e fotos REAIS de reportagem = credibilidade

---

## 15. Checklist de Qualidade

Antes de publicar, verifique:
- [ ] Fonte mínima 22px (nada abaixo de 20px)
- [ ] Fotos reais (nunca stock/Unsplash)
- [ ] profile-photo.jpeg sem ../
- [ ] Acentuação completa (á, é, í, ó, ú, ã, õ, ç)
- [ ] @rubimfx visível em todos os slides
- [ ] 1080x1350px
- [ ] HTML standalone (zero dependências externas)
- [ ] Headline com número/valor específico
- [ ] 7+ designs diferentes no carrossel
- [ ] CTA no último slide

---

## 16. Troubleshooting

### "Chrome não abre"
```bash
pkill -a "Google Chrome"
# Espere 2 segundos e tente de novo
```

### "Imagem não gerada"
- Verifique GOOGLE_API_KEY no .env
- Gemini bloqueia rostos de pessoas reais/famosas
- Tente outro prompt

### "Render falha"
- Verifique se http.server está livre (porta 8899)
- `lsof -i :8899` para ver se está ocupado
- `kill -9 PID` para liberar

### "Fontes pequenas"
- validate_fonts_html.py verifica automaticamente
- Mínimo: headlines 52px+, body 28px+, labels 22px+

### "pip install falha"
```bash
pip3 install google-genai --break-system-packages
```

---

## 17. FAQ

**Q: Quanto custa gerar imagens?**
A: ~US$0.07/imagem (~R$0.35). Um carrossel com 4 fotos IA custa ~R$1.40.

**Q: Funciona no Windows?**
A: Sim, mas os scripts são testados em macOS. Pode precisar ajustar paths.

**Q: Posso usar para outro nicho além de trading?**
A: Sim! Basta criar um novo squad com `/opensquad create` e configurar para seu nicho.

**Q: Preciso saber programar?**
A: Não. O Claude Code faz tudo. Você só precisa dar comandos em português.

**Q: Como adicionar um novo estilo de carrossel?**
A: Crie um novo template HTML em `templates/` seguindo o padrão dos existentes.

---

## 🎯 Resumo Rápido

Para criar e publicar um carrossel em 15 minutos:

1. `claude` → Abre o Claude Code
2. "busca notícias virais de hoje" → Pesquisa automática
3. Escolha o tema e estilo
4. "pode fazer" → Cria slides + imagens
5. "pode postar" → Publica no Instagram

É isso. O sistema faz o resto.

---

*Guia criado em 19 de março de 2026 por @rubimfx com Claude Code.*
