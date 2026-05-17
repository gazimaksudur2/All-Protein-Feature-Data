# Raw dataset: davis

**Source file:** `data/raw/davis.parquet`  
**Generated:** 2026-05-17 09:28 UTC

## Overview

| Metric | Value |
|--------|------:|
| Rows | 25,772 |
| Columns | 5 |
| Unique drugs (`Drug_ID`) | 68 |
| Unique targets (`Target_ID`) | 379 |
| Null `Target_ID` | 0 (0.00%) |
| Duplicate rows | 0 |

## Parquet schema

| Column | Dtype | Non-null | Null % |
|--------|-------|----------|--------|
| `Drug_ID` | `int64` | 25,772 | 0.00% |
| `drug_smiles` | `object` | 25,772 | 0.00% |
| `Target_ID` | `object` | 25,772 | 0.00% |
| `target_sequence` | `object` | 25,772 | 0.00% |
| `affinity_label` | `float64` | 25,772 | 0.00% |

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
count    25772.000000
mean      7558.112997
std       3990.013578
min          0.016000
25%       3775.000000
50%      10000.000000
75%      10000.000000
max      10000.000000
```

## Text field lengths (median / max)

| Field | Median length | Max length |
|-------|-------------:|-----------:|
| `drug_smiles` | 53 | 81 |
| `target_sequence` | 632 | 2549 |

## Target ID notes (Davis)

- `Target_ID` values are **human kinase gene symbols** (e.g. `AAK1`, `ABL1p`), not UniProt accessions.
- Trailing `p` denotes phosphatase-related naming in the benchmark (stripped during UniProt mapping).
- Complex names (e.g. `BRAF(V600E)`, `JAK2(JH1domain-catalytic)`) often fail automated gene lookup.

## Top 10 targets by row count

| Target_ID | Rows |
|-----------|-----:|
| `AAK1` | 68 |
| `ABL1p` | 68 |
| `ABL2` | 68 |
| `ACVR1` | 68 |
| `ACVR1B` | 68 |
| `ACVR2A` | 68 |
| `ACVR2B` | 68 |
| `ACVRL1` | 68 |
| `ADCK3` | 68 |
| `ADCK4` | 68 |
