#!/usr/bin/env python3
"""Publica carrossel no @rubimfx via Instagrapi. 2FA automático via TOTP."""
import sys, time, json, tempfile, shutil
from pathlib import Path
from PIL import Image
from instagrapi import Client
import pyotp

TOTP_SECRET = 'I3RPJBV2ATNOKQ4K2LBEGBJQIZCSF252'
SESSION_FILE = Path.home() / ".instagrapi" / "rubimfx.json"

DEVICE = {
    'app_version': '269.0.0.18.75', 'android_version': 31, 'android_release': '12.0',
    'dpi': '640dpi', 'resolution': '1440x2560', 'manufacturer': 'samsung',
    'device': 'star2lte', 'model': 'SM-G965F', 'cpu': 'exynos9810', 'version_code': '314665256',
}
UUIDS = {
    'phone_id': 'a1b2c3d4-e5f6-7890-abcd-ef1234567890',
    'uuid': 'f9e8d7c6-b5a4-3210-fedc-ba0987654321',
    'client_session_id': '11223344-5566-7788-99aa-bbccddeeff00',
    'advertising_id': 'aabbccdd-eeff-0011-2233-445566778899',
    'android_device_id': 'android-rubimfx2026fixed',
}


def get_client():
    cl = Client()
    cl.delay_range = [2, 4]
    cl.set_device(DEVICE)
    cl.set_uuids(UUIDS)

    # Tentar sessão salva primeiro
    if SESSION_FILE.exists():
        try:
            cl.load_settings(SESSION_FILE)
            cl.get_timeline_feed()
            print("SESSION: Reutilizada")
            return cl
        except Exception:
            print("SESSION: Expirada, relogando...")

    # Login com TOTP automático
    code = pyotp.TOTP(TOTP_SECRET).now()
    cl.login("rubimfx", "Gabriel@2025", verification_code=code)
    cl.dump_settings(SESSION_FILE)
    print("LOGIN: OK @rubimfx (2FA automático)")
    return cl


def publish(post_dir):
    post_dir = Path(post_dir)
    html_dir = post_dir / "html" if (post_dir / "html").exists() else post_dir

    slides = sorted(html_dir.glob("slide-*.png"))
    if not slides:
        print(f"ERRO: Nenhum slide PNG em {html_dir}")
        sys.exit(1)
    print(f"SLIDES: {len(slides)}")

    caption = ""
    for name in ["caption.txt", "caption.md"]:
        cap_file = post_dir / name
        if cap_file.exists():
            caption = cap_file.read_text("utf-8").strip()
            break
    print(f"CAPTION: {len(caption)} chars")

    cl = get_client()

    tmp_dir = Path(tempfile.mkdtemp(prefix="instagrapi-"))
    jpeg_paths = []
    for s in slides:
        jpg_path = tmp_dir / (s.stem + ".jpg")
        Image.open(s).convert("RGB").save(jpg_path, "JPEG", quality=95)
        jpeg_paths.append(str(jpg_path))

    print("PUBLICANDO...")
    media = cl.album_upload(paths=jpeg_paths, caption=caption)
    url = f"https://www.instagram.com/p/{media.code}/"
    print(f"POST PUBLICADO! {url}")

    log = {"publishedAt": time.strftime("%Y-%m-%dT%H:%M:%S"), "url": url, "account": "rubimfx", "slides": len(slides)}
    (post_dir / "publish-log.json").write_text(json.dumps(log, indent=2))
    shutil.rmtree(tmp_dir, ignore_errors=True)
    return url


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 publish-rubimfx.py <pasta-do-post>")
        sys.exit(1)
    publish(sys.argv[1])
