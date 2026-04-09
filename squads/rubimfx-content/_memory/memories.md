# Squad Memories — RubimFX Content OS

## Aprendizados
(Atualizado: 2 de abril de 2026 — 44 posts publicados)

---

### Agente Nara Notícia (reescrito 02/abr)
- Viralidade é o PRIMEIRO filtro (não relevância para trading)
- Twitter/X como fonte primária — buscar ANTES das fontes tradicionais
- Fontes em 5 tiers: Breaking (Twitter, Antagonista, JP) → Editoriais conservadores (Gazeta, Oeste) → Financeiros BR → Internacionais → Dados
- 5 critérios de scoring (max 25): Viral Potential, Debate, Dados Visuais, Relevância, Atualidade
- Categorias expandidas: politica-br, escandalo, tech-ia (não só trading)
- Escândalos com números (R$ bilhões, %) são os que mais viralizam

### Fotos reais de notícias (regra nova 02/abr)
- SEMPRE buscar og:image das matérias via Firecrawl
- Baixar e usar como: bg opacity 0.10-0.28, article card, hero
- Mínimo 3-4 fotos reais por carrossel
- Fotos de políticos/STF/PF > fotos genéricas de dinheiro

---

### Renderização (CRÍTICO)
- **Viewport DEVE ser 1080x1350** — se renderizar com viewport padrão sai 1200x1350 e Instagram corta os lados
- Usar `page.setViewportSize({ width: 1080, height: 1350 })` ANTES de qualquer screenshot
- `fullPage: false` — viewport only, não fullPage
- Servidor local deve rodar na pasta dos HTMLs (não na raiz do squad)
- Copiar profile-photo.jpeg pra mesma pasta dos HTMLs (paths relativos ../../assets/ não funcionam no http-server)

### Fotos Clone (Nano Banana)
- Script: `scripts/clone_image.py` com referência `assets/fotos-referencia/DSC04575.JPG`
- Presets disponíveis: trading-desk, office-ceo, podcast-studio, stage-speaker, casual-street, teaching-whiteboard, results-celebration, rooftop-night, home-content, thinking-window, market-stress, walking-office
- Custom scenes funcionam passando prompt narrativo direto (ex: boxing ring)
- API: Google Gemini (GOOGLE_API_KEY no .env)
- Custo: ~R$ 0,35/foto
- Gabriel prefere fotos dramáticas/cinematográficas (Kaique Epic style)
- SEMPRE gerar foto NOVA pra capa — reusar book nos demais

### Modelos que mais engajam
- **Kaique Epic** ⭐ — FAVORITO do Gabriel, melhor performance
  - Font: Anton (headlines) + Inter (body)
  - Permitido: Epic Cover, Tweet Card, Quote Card, CTA
  - Proibido: Header bar, grids 2x2, setas, Chrome Twitter
  - Accent: Amarelo #FFD600, Vermelho #FF3B30
- **Twitter Dark** — bom pra educacional/dados
- **Esteter Style** — bom pra notícias com prints reais

### Publicação Instagram
- SEMPRE fechar Chrome antes de abrir Playwright: `pkill -a "Google Chrome"`
- Login: rubimfx / Gabriel@2025 + 2FA (app autenticador)
- Fluxo: Novo post → Postar → Upload → Crop 4:5 → Avançar (filtros) → Avançar → Legenda → Compartilhar
- Threads e Facebook compartilham automaticamente (switches difíceis de desmarcar)
- Aguardar ~15s após clicar Compartilhar pra confirmação

### Conteúdo que funciona
- Notícias com números impactantes (R$ bilhões, %) geram alto salvamento
- Frases do Gabriel da sala ao vivo viram quotes poderosos
- Alternância visual dark/white é obrigatória (nunca 2 slides iguais seguidos)
- Mínimo de fontes: headlines 48-96px, body 26-30px, labels 20-22px
- Português CORRETO com acentos sempre (é, á, ã, õ, ç)

### Erros recorrentes a evitar
- NÃO misturar elementos entre modelos (regra absoluta)
- NÃO usar fullPage:true na renderização
- NÃO esquecer de copiar profile-photo.jpeg pro diretório dos HTMLs
- NÃO usar paths relativos ../../ — copiar assets pro local
- NÃO postar sem verificar dimensões (sips -g pixelWidth)
- NÃO deixar Chrome aberto quando for usar Playwright

### Pipeline de produção otimizado (tempo real)
1. Pesquisar notícia (WebSearch) — 5 min
2. Gabriel escolhe tema + modelo — checkpoint
3. Gerar fotos clone (clone_image.py) — 3 min (paralelo)
4. Criar 10 HTMLs (agente frontend) — 10 min
5. Subir http-server + setar viewport 1080x1350 — 1 min
6. Renderizar 10 PNGs (Playwright batch) — 2 min
7. Verificar dimensões (sips) — 1 min
8. Abrir pra Gabriel aprovar — checkpoint
9. Fechar Chrome + login Instagram + upload + legenda + publicar — 5 min
**Total: ~30 min por carrossel**

### Posts marcantes (referência)
- 2026-03-30 "Alta Performance" — Kaique Epic, clone boxing ring, 10 slides
- 2026-03-30 "Delação Banco Master" — Kaique Epic, foto real Vorcaro preso
- 2026-03-28 "Disciplina e Fé" — Kaique Epic, clone bíblico
- 2026-03-21 "8 Bombas Vorcaro" — alto engajamento, dados numéricos

### Temas com alto potencial viral
- Escândalos políticos com números (Banco Master, STF)
- Trading + mindset/fé (conexão pessoal do Gabriel)
- Comparações "antes vs depois"
- Notícias urgentes com foto de impacto
- Frases provocativas da sala ao vivo
