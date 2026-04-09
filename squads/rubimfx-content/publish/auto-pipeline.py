#!/usr/bin/env python3
"""
RubimFX Auto Pipeline — Roda o squad completo e manda pro Telegram pra aprovação.

Uso:
  python3 auto-pipeline.py                    # Notícia quente do dia
  python3 auto-pipeline.py --tema "live"      # Conteúdo da live
  python3 auto-pipeline.py --tema "educacional" # ICT/SMC educacional
  python3 auto-pipeline.py --tema "mindset"   # Mindset/alta performance

Fluxo:
  1. Pesquisa notícias (web search)
  2. Seleciona a mais viral
  3. Gera ângulo + copy (skills)
  4. Cria HTMLs + renderiza PNGs
  5. Manda pro Telegram pra aprovação
  6. Se aprovado → publica no Instagram
"""

import subprocess, sys, json, time, os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
PUBLISH_DIR = Path(__file__).parent
TELEGRAM_BOT = PUBLISH_DIR / "telegram-bot.py"
PUBLISH_SCRIPT = PUBLISH_DIR / "publish-rubimfx.py"


def run_claude(prompt):
    """Roda Claude Code como subprocesso pra executar o pipeline."""
    result = subprocess.run(
        ["claude", "-p", prompt, "--no-input"],
        capture_output=True, text=True, timeout=600,
        cwd=str(BASE_DIR)
    )
    return result.stdout, result.stderr, result.returncode


def send_telegram(text):
    """Envia mensagem pro Telegram."""
    import requests
    BOT_TOKEN = "8631398586:AAGpNKGafq_4GWGSH-5NG3rF33IBMs0CbOg"
    CHAT_ID = 737996107
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    )


def main():
    tema = "notícia quente do dia"
    if "--tema" in sys.argv:
        idx = sys.argv.index("--tema")
        tema = sys.argv[idx + 1]

    send_telegram(f"🚀 *Pipeline iniciado!*\nTema: {tema}\nAguarde...")

    # Gerar run ID
    run_id = time.strftime("%Y-%m-%d-%H%M%S")
    output_dir = BASE_DIR / "output" / run_id / "html"
    output_dir.mkdir(parents=True, exist_ok=True)
    post_dir = output_dir.parent

    prompt = f"""Você está no squad rubimfx-content. Execute o pipeline completo para criar UM post @rubimfx.

Tema: {tema}
Período: últimas 24h
Run ID: {run_id}

EXECUTE ESTES PASSOS NA ORDEM:

1. PESQUISAR notícias via web search (fontes: Gazeta do Povo, Revista Oeste, Jovem Pan, InfoMoney, O Antagonista). Busque as 5 mais virais de hoje.

2. SELECIONAR a notícia mais viral (maior potencial de engajamento: números impactantes, escândalo, debate, afeta o bolso).

3. CRIAR COPY dos 10 slides usando skills de copy:
   - Headlines com fórmulas (paradoxo, escala, pergunta, track record)
   - Hooks com 2+ gatilhos neurológicos
   - Blocos Lego (prova, contraste, future pacing)
   - 40-80 palavras por slide

4. CRIAR 10 HTMLs no modelo Twitter Dark (Dino):
   - Slide 1: Capa Breaking (tweet dark + 2 fotos + stats bar)
   - Slide 2: Tweet + Artigo branco
   - Slide 3: Screenshot reportagem (fundo claro)
   - Slide 4: Lista bullets dark
   - Slide 5: Número gigante
   - Slide 6: Citações/quotes
   - Slide 7: Comparativo antes vs depois
   - Slide 8: Screenshot reportagem 2 (fundo claro)
   - Slide 9: Conclusão + CTA
   - Slide 10: CTA gradiente

   CSS: Inter font, paleta (#000, #16181C, #F4212E, #1D9BF0, #00BA7C, #FFA500)
   Dimensões: 1080x1350px
   Fotos: buscar og:image reais das matérias via web fetch

5. SALVAR HTMLs em: squads/rubimfx-content/output/{run_id}/html/

6. RENDERIZAR PNGs via Playwright (viewport 1080x1350)

7. ESCREVER caption.txt em: squads/rubimfx-content/output/{run_id}/

NÃO publique no Instagram. Apenas crie os slides e caption.
Copie profile-photo.jpeg de templates/ pra pasta html/.
"""

    send_telegram("🔍 Pesquisando notícias + criando carrossel...")

    stdout, stderr, code = run_claude(prompt)

    if code != 0:
        send_telegram(f"❌ *Erro no pipeline:*\n```{stderr[:500]}```")
        return

    # Verificar se slides foram criados
    slides = sorted(Path(f"{BASE_DIR}/output/{run_id}/html").glob("slide-*.png"))
    if not slides:
        send_telegram("❌ *Erro:* Nenhum slide PNG gerado. Verifique manualmente.")
        return

    send_telegram(f"✅ *Post criado!* {len(slides)} slides. Enviando pra aprovação...")

    # Enviar pro Telegram pra aprovação
    actual_post_dir = f"{BASE_DIR}/output/{run_id}"
    result = subprocess.run(
        [sys.executable, str(TELEGRAM_BOT), "approve", actual_post_dir],
        capture_output=True, text=True, timeout=3700
    )
    print(result.stdout)


if __name__ == "__main__":
    main()
