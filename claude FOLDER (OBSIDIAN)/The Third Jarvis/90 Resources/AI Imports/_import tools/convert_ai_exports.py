#!/usr/bin/env python3
"""
Convert ChatGPT / claude.ai data-export zips into Obsidian markdown notes.

Usage:
  python3 convert_ai_exports.py chatgpt-export.zip
  python3 convert_ai_exports.py claude-export.zip

Auto-detects which service the zip came from and writes one .md note per
conversation into ../ChatGPT/ or ../Claude.ai/ (next to this script).
"""
import json, re, sys, zipfile
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent

def safe_name(s, max_len=80):
    s = re.sub(r'[\\/:*?"<>|#^\[\]]', "", (s or "Untitled")).strip()
    return (s[:max_len] or "Untitled").rstrip(". ")

def ts(t):
    try:
        if isinstance(t, (int, float)):
            return datetime.fromtimestamp(t).strftime("%Y-%m-%d")
        return str(t)[:10]
    except Exception:
        return ""

def write_note(folder, title, date, source, parts):
    folder.mkdir(parents=True, exist_ok=True)
    body = "\n\n".join(parts).strip()
    fm = f"---\ntags: [ai-import, {source.lower().replace('.', '')}]\nsource: {source}\ndate: {date}\n---\n\n"
    path = folder / f"{safe_name(title)}.md"
    n = 2
    while path.exists():
        path = folder / f"{safe_name(title)} {n}.md"
        n += 1
    path.write_text(fm + f"# {title}\n\n" + body + "\n", encoding="utf-8")
    return path

def convert_chatgpt(convs):
    out = HERE.parent / "ChatGPT"
    count = 0
    for c in convs:
        title = c.get("title") or "Untitled"
        date = ts(c.get("create_time"))
        parts = []
        # walk mapping in insertion order; fall back to create_time sort
        msgs = []
        for node in (c.get("mapping") or {}).values():
            m = node.get("message")
            if not m:
                continue
            role = (m.get("author") or {}).get("role")
            content = m.get("content") or {}
            texts = [p for p in (content.get("parts") or []) if isinstance(p, str) and p.strip()]
            if role in ("user", "assistant") and texts:
                msgs.append((m.get("create_time") or 0, role, "\n".join(texts)))
        msgs.sort(key=lambda x: x[0])
        for _, role, text in msgs:
            label = "**You:**" if role == "user" else "**ChatGPT:**"
            parts.append(f"{label}\n{text}")
        if parts:
            write_note(out, title, date, "ChatGPT", parts)
            count += 1
    return count, out

def convert_claude(convs):
    out = HERE.parent / "Claude.ai"
    count = 0
    for c in convs:
        title = c.get("name") or "Untitled"
        date = ts(c.get("created_at"))
        parts = []
        for m in c.get("chat_messages") or []:
            text = m.get("text") or ""
            if not text.strip():
                continue
            label = "**You:**" if m.get("sender") == "human" else "**Claude:**"
            parts.append(f"{label}\n{text}")
        if parts:
            write_note(out, title, date, "Claude.ai", parts)
            count += 1
    return count, out

def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    zpath = Path(sys.argv[1]).expanduser()
    with zipfile.ZipFile(zpath) as z:
        name = next((n for n in z.namelist() if n.endswith("conversations.json")), None)
        if not name:
            sys.exit("No conversations.json found in zip — is this a ChatGPT/Claude data export?")
        convs = json.loads(z.read(name))
    first = convs[0] if convs else {}
    if "mapping" in first:
        count, out = convert_chatgpt(convs)
    elif "chat_messages" in first:
        count, out = convert_claude(convs)
    else:
        sys.exit("Unrecognized export format.")
    print(f"Imported {count} conversations into {out}")

if __name__ == "__main__":
    main()
