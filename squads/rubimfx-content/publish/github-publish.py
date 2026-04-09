#!/usr/bin/env python3
"""
GitHub Actions Publisher — Publica o próximo post agendado da fila.

Lê schedule.json pra saber qual post publicar agora.
Envia notificação pro Telegram após publicar.
"""

import os, sys, json, time, glob
from pathlib import Path
from datetime import datetime, timezone, timedelta

# Timezone Brasil
BRT = timezone(timedelta(hours=-3))


def get_instagram_client():
    """Login no Instagram com TOTP automático."""
    from instagrapi import Client
    import pyotp

    user = os.environ["INSTA_USER"]
    password = os.environ["INSTA_PASS"]
    totp_secret = os.environ["TOTP_SECRET"]

    cl = Client()
    cl.delay_range = [2, 4]

    code = pyotp.TOTP(totp_secret).now()
    cl.login(user, password, verification_code=code)
    print(f"LOGIN OK @{user}")
    return cl


def send_telegram(text):
    """Notifica no Telegram."""
    import requests
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "")
    if token and chat_id:
        requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data={"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
        )


def find_next_post():
    """Encontra o próximo post pra publicar baseado no schedule.json."""
    base = Path(__file__).parent.parent
    schedule_file = base / "publish" / "schedule.json"

    if not schedule_file.exists():
        print("ERRO: schedule.json não encontrado")
        return None

    schedule = json.loads(schedule_file.read_text("utf-8"))
    now = datetime.now(BRT)

    for post in schedule.get("posts", []):
        if post.get("status") != "approved":
            continue

        scheduled_time = datetime.fromisoformat(post["scheduled_at"])
        # Publicar se está na janela (até 30 min após horário agendado)
        diff = (now - scheduled_time).total_seconds()
        if -300 <= diff <= 1800:  # 5 min antes até 30 min depois
            return post

    # Se não encontrou na janela exata, publicar o próximo aprovado que ainda não foi publicado
    for post in schedule.get("posts", []):
        if post.get("status") == "approved":
            return post

    print("Nenhum post aprovado na fila.")
    return None


def publish_post(post_info):
    """Publica um post no Instagram."""
    from PIL import Image
    import tempfile, shutil

    post_dir = Path(post_info["post_dir"])
    html_dir = post_dir / "html" if (post_dir / "html").exists() else post_dir

    slides = sorted(html_dir.glob("slide-*.png"))
    if not slides:
        print(f"ERRO: Sem slides em {html_dir}")
        return False

    # Caption
    caption = ""
    for name in ["caption.txt", "caption.md"]:
        cap_file = post_dir / name
        if cap_file.exists():
            caption = cap_file.read_text("utf-8").strip()
            break

    print(f"SLIDES: {len(slides)} | CAPTION: {len(caption)} chars")

    # Login Instagram
    cl = get_instagram_client()

    # PNG → JPEG
    tmp_dir = Path(tempfile.mkdtemp(prefix="gh-publish-"))
    jpeg_paths = []
    for s in slides:
        jpg_path = tmp_dir / (s.stem + ".jpg")
        Image.open(s).convert("RGB").save(jpg_path, "JPEG", quality=95)
        jpeg_paths.append(str(jpg_path))

    # Publicar
    print("PUBLICANDO...")
    media = cl.album_upload(paths=jpeg_paths, caption=caption)
    url = f"https://www.instagram.com/p/{media.code}/"
    print(f"POST PUBLICADO! {url}")

    # Notificar Telegram
    send_telegram(f"✅ *Post publicado automaticamente!*\n\n📸 {len(slides)} slides\n🔗 {url}")

    # Atualizar schedule
    update_schedule(post_info["id"], "published", url)

    shutil.rmtree(tmp_dir, ignore_errors=True)
    return True


def update_schedule(post_id, status, url=""):
    """Atualiza o status de um post no schedule.json."""
    base = Path(__file__).parent.parent
    schedule_file = base / "publish" / "schedule.json"

    schedule = json.loads(schedule_file.read_text("utf-8"))
    for post in schedule.get("posts", []):
        if post["id"] == post_id:
            post["status"] = status
            post["published_at"] = time.strftime("%Y-%m-%dT%H:%M:%S-03:00")
            post["url"] = url
            break

    schedule_file.write_text(json.dumps(schedule, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    post = find_next_post()
    if post:
        print(f"Publicando: {post.get('title', post['id'])}")
        success = publish_post(post)
        if not success:
            send_telegram(f"❌ *Erro na publicação agendada:* {post.get('title', post['id'])}")
            sys.exit(1)
    else:
        print("Nada pra publicar agora.")
