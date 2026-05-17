# CTD feature selection (methodology & findings)

**Notebook:** `ctd_feature_selection.ipynb`  
**Input:** `data/processed/*_enriched.parquet`  
**Output:** `data/trainready/*_trainready.parquet`  
**Reports:** `data/trainready/reports/dropped_ctd_features.json`  
**Generated:** 2026-05-17 09:37 UTC

## Objective

Reduce collinearity and low-information CTD descriptors before DTI model training. Only `ctd__*` columns are filtered; all other enriched columns are preserved unchanged.

## Pipeline stages

### Stage 1 — Variance threshold

- **Rule:** Drop CTD features with variance $\sigma^2 \le 0.01$.
- **Rationale:** Near-constant features across rows carry no discriminative signal.
- **Implementation:** `sklearn.feature_selection.VarianceThreshold(threshold=0.01)`.

### Stage 2 — Collinearity filter

- **Rule:** For pairs with $|r| > 0.85$, remove the feature with **lower variance**.
- **Rationale:** Redundant collinear inputs hurt MLP/linear layers; keep higher-variance member.

### Preprocessing (selection fit only)

- Numeric coercion; median imputation for fitting only (original NaNs kept in output).
- Row index and non-CTD columns unchanged.

## Results summary

| Dataset | CTD in | Stage 1 dropped | Stage 2 dropped | CTD kept | Reduction |
|---------|------:|------------------:|------------------:|---------:|----------:|
| **davis** | 147 | 50 | 28 | **69** | 53.1% |
| **kiba** | 147 | 49 | 28 | **70** | 52.4% |
| **bindingdb_kd** | 147 | 42 | 34 | **71** | 51.7% |

## Key findings

1. **~47–52% CTD reduction** (147 → 69–71) across all three benchmarks.
2. **Stage 1** removes many Composition (`*C1–C3`), Transition (`*T12–T23`), and low-percentile Distribution terms with variance ≤ 0.01.
3. **Stage 2** removes redundant distribution bins (`HydrophobicityD*`, `PolarityD*`, `PolarizabilityD*`, `NormalizedVDWVD*`) among survivors.
4. **BindingDB:** fewer stage-1 drops (42) but more stage-2 drops (34) vs Davis/KIBA.
5. **Alignment:** train-ready row counts and ID/SMILES columns match `data/processed/` exactly.
6. **`data/processed/` is never modified** by the selection notebook.

## Dropped-feature logs

| Dataset | Report file |
|---------|-------------|
| davis | `data/trainready/reports/dropped_ctd_features_davis.json` |
| kiba | `data/trainready/reports/dropped_ctd_features_kiba.json` |
| bindingdb_kd | `data/trainready/reports/dropped_ctd_features_bindingdb_kd.json` |

Combined: `data/trainready/reports/dropped_ctd_features.json`
