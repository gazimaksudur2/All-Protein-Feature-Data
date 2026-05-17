# Raw dataset: bindingdb_kd

**Source file:** `data/raw/bindingdb_kd.parquet`  
**Generated:** 2026-05-17 16:38 UTC

## Overview

| Metric | Value |
|--------|------:|
| Rows | 52,274 |
| Columns | 5 |
| Unique drugs (`Drug_ID`) | 10,636 |
| Unique targets (`Target_ID`) | 1,090 |
| Null `Target_ID` | 4,333 (8.29%) |
| Duplicate rows | 0 |

## Parquet schema

| Column | Dtype | Non-null | Null % |
|--------|-------|----------|--------|
| `Drug_ID` | `float64` | 52,274 | 0.00% |
| `drug_smiles` | `object` | 52,274 | 0.00% |
| `Target_ID` | `object` | 47,941 | 8.29% |
| `target_sequence` | `object` | 52,274 | 0.00% |
| `affinity_label` | `float64` | 52,274 | 0.00% |

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
count    5.227400e+04
mean     4.353189e+04
std      4.102312e+05
min      0.000000e+00
25%      2.200000e+02
50%      9.800000e+03
75%      1.000000e+04
max      1.000000e+07
```

## Text field lengths (median / max)

| Field | Median length | Max length |
|-------|-------------:|-----------:|
| `drug_smiles` | 56 | 973 |
| `target_sequence` | 596 | 4128 |

## Target ID notes (BindingDB-KD)

- `Target_ID` is mostly UniProt accessions; **null** targets occur on a subset of rows.
- Some rows may use composite or non-standard IDs that fail UniProt REST lookup.

## Top 10 targets by row count

| Target_ID | Rows |
|-----------|-----:|
| `P00519` | 814 |
| `P10721` | 673 |
| `P36888` | 642 |
| `P15056` | 601 |
| `P00533` | 560 |
| `P51449` | 395 |
| `P00918` | 363 |
| `P24941` | 302 |
| `Q8K4Z4` | 229 |
| `P07949` | 224 |
