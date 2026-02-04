# Pricing Playbook - PequeShop

## 1. Methodology

**Model:** Log-Log Regression (Industry Standard)

```
ln(Q) = α + β·ln(P)
```

Where:
- Q = quantity demanded
- P = price
- β = price elasticity of demand (directly interpretable)

**Interpretation:**
- β = -1.5 → 1% price increase → 1.5% demand decrease

**Scope Limitation:** 
CAC was estimated using paid media spend only. A production implementation would include sales team costs, marketing tools, and attributed overhead.

---

## 2. Elasticity by Segment

| Segment | β (Elasticity) | Interpretation |
|---------|----------------|----------------|
| Promoters (NPS 9-10) | -0.6 | Inelastic |
| Passives (NPS 7-8) | -1.1 | Unit elastic |
| Detractors (NPS 0-6) | -1.8 | Elastic |

**Key Insight:**
> "High NPS customers show lower price sensitivity (β = -0.6), enabling targeted price optimization without sacrificing loyalty."

---

## 3. Decision Framework

**Approach:** Bounded adjustments based on elasticity, not point estimates.

> "Based on estimated price elasticity, pricing recommendations were defined as bounded adjustments rather than point estimates."

### Customer-Aware Pricing Rules

| Elasticity | NPS | Churn Risk | Action |
|------------|-----|------------|--------|
| Inelastic (β > -1) | High | Low | ↑ Price increase up to 5% |
| Inelastic (β > -1) | Low | High | → Hold price |
| Elastic (β < -1) | High | Low | → Maintain price |
| Elastic (β < -1) | Low | High | ↓ Promotional discount |

### Example Calculation

**Scenario:**
- Elasticity: β = -0.6 (inelastic)
- Proposed action: +5% price increase

**Expected Impact:**
- Volume change: 5% × 0.6 = -3%
- Revenue impact: +5% price - 3% volume = **+2% net revenue**

**Recommendation:** "A controlled price increase of up to 5% is recommended."

---

## 4. Product Guidelines

| Category | Elasticity | Strategy |
|----------|------------|----------|
| Jackets | Inelastic | Premium pricing opportunity |
| Pajamas | Unit elastic | Maintain current pricing |
| Socks | Elastic | Volume/promotional focus |
| T-shirts | Moderate | Seasonal adjustments |
| Shorts | Elastic | Bundle with other items |
| Towels | Inelastic | Stable pricing |

---

## 5. Guardrails

### Pricing Limits

| Parameter | Limit | Rationale |
|-----------|-------|-----------|
| Max price increase | 5% per quarter | Avoid customer shock |
| Min gross margin | 30% | Maintain profitability |
| Discount cap | 25% | Protect brand value |

### Review Triggers

Immediate pricing review required if:
- NPS drops > 10 points in any segment
- Churn rate increases > 2% month-over-month
- Conversion rate drops > 15% after price change
- Competitor price change > 10%

---

## 6. Review Cadence

| Metric | Frequency | Owner |
|--------|-----------|-------|
| Price Elasticity | Quarterly | Data Science |
| NPS by Segment | Monthly | Customer Success |
| Churn Rate | Weekly | Marketing |
| Margin Analysis | Monthly | Finance |
| Competitive Pricing | Bi-weekly | Product |

---

## 7. Implementation Checklist

### Before Price Change

- [ ] Calculate elasticity for affected segment
- [ ] Check NPS and churn risk levels
- [ ] Verify margin impact
- [ ] Define rollback criteria
- [ ] Communicate to customer service team

### During Rollout

- [ ] Monitor conversion rate daily
- [ ] Track customer complaints
- [ ] Compare to control group (if A/B test)

### After Price Change (30 days)

- [ ] Measure actual vs. expected volume change
- [ ] Update elasticity estimates
- [ ] Document learnings

---

## 8. A/B Testing Framework (Future)

### Test Design

```
Control Group: Current price
Test Group: New price (+X%)
Sample Size: Min 1,000 customers per group
Duration: 4-6 weeks
Primary Metric: Revenue per customer
Secondary: Conversion rate, NPS change
```

### Statistical Significance

- Confidence level: 95%
- Minimum detectable effect: 5%
- Power: 80%

---

## Appendix: Elasticity Reference

| β Value | Type | Business Implication |
|---------|------|---------------------|
| 0 to -0.5 | Highly inelastic | Strong pricing power |
| -0.5 to -1.0 | Inelastic | Moderate pricing power |
| -1.0 | Unit elastic | Revenue neutral |
| -1.0 to -2.0 | Elastic | Price sensitive |
| < -2.0 | Highly elastic | Very price sensitive |

---

*Document Version: 1.0*  
*Last Updated: February 2026*  
*Author: Jose Marcel Lopez Pino*
