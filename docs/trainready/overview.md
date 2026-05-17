# Train-ready datasets — overview

**Directory:** `data/trainready/`  
**Generated:** 2026-05-17 09:28 UTC

Final modeling inputs after CTD feature selection. `data/processed/` is unchanged.

## File inventory

| File | Rows | Columns | CTD cols | Size (MB) |
|------|-----:|--------:|---------:|----------:|
| `davis_trainready.parquet` | 25,772 | 161 | 69 | 1.65 |
| `kiba_trainready.parquet` | 117,657 | 162 | 70 | 5.91 |
| `bindingdb_kd_trainready.parquet` | 52,274 | 195 | 71 | 9.80 |

## Pipeline

```text
data/raw → enrichment → data/processed → CTD selection → data/trainready
```

- [CTD methodology & findings](ctd_feature_selection.md)
