---
tags: [project, ai]
status: active
---

# Project: Jarvis AI

Vision: personal + business AI operator on top of this vault — vault as memory, MCP as hands, agents as workers ("The Third Jarvis").

⚠️ Stub — migrate Jarvis/Hermes planning from remaining ChatGPT parts.

Current foundation: vault connected to Claude (Cowork) · import pipeline live · [[MCP (Model Context Protocol)]] · [[AI Agents]]

## Local build v1 (2026-07-10)
Working local Jarvis app at `~/Jarvis` — chat UI at http://127.0.0.1:8765, launched via `Start Jarvis.command`.
- Memory: this vault, indexed live (edits picked up automatically)
- Brain: Claude Code CLI (`claude -p`, sonnet) — requires one-time `claude` → `/login` in Terminal
- Capture: "remember this" button saves answers to `_inbox/`
- Voice: 🎙 tap-to-talk (auto-sends) + 🔊 spoken replies (macOS "Daniel" en-GB voice, local) with hands-free follow-up loop
- Config (vault path, model, notes-per-question): top of `~/Jarvis/jarvis.py`
