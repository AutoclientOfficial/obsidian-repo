---
tags: [howto, ai-setup]
---

# Connecting AI to this vault

Vault location: `~/odysseus/integrations/claude/The Third Jarvis`

## 1. Claude (Cowork) — already works ✅

In any Cowork session, connect the folder `~/odysseus/integrations/claude` (or the vault folder directly). Claude then reads and writes your notes natively — no plugin needed. Useful prompts:

- "Read my FBPH Knowledge Base note before answering"
- "Save this as a note in 40 Marketing"
- "Update the brand profile for X in 20 Brands"

## 2. Claude Desktop chat (outside Cowork) — MCP

To let regular Claude chats search the vault, add an Obsidian MCP server: Claude Desktop → Settings → Extensions/Connectors → add **Filesystem** pointing at the vault folder, or install an Obsidian MCP (e.g. `mcp-obsidian`, needs the **Local REST API** community plugin in Obsidian).

## 3. AI inside Obsidian — community plugins

Settings → Community plugins → Browse:

- **Copilot** — chat with your vault; add your Anthropic and/or OpenAI API key. Supports "chat with all notes" (RAG).
- **Smart Connections** — automatic related-notes + local embeddings search.

You already have **Templater** and **Importer** installed. (Importer can also ingest ChatGPT exports directly if you prefer it over the script.)

## 4. ChatGPT

ChatGPT can't read local folders natively. Workarounds:

- Create a ChatGPT **Project** and upload key notes (e.g. the FBPH Knowledge Base) as files; re-upload when they change.
- Or keep ChatGPT for drafting and paste results into `_inbox` for filing.

## Rule of thumb

This vault is the **single source of truth**. AI tools read from it and write back to it; nothing important lives only inside a chat thread.

## Related

- [[How to import ChatGPT & Claude exports]] · [[MCP (Model Context Protocol)]]
