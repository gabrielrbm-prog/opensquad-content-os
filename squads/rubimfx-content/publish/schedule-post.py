#!/usr/bin/env python3
"""
Agenda um post aprovado pra publicação automática.

Uso:
  python3 schedule-post.py <pasta-do-post> <data-hora>
  python3 schedule-post.py <pasta-do-post> "2026-04-10T08:03:00"
  python3 schedule-post.py <pasta-do-post> "amanha 14h"
  python3 schedule-post.py <pasta-do-post> "hoje 20h"
"""

import sys, json, uuid
from pathlib import Path
from datetime import datetime, timedelta, timezone

BRT = timezone(timedelta(hours=-3))
SCHEDULE_FILE = Path(__file__).parent / "schedule.json"


def parse_time(time_str):
    """Parse tempo flexível."""
    now = datetime.now(BRT)

    if "amanha" in time_str.lower() or "amanhã" in time_str.lower():
        base = now + timedelta(days=1)
    elif "hoje" in time_str.lower():
        base = now
    else:
        try:
            return datetime.fromisoformat(time_str).replace(tzinfo=BRT)
        except:
            base = now

    # Extrair hora
    import re
    match = re.search(r"(\d{1,2})h", time_str)
    if match:
        hour = int(match.group(1))
        return base.replace(hour=hour, minute=3, second=0, microsecond=0)

    return base


def schedule(post_dir, scheduled_at):
    post_dir = Path(post_dir).resolve()

    # Ler título do caption
    title = "Post sem título"
    for name in ["caption.txt", "caption.md"]:
        cap = post_dir / name
        if cap.exists():
            first_line = cap.read_text("utf-8").strip().split("\n")[0][:80]
            title = first_line
            break

    # Contar slides
    html_dir = post_dir / "html" if (post_dir / "html").exists() else post_dir
    slides = len(list(html_dir.glob("slide-*.png")))

    # Adicionar ao schedule
    schedule = json.loads(SCHEDULE_FILE.read_text("utf-8"))
    post_entry = {
        "id": str(uuid.uuid4())[:8],
        "title": title,
        "post_dir": str(post_dir),
        "slides": slides,
        "scheduled_at": scheduled_at.isoformat(),
        "status": "approved",
        "created_at": datetime.now(BRT).isoformat(),
        "published_at": None,
        "url": None
    }
    schedule["posts"].append(post_entry)
    SCHEDULE_FILE.write_text(json.dumps(schedule, indent=2, ensure_ascii=False))

    print(f"✅ Post agendado!")
    print(f"   Título: {title}")
    print(f"   Slides: {slides}")
    print(f"   Horário: {scheduled_at.strftime('%d/%m/%Y %H:%M')} BRT")
    print(f"   ID: {post_entry['id']}")
    return post_entry


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    post_dir = sys.argv[1]
    time_str = " ".join(sys.argv[2:])
    dt = parse_time(time_str)
    schedule(post_dir, dt)
