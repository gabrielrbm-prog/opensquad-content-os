#!/usr/bin/env python3
"""
Instagram Publisher via Instagrapi (multi-perfil)

Uso:
  python3 instagrapi-publish.py <post_dir> --account <username>
  python3 instagrapi-publish.py --save-session <user> <pass>
"""

import os
import sys
import json
import time
from pathlib import Path

SESSION_DIR = Path.home() / ".instagrapi"


def get_session_file(username):
    return SESSION_DIR / f"{username}.json"


def get_client(username=None, password=None):
    from instagrapi import Client

    cl = Client()
    cl.delay_range = [2, 5]

    session_file = get_session_file(username) if username else None

    if session_file and session_file.exists():
        try:
            cl.load_settings(session_file)
            cl.login(username, password) if password else cl.login_by_sessionid(
                cl.settings.get("authorization_data", {}).get("sessionid", "")
            )
            cl.get_timeline_feed()
            print(f"SESSION: Reutilizando sessão de @{username}")
            return cl
        except Exception as e:
            print(f"SESSION: Sessão expirada ({e}), fazendo login...")

    if not username or not password:
        username = username or os.environ.get("INSTA_USER")
        password = password or os.environ.get("INSTA_PASS")

    if not username or not password:
        print("ERRO: Credenciais necessárias.")
        sys.exit(1)

    try:
        cl.login(username, password)
        print(f"LOGIN: OK como @{username}")

        SESSION_DIR.mkdir(parents=True, exist_ok=True)
        sf = get_session_file(username)
        cl.dump_settings(sf)
        print(f"SESSION: Salva em {sf}")

        return cl
    except Exception as e:
        print(f"LOGIN ERRO: {e}")
        sys.exit(1)


def publish_carousel(post_dir, username, password=None):
    post_dir = Path(post_dir)

    slides = sorted(post_dir.glob("slide-*.png"))
    if not slides:
        html_dir = post_dir / "html"
        if html_dir.exists():
            slides = sorted(html_dir.glob("slide-*.png"))

    if not slides:
        print(f"ERRO: Nenhum slide PNG encontrado em {post_dir}")
        sys.exit(1)

    print(f"SLIDES: {len(slides)} encontrados")
    for s in slides:
        print(f"  {s.name} ({s.stat().st_size // 1024}KB)")

    # Ler caption
    caption = ""
    caption_path = post_dir / "caption.txt"
    if not caption_path.exists():
        caption_path = post_dir / "caption.md"
    if caption_path.exists():
        import re
        raw = caption_path.read_text("utf-8").strip()
        sections = re.split(r'\n## (Hashtags|Primeira linha|Meta)', raw)
        caption = sections[0]
        caption = re.sub(r'^#{1,6}\s+.*$', '', caption, flags=re.MULTILINE)
        caption = re.sub(r'^---+$', '', caption, flags=re.MULTILINE)
        caption = re.sub(r'^\s*>\s*', '', caption, flags=re.MULTILINE)
        caption = caption.replace('**', '').replace('__', '').replace('*', '')
        caption = re.sub(r'\n{3,}', '\n\n', caption).strip()
        hashtags = ""
        for i, section in enumerate(sections):
            if section == "Hashtags" and i + 1 < len(sections):
                hashtags = sections[i + 1].strip().split("\n")[0].strip()
        if hashtags:
            caption = caption + "\n\n" + hashtags
        if len(caption) > 2200:
            caption = caption[:2190] + "..."
        print(f"CAPTION: {len(caption)} chars")
    else:
        print("AVISO: Sem caption, publicando sem legenda")

    cl = get_client(username, password)

    # PNG → JPEG
    from PIL import Image
    import tempfile
    tmp_dir = Path(tempfile.mkdtemp(prefix="instagrapi-"))
    jpeg_paths = []
    for s in slides:
        jpg_path = tmp_dir / (s.stem + ".jpg")
        img = Image.open(s).convert("RGB")
        img.save(jpg_path, "JPEG", quality=95)
        jpeg_paths.append(str(jpg_path))
        print(f"  → {jpg_path.name} ({jpg_path.stat().st_size // 1024}KB)")

    print(f"\nPUBLICANDO carrossel @{username} com {len(jpeg_paths)} slides...")

    try:
        media = cl.album_upload(paths=jpeg_paths, caption=caption)
        print(f"\n=== POST PUBLICADO COM SUCESSO! ===")
        print(f"URL: https://www.instagram.com/p/{media.code}/")

        log = {
            "publishedAt": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "mediaId": str(media.id),
            "code": media.code,
            "url": f"https://www.instagram.com/p/{media.code}/",
            "account": username,
            "slides": len(slides),
            "method": "instagrapi",
        }
        log_path = post_dir / "publish-log.json"
        log_path.write_text(json.dumps(log, indent=2, ensure_ascii=False))
        return True
    except Exception as e:
        print(f"\nERRO: {type(e).__name__}: {e}")
        return False
    finally:
        import shutil
        try:
            shutil.rmtree(tmp_dir)
        except:
            pass


def save_session(username, password):
    get_client(username, password)
    print(f"Sessão de @{username} salva com sucesso!")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    if sys.argv[1] == "--save-session":
        if len(sys.argv) < 4:
            print("Uso: --save-session <user> <pass>")
            sys.exit(1)
        save_session(sys.argv[2], sys.argv[3])
    else:
        post_dir = sys.argv[1]
        username = None
        password = None
        if "--account" in sys.argv:
            idx = sys.argv.index("--account")
            username = sys.argv[idx + 1]
        if "--login" in sys.argv:
            idx = sys.argv.index("--login")
            username = sys.argv[idx + 1]
            password = sys.argv[idx + 2]
        if not username:
            print("ERRO: Use --account <username>")
            sys.exit(1)
        success = publish_carousel(post_dir, username, password)
        sys.exit(0 if success else 1)
