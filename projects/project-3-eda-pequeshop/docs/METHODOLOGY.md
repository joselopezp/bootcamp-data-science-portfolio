# Methodology: CRISP-DM + Lean

> This document describes the hybrid framework applied to this project,
> combining the industry-standard CRISP-DM methodology with Lean principles
> from Industrial Engineering.

---

## Why This Framework?

**CRISP-DM** provides structure: six iterative phases that ensure rigor and
reproducibility in data science projects (adopted by 65%+ of the industry).

**Lean Thinking** provides focus: every analysis must create value for the
stakeholder, and any work that does not contribute to a business decision
is waste to be eliminated.

The combination ensures that data science work is not just technically
correct but also **business-relevant and efficient**.

---

## CRISP-DM Phases with Lean Integration

### Phase 1: Business Understanding

**CRISP-DM objective**: Define the business problem and project goals.

**Lean enhancement**:
- **Define Value**: What specific decision will this analysis enable?
- **Identify the Customer**: Who is the stakeholder? What do they need?
- **Set Success Criteria**: How will we know the analysis is useful?

**Deliverable**: Business problem statement with measurable success criteria.

**Key questions**:
- [ ] What decision is the stakeholder trying to make?
- [ ] What happens if we do nothing? (cost of inaction)
- [ ] What is the minimum output that enables a decision? (MVA scope)

---

### Phase 2: Data Understanding

**CRISP-DM objective**: Collect, describe, and explore the data.

**Lean enhancement**:
- **Pull System**: Only explore variables relevant to the business question.
- **Eliminate Waste**: Skip exhaustive profiling of irrelevant columns.
- **Early Quality Check**: Identify data issues before investing in preparation.

**Deliverable**: Data quality report focused on decision-relevant variables.

**Key questions**:
- [ ] Which variables directly relate to the business question?
- [ ] What data quality issues could affect our conclusions?
- [ ] Is the data sufficient to answer the question? If not, what's missing?

---

### Phase 3: Data Preparation

**CRISP-DM objective**: Clean, transform, and engineer features.

**Lean enhancement**:
- **Minimum Viable Transformation**: Only transformations that add analytical value.
- **One-Piece Flow**: Process data in a clear, reproducible pipeline.
- **Document Decisions**: Record why each transformation was applied.

**Deliverable**: Clean, analysis-ready dataset with documented transformations.

**Key questions**:
- [ ] Does each transformation serve the business question?
- [ ] Can someone else reproduce this pipeline from documentation alone?
- [ ] Are we over-engineering features before testing a simple approach?

---

### Phase 4: Modeling

**CRISP-DM objective**: Build and calibrate analytical models.

**Lean enhancement**:
- **Start Simple**: Simplest model that answers the business question first.
- **Iterate Based on Value**: Increase complexity only if simple model is insufficient.
- **80/20 Principle**: 20% of modeling effort often generates 80% of insight.

**Deliverable**: Model(s) with documented rationale for approach selection.

**Key questions**:
- [ ] Does a descriptive analysis already answer the question?
- [ ] What is the simplest model that provides actionable insight?
- [ ] Is additional complexity justified by business value?

---

### Phase 5: Evaluation

**CRISP-DM objective**: Assess model results against business objectives.

**Lean enhancement**:
- **Business Validation**: Does the result answer the original question?
- **Stakeholder Review**: Present findings to stakeholders for feedback.
- **Continuous Improvement**: Document lessons for the next iteration.

**Deliverable**: Evaluation report connecting technical metrics to business impact.

**Key questions**:
- [ ] Does this result enable the stakeholder's decision?
- [ ] Can we explain the findings in non-technical language?
- [ ] What would we do differently in the next iteration?

---

### Phase 6: Deployment

**CRISP-DM objective**: Deliver results and operationalize if needed.

**Lean enhancement**:
- **Dual-Format Delivery**: Technical report + Executive summary.
- **Actionable Output**: Concrete recommendations, not just findings.
- **Knowledge Transfer**: Documentation that enables others to maintain/extend.

**Deliverable**: Final reports (technical + executive) with actionable recommendations.

**Key questions**:
- [ ] Is the technical report reproducible by another data scientist?
- [ ] Does the executive summary enable a business decision?
- [ ] Is the code clean, documented, and version-controlled?

---

## Lean Principles Applied Throughout

| Lean Principle | Application in Data Science |
|----------------|---------------------------|
| **Define Value** | Every analysis serves a business decision |
| **Map the Value Stream** | CRISP-DM phases as a clear workflow |
| **Create Flow** | Reproducible pipeline from raw data to insight |
| **Establish Pull** | Stakeholder needs drive analysis scope |
| **Pursue Perfection** | Iterate based on feedback (Kaizen) |

### Waste Types in Data Science (Lean Muda)

| Waste Type | Data Science Example | Mitigation |
|------------|---------------------|------------|
| **Overprocessing** | Cleaning columns not used in analysis | Only process decision-relevant variables |
| **Overproduction** | 50-page report when 2-page summary suffices | Dual-format: technical + executive |
| **Waiting** | Blocked by data access or approvals | Identify dependencies early in Phase 1 |
| **Defects** | Errors in data pipeline | Validation checks at each phase |
| **Inventory** | Hoarding intermediate datasets | Clean pipeline: raw → processed → final |
| **Motion** | Context-switching between unrelated analyses | Focus on one CRISP-DM phase at a time |
| **Transportation** | Moving data between incompatible tools | Standardized Python environment |

---

## Minimum Viable Analysis (MVA)

Inspired by Lean Startup's MVP concept:

1. **Define**: What is the simplest analysis that provides value?
2. **Build**: Create the MVA with basic tools and techniques.
3. **Measure**: Does it answer the business question?
4. **Learn**: Iterate only if additional depth is justified.

**MVA ≠ low quality**. It means starting with the highest-value analysis
and adding complexity only when business needs require it.

---

## Retrospective Template

After each project, complete `/docs/lean_retrospective.md`:

- **What went well?** (Keep)
- **What could improve?** (Change)
- **What waste was eliminated?** (Lean wins)
- **What waste remains?** (Next iteration)
- **Time: estimated vs actual per phase**
- **Key learning for future projects**

---

*Framework: CRISP-DM + Lean | Designed for business-driven data science*
