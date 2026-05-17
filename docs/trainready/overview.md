# Train-ready datasets — overview

**Directory:** `data/trainready/`  
**Generated:** 2026-05-17 09:37 UTC

Final modeling inputs after CTD feature selection. `data/processed/` is unchanged.

## File inventory

| File | Rows | Columns | CTD cols | Size (MB) |
|------|-----:|--------:|---------:|----------:|
| `davis_trainready.parquet` | 25,772 | 157 | 65 | 1.62 |
| `kiba_trainready.parquet` | 117,657 | 157 | 65 | 5.72 |
| `bindingdb_kd_trainready.parquet` | 52,274 | 157 | 65 | 9.54 |

## Pipeline

```text
data/raw → enrichment → data/processed → CTD selection → data/trainready
```

- [CTD methodology & findings](ctd_feature_selection.md)
