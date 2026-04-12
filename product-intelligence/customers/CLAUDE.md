# Customers

> Source of truth lives in Confluence: **Product Readiness Hub (PRH) > Customers folder**
> Confluence folder ID: `17748688902`
> Direct URL: https://alineops.atlassian.net/wiki/spaces/PRH/pages/17748688902

## Structure in Confluence

Each customer gets one page under the Customers folder. Call summaries are child pages.

```
Customers/
└── [Customer Name]/
    ├── Account Context        (contacts, use cases, goals, risks, open items)
    └── Calls/
        └── YYYY-MM-DD         (one page per call summary)
```

## How to Add a Customer

Run `/customer-call`. The skill checks if a customer page exists; if not, it creates one with the Account Context template before writing the call summary.

## How to Find a Customer

Use `confluence_search` with the customer name in space PRH, or `confluence_get_page_children` on parent `17748688902`.
