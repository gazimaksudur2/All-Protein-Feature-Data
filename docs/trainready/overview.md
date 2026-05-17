# Train-ready datasets — overview

**Directory:** `data/trainready/`  
**Generated:** 2026-05-17 16:38 UTC

Final modeling inputs after CTD feature selection. `data/processed/` is unchanged.

## File inventory

| File | Rows | Columns | CTD cols | Size (MB) |
|------|-----:|--------:|---------:|----------:|
| `davis_trainready.parquet` | 23,256 | 157 | 65 | 1.52 |
| `kiba_trainready.parquet` | 117,657 | 157 | 65 | 5.72 |
| `bindingdb_kd_trainready.parquet` | 47,941 | 157 | 65 | 8.53 |

## Pipeline

```text
data/raw → enrichment → data/processed → CTD selection → data/trainready
```

- [CTD methodology & findings](ctd_feature_selection.md)
