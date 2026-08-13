---
tags: [ai-import, sales, forms]
status: theory
source: Claude Cowork sessions "Client questionnaire planning" + "Sales data positioning"
imported: 2026-07-04
---

# Client Questionnaire & Sales Data Form

## Sales Data section (Tally build sheet)

18 questions total: 9 **Number** blocks (peso figures, percentages — items 2–9, 12, 16, 18) and 9 **Short answer** blocks (periods, seasons, links, Yes/No). Item 15 (Running Paid Ads?) works better as Multiple Choice Yes/No.

## Quiz funnel tech note

The client questionnaire quiz posts to Google Sheets via `SHEETS_WEBHOOK_URL` — the constant sits at the **top of the `<script>` block** (under the "QUIZ ENGINE" comment), not inside any function. Web app must be deployed with access = **Anyone** or rows won't log.

## Related

- [[Sessions Index]] · feeds [[FBPH Funnel and Lead Qualification System]]
