---
tags: [ai-import, sales, funnel, tech]
status: theory
source: Claude Cowork sessions "Quotation form Google Sheets integration" + "Launchpoint franchise PH market analysis"
imported: 2026-07-04
---

# Quotation Form → Sheets → Payment Flow

Flow: quote form → PDF download (with clickable "Move to Payment" button inside the PDF) → auto-save to Drive + log row to "ICEXPRESS QUOTATION" Sheet → redirect to Tally payment form (`https://tally.so/r/obp6o5`).

## Hard-won bugs & fixes

- **`keepalive: true` breaks big uploads** — browsers cap keepalive at ~64KB; PDF base64 is bigger, so the request silently failed. Fix: remove keepalive, use `mode: "no-cors"` + `text/plain` content type (Apps Script requirement), and redirect **after** upload finishes (15s safety net).
- **Apps Script "doesn't work" = stale deployment.** After editing Code.gs: Deploy → Manage deployments → pencil → Version: New version → Deploy. Verify via the `/exec` URL (should return the JSON status message).
- If `/exec` shows an authorization page: redeploy Execute as **Me**, access **Anyone**.
- `STORAGE_URL` in the landing page must hold the Web App URL for Drive + Sheet auto-save.

## Related

- [[Sessions Index]] · feeds [[Client Delivery System]] · [[Proposal SOP]]
