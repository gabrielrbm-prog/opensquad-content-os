#!/usr/bin/env python3
"""
RubimFX Telegram Approval Bot
Envia preview de posts pro Gabriel aprovar antes de publicar no Instagram.

Uso:
  # Enviar post pra aprovação:
  python3 telegram-bot.py send <pasta-do-post>

  # Rodar bot ouvindo respostas (polling):
  python3 telegram-bot.py listen

  # Enviar + esperar aprovação (blocking):
  python3 telegram-bot.py approve <pasta-do-post>
"""

import sys, json, time, os, glob
from pathlib import Path
import requests

BOT_TOKEN = "8631398586:AAGpNKGafq_4GWGSH-5NG3rF33IBMs0CbOg"
CHAT_ID = 737996107
API = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_message(text, reply_markup=None):
    data = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    if reply_markup:
        data["reply_markup"] = json.dumps(reply_markup)
    return requests.post(f"{API}/sendMessage", data=data).json()


def send_photo(photo_path, caption=""):
    with open(photo_path, "rb") as f:
        data = {"chat_id": CHAT_ID, "caption": caption[:1024], "parse_mode": "Markdown"}
        return requests.post(f"{API}/sendPhoto", files={"photo": f}, data=data).json()


def send_media_group(photo_paths):
    """Envia grupo de fotos (álbum)."""
    media = []
    files = {}
    for i, path in enumerate(photo_paths[:10]):
        key = f"photo{i}"
        media.append({"type": "photo", "media": f"attach://{key}"})
        files[key] = open(path, "rb")

    data = {"chat_id": CHAT_ID, "media": json.dumps(media)}
    resp = requests.post(f"{API}/sendMediaGroup", data=data, files=files).json()

    for f in files.values():
        f.close()
    return resp


def send_post_for_approval(post_dir):
    """Envia slides + caption pro Telegram pra aprovação."""
    post_dir = Path(post_dir)
    html_dir = post_dir / "html" if (post_dir / "html").exists() else post_dir

    # Slides
    slides = sorted(html_dir.glob("slide-*.png"))
    if not slides:
        print("ERRO: Nenhum slide PNG encontrado")
        return False

    # Caption
    caption = ""
    for name in ["caption.txt", "caption.md"]:
        cap_file = post_dir / name
        if cap_file.exists():
            caption = cap_file.read_text("utf-8").strip()
            break

    # Enviar header
    send_message(f"📸 *NOVO POST @rubimfx* — {len(slides)} slides\n\nRevisando para aprovação...")

    # Enviar slides em grupos de 10
    for i in range(0, len(slides), 10):
        batch = [str(s) for s in slides[i:i+10]]
        send_media_group(batch)
        time.sleep(1)

    # Enviar caption
    if caption:
        # Telegram max message: 4096 chars
        if len(caption) > 4000:
            caption = caption[:3990] + "..."
        send_message(f"✍️ *CAPTION:*\n\n{caption}")

    # Enviar botões de aprovação
    keyboard = {
        "inline_keyboard": [
            [
                {"text": "✅ APROVAR E PUBLICAR", "callback_data": f"approve:{post_dir}"},
                {"text": "🔄 PEDIR AJUSTES", "callback_data": f"adjust:{post_dir}"}
            ],
            [
                {"text": "❌ REJEITAR", "callback_data": f"reject:{post_dir}"}
            ]
        ]
    }
    send_message("👆 *O que você quer fazer?*", reply_markup=keyboard)

    # Salvar estado
    state = {"status": "pending", "post_dir": str(post_dir), "sent_at": time.strftime("%Y-%m-%dT%H:%M:%S")}
    (post_dir / "telegram-state.json").write_text(json.dumps(state, indent=2))

    print(f"POST ENVIADO pro Telegram! {len(slides)} slides + caption")
    return True


