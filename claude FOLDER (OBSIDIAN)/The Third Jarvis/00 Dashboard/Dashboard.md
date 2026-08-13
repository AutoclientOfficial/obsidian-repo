---
tags: [dashboard]
---

# 🏠 Business OS — Command Center

The single source of truth. AI tools read from and write to this vault; nothing important lives only in a chat thread.

> [!info] Live sections below need the **Dataview** plugin: Settings → Community plugins → Browse → "Dataview" → Install & Enable. Everything else works without it.

## 💼 Deal Pipeline

Pulled from client note frontmatter — update `stage` / `next_action` there, not here.

```dataview
TABLE stage AS Stage, next_action AS "Next action", deal_value AS Value
FROM "30 Businesses/Franchise Brokerage PH/Clients"
WHERE type = "client"
SORT file.name ASC
```

## 🚀 Active Projects

```dataview
TABLE file.mtime AS "Last touched"
FROM "80 Projects"
SORT file.mtime DESC
```

## 🧪 Hypotheses Being Tested — review monthly

Upgrade to `validated` with evidence (name the client/campaign), or archive if dead. See [[Epistemic Status Convention]].

```dataview
TABLE file.folder AS Area
FROM ""
WHERE status = "hypothesis"
SORT file.folder ASC
```

## 📚 Theory Backlog — imported, not yet tested

```dataview
LIST
FROM "20 Knowledge" OR "90 Resources"
WHERE status = "theory"
SORT file.name ASC
```

## ✅ Validated — proven by our own results

```dataview
LIST
FROM ""
WHERE status = "validated" AND file.name != "Epistemic Status Convention"
SORT file.name ASC
```

## 📥 Inbox — file these during Weekly Review

```dataview
LIST
FROM "_inbox"
SORT file.ctime DESC
```

## 🕐 Recently Updated

```dataview
TABLE file.mtime AS Modified, file.folder AS Folder
FROM ""
WHERE file.name != "Dashboard"
SORT file.mtime DESC
LIMIT 10
```

---

## Navigation

### Me

- [[Who is Thirdy]] · [[Operating Principles (Thirdy)]] · [[Business Priorities 2026]]

### Principles

- [[Business Principles]] · [[Marketing Principles]] · [[Sales Principles]] · [[AI Principles]] · [[Money Principles]]
- [[Epistemic Status Convention]] — theory / hypothesis / validated

### Knowledge (evergreen)

- [[AI MOC]] · [[Marketing MOC]] · [[Sales MOC]] · [[Strategy MOC]] · [[Life Coaching MOC]] · [[Mentorship MOC]]

### Businesses

- [[FBPH Index]] — Franchise Brokerage PH (clients: Eagles 4x4, IceXpress, SQOE…)
- [[NXT Gen Hex Overview]] — AI agency
- [[AutoClient Overview]] — lead gen system

### Machines

- `40 Systems` — repeatable machines · `50 Playbooks` — how-to guides · `60 SOPs` — processes · `70 Templates`

### Resources & Imports

- `90 Resources` — [[Prompt Library]], [[Framework Library]], AI Imports ([[ChatGPT Knowledge Index]], [[Sessions Index]])
- [[How to import ChatGPT & Claude exports]] · [[Connecting AI to this vault]]

### Housekeeping

- `_inbox` — dump anything, file later · `99 Archive` — [[Archive README|how to archive]]
