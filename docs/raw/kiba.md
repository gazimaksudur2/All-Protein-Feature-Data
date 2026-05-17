# Raw dataset: kiba

**Source file:** `data/raw/kiba.parquet`  
**Generated:** 2026-05-16 14:29 UTC

## Overview

| Metric | Value |
|--------|------:|
| Rows | 117,657 |
| Columns | 5 |
| Unique drugs (`Drug_ID`) | 2,068 |
| Unique targets (`Target_ID`) | 229 |
| Null `Target_ID` | 0 (0.00%) |
| Duplicate rows | 0 |

## Parquet schema

| Column | Dtype | Non-null | Null % |
|--------|-------|----------|--------|
| `Drug_ID` | `object` | 117,657 | 0.00% |
| `drug_smiles` | `object` | 117,657 | 0.00% |
| `Target_ID` | `object` | 117,657 | 0.00% |
| `target_sequence` | `object` | 117,657 | 0.00% |
| `affinity_label` | `float64` | 117,657 | 0.00% |

## Column descriptions

| Column | Dtype | Description |
|--------|-------|-------------|
| `Drug_ID` | object/numeric | Compound identifier (dataset-specific format). |
| `drug_smiles` | string | SMILES representation of the compound. |
| `Target_ID` | string | Protein identifier (gene symbol for Davis; UniProt for KIBA/BindingDB). |
| `target_sequence` | string | Target amino acid sequence bundled with the benchmark row. |
| `affinity_label` | float | Affinity or activity label (scale differs by dataset). |

## `affinity_label` distribution

```
count    117657.000000
mean         11.720685
std           0.834272
min           0.000000
25%          11.200000
50%          11.520216
75%          11.923909
max          17.200179
```

## Text field lengths (median / max)

| Field | Median length | Max length |
|-------|-------------:|-----------:|
| `drug_smiles` | 45 | 532 |
| `target_sequence` | 629 | 4128 |

## Target ID notes (KIBA)

- `Target_ID` values are **UniProt accessions** (e.g. `O00141`, `P00533`).
- No gene-symbol mapping is required before UniProt fetch.

## Top 10 targets by row count

| Target_ID | Rows |
|-----------|-----:|
| `P35968` | 1,432 |
| `P17612` | 1,237 |
| `O94806` | 1,203 |
| `P49841` | 1,168 |
| `P06239` | 1,135 |
| `Q05655` | 1,120 |
| `P05129` | 1,113 |
| `P12931` | 1,106 |
| `P11309` | 1,090 |
| `Q05513` | 1,089 |
