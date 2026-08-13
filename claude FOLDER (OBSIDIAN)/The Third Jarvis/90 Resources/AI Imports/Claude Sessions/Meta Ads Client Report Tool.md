---
tags: [ai-import, marketing, ads, tool]
status: theory
source: Claude Cowork session "Marketing report HTML template"
imported: 2026-07-04
---

# Meta Ads Client Report Tool

HTML tool that turns Meta Ads CSV exports into client-ready reports.

## How it works

1. Upload this month's Meta CSV ("This period") and optionally last month's ("Last period")
2. Client name + date range auto-fill → Generate
3. Outputs KPI cards (Reach, Impressions, Website Schedules, Messaging conversations, Spend, Cost/Result), a green/red "% improvement vs last period" chart, and an ad-set breakdown table
4. Auto-writes the client message in Meta terms — English/Taglish toggle, editable
5. Download as PNG or copy to clipboard

## Notes

- Reads Meta's exact column names (Amount spent (PHP), Results + Result indicator, ROAS…), totals multi-ad-set rows, auto-detects result type
- Built around conversions/messaging, not CTR (exports had no clicks column)
- Possible upgrades: Purchases/ROAS KPI cards, logo upload

## Related

- [[Sessions Index]] · feeds [[Reporting System]] · [[Facebook Ads Essentials]]
