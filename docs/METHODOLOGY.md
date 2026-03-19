# Methodology — Project 6: Customer Segmentation

## Framework: CRISP-DM + LEAN

### CRISP-DM Phases Applied

| Phase | Notebook | Key Output |
|-------|----------|-----------|
| 1. Business Understanding | 01 | Problem definition, KPIs, success criteria |
| 2. Data Understanding | 02 | EDA, distribution analysis, missing value audit |
| 3. Data Preparation | 03 | Cleaned + encoded + normalized dataset |
| 4. Modeling | 04 | KMeans, DBSCAN, Hierarchical + PCA + t-SNE |
| 5. Evaluation | 05 | Silhouette scores, elbow curve, business interpretation |
| 6. Deployment | 06 | Executive report (ES) + notebook documentation |

### LEAN Principles Applied

- **MVA**: Start with KMeans (simplest); add DBSCAN/hierarchical only if KMeans is insufficient
- **Waste elimination**: Only encode variables that contribute to behavioral segmentation
- **80/20**: Focus analysis on 3 most discriminating variables before full-feature modeling
- **Iterate on value**: Increase k only if business team can act on additional segments

### ICI Advantage

As an Industrial Civil Engineer, the segmentation outputs are framed as operational decisions:
- Cluster profiles → campaign design specs
- Silhouette scores → quality control metric (analogous to Cpk in process control)
- Segment stability → analogous to process capability over time
