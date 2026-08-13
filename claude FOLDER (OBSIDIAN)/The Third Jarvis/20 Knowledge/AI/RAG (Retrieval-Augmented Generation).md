---
tags: [knowledge, ai]
status: theory
---

# RAG (Retrieval-Augmented Generation)

Pattern: instead of hoping the model "knows," you **retrieve relevant documents first** (search/embeddings) and feed them into the prompt.

Why it matters for us: it's how AI answers from *our* knowledge (this vault, client docs, SOPs) instead of generic training data.

- Docs → chunks → embeddings → vector database → similarity search → context in prompt
- Quality of chunks/notes matters more than the model — atomic, well-titled notes retrieve better (an argument for this vault's structure)
- Obsidian plugins like Smart Connections / Copilot do lightweight local RAG over the vault

## Related

- [[AI MOC]] · [[AI Agents]] · applied in [[Knowledge Base Build]]
