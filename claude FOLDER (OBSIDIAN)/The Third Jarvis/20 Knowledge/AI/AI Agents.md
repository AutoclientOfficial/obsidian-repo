---
tags: [knowledge, ai]
status: theory
---

# AI Agents

An agent = LLM + tools + a loop (perceive → decide → act → observe). Differs from a chatbot: it takes actions (search, write files, call APIs), not just replies.

Key design lessons:

- **Narrow scope wins.** One agent that qualifies leads well beats one "do-everything" agent.
- **Tools define capability**; the model defines judgment.
- **Human-in-the-loop for irreversible actions** (payments, sending messages to clients).
- **Memory/knowledge base makes agents compound** — this vault is the memory layer for the Jarvis vision.

Business applications: lead qualification, follow-up sequencing, report generation, booking, CRM hygiene.

## Related

- [[AI MOC]] · [[MCP (Model Context Protocol)]] · [[AI Automation Stack]] · applied in [[Jarvis AI]]
