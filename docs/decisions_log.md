# Decisions Log — Project 6: Customer Segmentation

| # | Notebook | Decision | Rationale | Alternatives Considered | LEAN Value? |
|---|----------|----------|-----------|------------------------|-------------|
| 1 | 01 | Use Kaggle kaushiksuresh147 dataset | Realistic retail segmentation scenario, labeled for post-hoc validation | Synthetic data | ✅ |
| 2 | 03 | Apply IQR outlier removal (factor=1.5) | Conservative removal preserving most data | Z-score, manual inspection | ✅ |
| 3 | 03 | StandardScaler over MinMaxScaler | Distance-based algorithms (KMeans, DBSCAN) require zero-mean, unit-variance | MinMaxScaler | ✅ |
| 4 | 03 | PCA before t-SNE | t-SNE on high-dim data is slow and unstable; PCA first improves both | t-SNE directly on scaled data | ✅ |
| 5 | 04 | Evaluate k=2…10 for elbow | Common business range; covers interpretable segment counts | k=2…20 | ✅ |
| 6 | 04 | Ward linkage for hierarchical | Minimizes within-cluster variance; consistent with KMeans objective | Complete, average | ✅ |
| 7 | 05 | Hold out `Segmentation` label for external validation only | Maintains unsupervised discipline; use label only to interpret cluster alignment | Use label during modeling | ✅ |