def wait_for_approval(post_dir, timeout=3600):
    """Espera aprovação no Telegram (polling). Retorna: 'approved', 'adjust:feedback', 'rejected', 'timeout'."""
    post_dir = Path(post_dir)
    last_update_id = 0

    # Limpar updates antigos
    resp = requests.get(f"{API}/getUpdates", params={"offset": -1}).json()
    if resp.get("result"):
        last_update_id = resp["result"][-1]["update_id"] + 1

    start = time.time()
    print("Aguardando resposta no Telegram...")

    while time.time() - start < timeout:
        resp = requests.get(f"{API}/getUpdates", params={"offset": last_update_id, "timeout": 30}).json()

        for update in resp.get("result", []):
            last_update_id = update["update_id"] + 1

            # Callback query (botão clicado)
            cb = update.get("callback_query")
            if cb:
                data = cb.get("data", "")
                # Responder callback
                requests.post(f"{API}/answerCallbackQuery", data={"callback_query_id": cb["id"]})

                if data.startswith("approve:"):
                    send_message("✅ *APROVADO!* Publicando no Instagram...")
                    state = {"status": "approved", "approved_at": time.strftime("%Y-%m-%dT%H:%M:%S")}
                    (post_dir / "telegram-state.json").write_text(json.dumps(state, indent=2))
                    return "approved"

                elif data.startswith("adjust:"):
                    send_message("🔄 *Ok, me manda o feedback:*\nDigita o que quer ajustar.")
                    # Esperar mensagem de texto com feedback
                    feedback = wait_for_text(last_update_id, timeout=300)
                    state = {"status": "adjust", "feedback": feedback, "at": time.strftime("%Y-%m-%dT%H:%M:%S")}
                    (post_dir / "telegram-state.json").write_text(json.dumps(state, indent=2))
                    return f"adjust:{feedback}"

                elif data.startswith("reject:"):
                    send_message("❌ *Rejeitado.* Post descartado.")
                    state = {"status": "rejected", "at": time.strftime("%Y-%m-%dT%H:%M:%S")}
                    (post_dir / "telegram-state.json").write_text(json.dumps(state, indent=2))
                    return "rejected"

            # Mensagem de texto (resposta direta)
            msg = update.get("message", {})
            text = msg.get("text", "").strip().lower()
            if text in ["ok", "aprova", "publica", "sim", "vai", "bora", "go"]:
                send_message("✅ *APROVADO!* Publicando no Instagram...")
                state = {"status": "approved", "approved_at": time.strftime("%Y-%m-%dT%H:%M:%S")}
                (post_dir / "telegram-state.json").write_text(json.dumps(state, indent=2))
                return "approved"

    return "timeout"


def wait_for_text(last_update_id, timeout=300):
    """Espera uma mensagem de texto do usuário."""
    start = time.time()
    while time.time() - start < timeout:
        resp = requests.get(f"{API}/getUpdates", params={"offset": last_update_id, "timeout": 15}).json()
        for update in resp.get("result", []):
            last_update_id = update["update_id"] + 1
            msg = update.get("message", {})
            text = msg.get("text", "")
            if text:
                return text
    return ""


def approve_and_publish(post_dir):
    """Fluxo completo: envia pro Telegram, espera aprovação, publica."""
    if not send_post_for_approval(post_dir):
        return False

    result = wait_for_approval(post_dir)

    if result == "approved":
        # Publicar no Instagram
        print("Publicando no Instagram...")
        import subprocess
        publish_script = Path(__file__).parent / "publish-rubimfx.py"
        proc = subprocess.run(
            [sys.executable, str(publish_script), str(post_dir)],
            capture_output=True, text=True
        )
        print(proc.stdout)
        if proc.returncode == 0:
            # Extrair URL do output
            for line in proc.stdout.split("\n"):
                if "instagram.com/p/" in line:
                    url = line.split("!")[-1].strip()
                    send_message(f"🎉 *POST PUBLICADO!*\n\n{url}")
                    break
            return True
        else:
            send_message(f"❌ *Erro na publicação:*\n```{proc.stderr[:500]}```")
            return False

    elif result.startswith("adjust:"):
        feedback = result.split(":", 1)[1]
        send_message(f"📝 *Feedback recebido:* {feedback}\n\nVou ajustar e enviar de novo.")
        print(f"FEEDBACK: {feedback}")
        return False

    elif result == "rejected":
        print("Post rejeitado.")
        return False

    else:
        send_message("⏰ *Timeout* — nenhuma resposta em 1 hora. Post não publicado.")
        print("Timeout.")
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "send":
        send_post_for_approval(sys.argv[2])

    elif cmd == "listen":
        print("Bot ouvindo... (Ctrl+C pra parar)")
        wait_for_approval(sys.argv[2] if len(sys.argv) > 2 else ".")

    elif cmd == "approve":
        approve_and_publish(sys.argv[2])

    elif cmd == "test":
        send_message("🧪 Teste do bot! Se você recebeu isso, tá funcionando.")

    else:
        print(f"Comando desconhecido: {cmd}")
        print(__doc__)
