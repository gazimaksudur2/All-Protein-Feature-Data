# Dataset documentation

Analytics and schema reference for DTI parquet files in this repository.

## Contents

- [Feature catalog](feature_catalog.md) — all protein feature groups and column meanings
- [Processed overview](processed/overview.md) — cross-dataset comparison of enriched files
- [Train-ready overview](trainready/overview.md) — CTD-filtered modeling inputs
- [CTD feature selection](trainready/ctd_feature_selection.md) — methodology, findings, dropped-column logs

### Raw inputs (`data/raw/`)

- [davis.md](raw/davis.md)
- [kiba.md](raw/kiba.md)
- [bindingdb_kd.md](raw/bindingdb_kd.md)

### Enriched outputs (`data/processed/`)

- [davis.md](processed/davis.md)
- [kiba.md](processed/kiba.md)
- [bindingdb_kd.md](processed/bindingdb_kd.md)

### Train-ready outputs (`data/trainready/`)

- [davis.md](trainready/davis.md)
- [kiba.md](trainready/kiba.md)
- [bindingdb_kd.md](trainready/bindingdb_kd.md)

### Full parquet schemas (all columns)

| Dataset | Raw | Processed | Train-ready |
|---------|-----|-----------|-------------|
| Davis | [schemas/raw_davis_schema.md](schemas/raw_davis_schema.md) | [schemas/processed_davis_schema.md](schemas/processed_davis_schema.md) | [schemas/trainready_davis_schema.md](schemas/trainready_davis_schema.md) |
| KIBA | [schemas/raw_kiba_schema.md](schemas/raw_kiba_schema.md) | [schemas/processed_kiba_schema.md](schemas/processed_kiba_schema.md) | [schemas/trainready_kiba_schema.md](schemas/trainready_kiba_schema.md) |
| BindingDB-KD | [schemas/raw_bindingdb_kd_schema.md](schemas/raw_bindingdb_kd_schema.md) | [schemas/processed_bindingdb_kd_schema.md](schemas/processed_bindingdb_kd_schema.md) | [schemas/trainready_bindingdb_kd_schema.md](schemas/trainready_bindingdb_kd_schema.md) |

Regenerate analytics: `python _generate_docs.py`
