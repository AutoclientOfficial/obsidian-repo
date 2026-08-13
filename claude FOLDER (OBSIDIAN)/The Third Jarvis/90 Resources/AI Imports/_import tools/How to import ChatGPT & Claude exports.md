---
tags: [howto, ai-import]
---

# How to import ChatGPT & Claude exports

## Step 1 — Request your exports

**ChatGPT:** chatgpt.com → Settings → **Data controls** → **Export data**. A download link arrives by email (valid 24h). Download the zip.

**claude.ai:** claude.ai → Settings → **Privacy** → **Export data**. Same deal — zip arrives by email.

## Step 2 — Import into this vault

Easiest: start a Cowork session, drop the zip into the chat, and say *"import this into my Obsidian vault"*. Claude runs the converter and files everything.

Or run it yourself:

```bash
python3 "90 Resources/AI Imports/_import tools/convert_ai_exports.py" ~/Downloads/chatgpt-export.zip
```

One markdown note per conversation lands in `90 Resources/AI Imports/ChatGPT/` or `90 Resources/AI Imports/Claude.ai/`, tagged `#ai-import`.

## Step 3 — Distill

Raw chat logs are bulky. Ask Claude: *"read the new imports and distill the business knowledge into the right vault folders"* — the useful frameworks get promoted into `10 Business Core`, `40 Marketing`, etc., linked from [[Dashboard]].
