# KPI Framework - PequeShop

## KPI Tree (Executive Level)

```
                         ┌─────────────────┐
                         │     REVENUE     │
                         └────────┬────────┘
            ┌────────────────────┼────────────────────┐
            ▼                    ▼                    ▼
    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
    │    Traffic   │    │  Conversion  │    │     AOV      │
    └──────────────┘    └──────────────┘    └──────────────┘

                       ┌─────────────────┐
                       │  PROFITABILITY  │
                       └────────┬────────┘
            ┌────────────────────┼────────────────────┐
            ▼                    ▼                    ▼
    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
    │     CAC      │    │Revenue Churn │    │  Elasticity  │
    └──────────────┘    └──────────────┘    └──────────────┘
```

---

## 1️⃣ Acquisition & Traffic

**Objetivo:** Atraer usuarios con intención de compra

| KPI | Formula | Target | Frequency |
|-----|---------|--------|-----------|
| Traffic by Channel | Sessions per source | Monitor | Weekly |
| CAC | Marketing Spend / New Customers | < $8,000 CLP | Monthly |
| New Customer Rate | New / Total Customers | > 20% | Monthly |
| Cost per Click (CPC) | Ad Spend / Clicks | < $200 CLP | Weekly |

### CAC Calculation Note

**Formula applied:**
```
CAC = Paid Media Spend / New Customers
```

**Scope limitation:** 
CAC was estimated using paid media spend only. A production implementation would include sales team costs, marketing tools, and attributed overhead.

**Channels tracked:**
- MercadoLibre Ads
- Google Ads  
- Facebook Ads
- Instagram Ads

---

## 2️⃣ Conversion & Funnel

**Objetivo:** Transformar visitas en ventas

| KPI | Formula | Target | Frequency |
|-----|---------|--------|-----------|
| Conversion Rate | Orders / Sessions | > 2.5% | Weekly |
| Cart Abandonment | Abandoned / Started Carts | < 70% | Weekly |
| AOV (Average Order Value) | Revenue / Orders | > $15,000 CLP | Weekly |
| Units per Transaction | Total Units / Transactions | > 1.5 | Monthly |

### Funnel Stages

```
Visitors → Product Views → Add to Cart → Checkout → Purchase
  100%        60%             25%          15%        2.5%
```

---

## 3️⃣ Customer Experience & Retention

**Objetivo:** Que el cliente vuelva

| KPI | Formula | Target | Frequency |
|-----|---------|--------|-----------|
| NPS | %Promoters - %Detractors | > 50 | Monthly |
| Customer Churn | Lost / Active Customers | < 5% | Monthly |
| Repeat Purchase Rate | Returning / Total Customers | > 30% | Monthly |
| Dormant Rate | No purchase 90+ days / Total | < 20% | Weekly |
| Customer Lifetime Value (CLTV) | Avg Revenue × Avg Lifespan | > $150,000 CLP | Quarterly |

### NPS Classification

| Score | Category | Percentage Target |
|-------|----------|-------------------|
| 9-10 | Promoter | > 50% |
| 7-8 | Passive | < 30% |
| 0-6 | Detractor | < 20% |

### Retargeting Segments

| Segment | Criteria | Target % | Action |
|---------|----------|----------|--------|
| Active | Purchase within 60 days | > 45% | Upsell campaigns |
| At Risk | 60-90 days since purchase | < 35% | Retention offers |
| Dormant | 90+ days since purchase | < 20% | Win-back campaigns |

---

## 4️⃣ Marketing Efficiency

**Objetivo:** Crecer sin destruir margen

| KPI | Formula | Target | Frequency |
|-----|---------|--------|-----------|
| ROAS | Revenue / Ad Spend | > 4.0 | Weekly |
| CAC Payback | CAC / Monthly ARPU | < 3 months | Monthly |
| CLTV:CAC Ratio | CLTV / CAC | > 3:1 | Quarterly |
| Marketing ROI | (Revenue - Cost) / Cost | > 300% | Monthly |

### ROAS by Channel Benchmark

| Channel | Target ROAS | Priority |
|---------|-------------|----------|
| Google Ads | > 5.0 | High |
| Facebook Ads | > 3.5 | Medium |
| Instagram Ads | > 3.0 | Medium |
| MercadoLibre Ads | > 4.0 | High |

---

## 5️⃣ Pricing & Revenue Optimization

**Objetivo:** Optimizar precio y margen

| KPI | Formula | Target | Frequency |
|-----|---------|--------|-----------|
| Price Elasticity (β) | Log-Log regression | Monitor | Quarterly |
| Gross Margin | (Revenue - COGS) / Revenue | > 30% | Monthly |
| Revenue Churn | Lost Rev / Previous Rev | < 3% | Monthly |
| Discount Rate | Discounted Sales / Total Sales | < 20% | Weekly |

### Elasticity Monitoring

| Segment | Current β | Alert Threshold |
|---------|-----------|-----------------|
| Promoters | -0.6 | If > -0.3 (becoming more elastic) |
| Passives | -1.1 | If > -0.8 |
| Detractors | -1.8 | If > -1.5 |

---

## Dashboard Summary

### Primary KPIs (Executive Dashboard)

| KPI | Current | Target | Status |
|-----|---------|--------|--------|
| NPS | 30+ | > 50 | 🟡 |
| Customer Churn | 18% | < 5% | 🔴 |
| CAC | $X CLP | < $8,000 CLP | 🟢 |
| CLTV:CAC | X:1 | > 3:1 | 🟡 |
| ROAS | X.X | > 4.0 | 🟢 |

### Status Legend

- 🟢 On target
- 🟡 Needs attention
- 🔴 Critical

---

## Review Cadence

| Review Type | Frequency | Attendees | Focus |
|-------------|-----------|-----------|-------|
| Daily Standup | Daily | Ops | Conversion, issues |
| Weekly Review | Weekly | Marketing, Sales | Traffic, ROAS, CAC |
| Monthly Business Review | Monthly | Leadership | All KPIs, trends |
| Quarterly Strategy | Quarterly | C-Suite | CLTV, Churn, Elasticity |

---

## Data Sources

| KPI Category | Primary Source | Secondary Source |
|--------------|----------------|------------------|
| Traffic | Google Analytics | Platform dashboards |
| Conversion | Shopify | MercadoLibre |
| Customer | CRM / Database | NPS surveys |
| Marketing | Ad platforms | Attribution tool |
| Pricing | Transaction data | Competitor monitoring |

---

*Document Version: 1.0*  
*Last Updated: February 2026*  
*Author: Jose Marcel Lopez Pino*
