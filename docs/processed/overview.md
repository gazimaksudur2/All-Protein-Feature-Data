# Processed datasets — cross-dataset overview

**Directory:** `data/processed/`  
**Generated:** 2026-05-17 09:37 UTC

## File inventory

| File | Rows | Columns | Size (approx.) |
|------|-----:|--------:|----------------:|
| `davis_enriched.parquet` | 25,772 | 239 | 1.74 MB |
| `kiba_enriched.parquet` | 117,657 | 239 | 8.50 MB |
| `bindingdb_kd_enriched.parquet` | 52,274 | 271 | 12.43 MB |

## Comparison

| Dataset | Rows | Cols | % with UniProt | Unique drugs | Unique targets | Affinity (median) |
|---------|-----:|-----:|---------------:|-------------:|-----------------:|------------------:|
| **davis** | 25,772 | 239 | 90.2% | 68 | 379 | 1e+04 |
| **kiba** | 117,657 | 239 | 100.0% | 2,068 | 229 | 11.52 |
| **bindingdb_kd** | 52,274 | 271 | 91.7% | 10,636 | 1,090 | 9800 |

## Shared vs dataset-specific columns

- **Davis** and **KIBA** share the same **239** enriched columns.
- **BindingDB-KD** has **271** columns (32 extra `paac_{AA}` fallback columns from heterogeneous descriptor computation).
- **239** columns are common across all three files.

## Per-dataset documentation

| Dataset | Raw analytics | Processed analytics |
|---------|---------------|---------------------|
| Davis | [raw/davis.md](raw/davis.md) | [processed/davis.md](processed/davis.md) |
| KIBA | [raw/kiba.md](raw/kiba.md) | [processed/kiba.md](processed/kiba.md) |
| BindingDB-KD | [raw/bindingdb_kd.md](raw/bindingdb_kd.md) | [processed/bindingdb_kd.md](processed/bindingdb_kd.md) |

See also: [feature_catalog.md](feature_catalog.md)

## Downstream: CTD feature selection

Train-ready outputs in `data/trainready/` (see [trainready/overview.md](../trainready/overview.md)):

| Dataset | Processed cols | Train-ready cols | CTD 147 → kept |
|---------|---------------:|-----------------:|---------------:|
| **davis** | 239 | 157 | 147 → 65 |
| **kiba** | 239 | 157 | 147 → 65 |
| **bindingdb_kd** | 271 | 157 | 147 → 65 |
