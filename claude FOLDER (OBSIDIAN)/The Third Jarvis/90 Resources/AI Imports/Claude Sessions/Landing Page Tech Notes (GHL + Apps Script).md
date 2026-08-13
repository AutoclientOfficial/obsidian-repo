---
tags: [ai-import, tech, funnel, ghl]
status: theory
source: Claude Cowork sessions "Franchise event landing page" + "Business expansion landing page"
imported: 2026-07-04
---

# Landing Page Tech Notes (GHL + Apps Script)

## GHL full-bleed embed

To make custom HTML stretch edge-to-edge inside GoHighLevel's centered column: wrap the page in a container using the `100vw` + negative-margin technique, add `overflow-x:hidden`. Paste into a **full-width row** with row/column padding 0; if a gutter remains, zero the section's horizontal padding too.

## Apps Script backend (assessment funnel)

Business-expansion assessment posts to a Google Sheet ("Assessment Submissions" tab) + email notification. Standard failure mode: web app not redeployed with access = **Anyone**. Always test end-to-end: submit test data → check Sheet row + email.

## Related

- [[Sessions Index]] · pairs with [[Landing Page Copy Rules]] · [[How to Build a Funnel]]
