#!/usr/bin/env python3
"""Login @rubimfx com sessão persistente. Roda interativamente se precisar de 2FA."""
from instagrapi import Client
from pathlib import Path

SESSION_DIR = Path.home() / ".instagrapi"
SESSION_DIR.mkdir(parents=True, exist_ok=True)
SESSION_FILE = SESSION_DIR / "rubimfx.json"

# Device ID FIXO — reusar sempre o mesmo pra sessão durar mais
DEVICE = {
    'app_version': '269.0.0.18.75',
    'android_version': 31,
    'android_release': '12.0',
    'dpi': '640dpi',
    'resolution': '1440x2560',
    'manufacturer': 'samsung',
    'device': 'star2lte',
    'model': 'SM-G965F',
    'cpu': 'exynos9810',
    'version_code': '314665256',
}
UUIDS = {
    'phone_id': 'a1b2c3d4-e5f6-7890-abcd-ef1234567890',
    'uuid': 'f9e8d7c6-b5a4-3210-fedc-ba0987654321',
    'client_session_id': '11223344-5566-7788-99aa-bbccddeeff00',
    'advertising_id': 'aabbccdd-eeff-0011-2233-445566778899',
    'android_device_id': 'android-rubimfx2026fixed',
}

cl = Client()
cl.delay_range = [1, 2]
cl.set_device(DEVICE)
cl.set_uuids(UUIDS)

# Tentar reusar sessão salva
if SESSION_FILE.exists():
    try:
        cl.load_settings(SESSION_FILE)
        cl.get_timeline_feed()
        print("SESSÃO VÁLIDA — reutilizada com sucesso!")
        exit(0)
    except Exception:
        print("Sessão expirada, fazendo login novo...")

# Login
print("Fazendo login @rubimfx...")
try:
    cl.login("rubimfx", "Gabriel@2025")
    print("LOGIN OK sem 2FA!")
except Exception as e:
    if "two_factor" in str(e).lower():
        two_factor_id = cl.last_json.get("two_factor_info", {}).get("two_factor_identifier", "")
        if not two_factor_id:
            print(f"ERRO: Não obteve two_factor_identifier: {e}")
            exit(1)
        print("2FA necessário. Digite o código:")
        code = input("> ").strip()
        data = {
            "verification_code": code,
            "two_factor_identifier": two_factor_id,
            "username": "rubimfx",
            "device_id": cl.android_device_id,
            "verification_method": "0",
        }
        try:
            cl.private_request("accounts/two_factor_login/", data=data)
            print("2FA OK!")
        except Exception as e2:
            print(f"ERRO 2FA: {e2}")
            exit(1)
    else:
        print(f"ERRO: {e}")
        exit(1)

cl.dump_settings(SESSION_FILE)
print(f"SESSÃO SALVA em {SESSION_FILE}")
print("Próximas publicações vão reutilizar esta sessão automaticamente.")
