# Processed (enriched) dataset: kiba

**Source file:** `data/processed/kiba_enriched.parquet`  
**Raw reference:** `data/raw/kiba.parquet`  
**Generated:** 2026-05-17 09:28 UTC

## Overview

| Metric | Value |
|--------|------:|
| Rows | 117,657 |
| Total columns | 239 |
| Raw / ID columns | 7 |
| UniProt metadata columns | 25 |
| AAC columns | 20 |
| PAAC columns | 40 |
| CTD columns | 147 |
| Rows with `uniprot_id` | 117,657 (100.00%) |
| Rows missing all protein features | 0 |
| Mean null rate across feature cols (rows with UniProt) | 1.89% |

## Parquet schema (all columns)

| Column | Dtype | Non-null | Null % |
|--------|-------|----------|--------|
| `Drug_ID` | `object` | 117,657 | 0.00% |
| `drug_smiles` | `object` | 117,657 | 0.00% |
| `Target_ID` | `object` | 117,657 | 0.00% |
| `target_sequence` | `object` | 117,657 | 0.00% |
| `affinity_label` | `float64` | 117,657 | 0.00% |
| `uniprot_id` | `object` | 117,657 | 0.00% |
| `map_error` | `object` | 0 | 100.00% |
| `sequence_length` | `int64` | 117,657 | 0.00% |
| `sequence_checksum` | `object` | 0 | 100.00% |
| `molecular_weight` | `float64` | 117,657 | 0.00% |
| `recommended_name` | `object` | 117,657 | 0.00% |
| `ec_numbers` | `object` | 116,272 | 1.18% |
| `go_terms` | `object` | 117,657 | 0.00% |
| `keywords` | `object` | 117,657 | 0.00% |
| `reactome` | `object` | 101,869 | 13.42% |
| `subcellular_location` | `object` | 111,795 | 4.98% |
| `function` | `object` | 117,498 | 0.14% |
| `pathway` | `object` | 698 | 99.41% |
| `enzyme_regulation` | `object` | 0 | 100.00% |
| `tissue_specificity` | `object` | 99,963 | 15.04% |
| `developmental_stage` | `object` | 8,854 | 92.47% |
| `isoform_count` | `int64` | 117,657 | 0.00% |
| `ft_transmem_count` | `int64` | 117,657 | 0.00% |
| `ft_topo_dom_count` | `int64` | 117,657 | 0.00% |
| `ft_domain_count` | `int64` | 117,657 | 0.00% |
| `ft_region_count` | `int64` | 117,657 | 0.00% |
| `ft_binding_count` | `int64` | 117,657 | 0.00% |
| `ft_ptm_count` | `int64` | 117,657 | 0.00% |
| `ft_variant_count` | `int64` | 117,657 | 0.00% |
| `ft_mutagen_count` | `int64` | 117,657 | 0.00% |
| `pdb_count` | `int64` | 117,657 | 0.00% |
| `pdb_ids` | `object` | 103,763 | 11.81% |
| `aac_A` | `float64` | 117,657 | 0.00% |
| `aac_R` | `float64` | 117,657 | 0.00% |
| `aac_N` | `float64` | 117,657 | 0.00% |
| `aac_D` | `float64` | 117,657 | 0.00% |
| `aac_C` | `float64` | 117,657 | 0.00% |
| `aac_E` | `float64` | 117,657 | 0.00% |
| `aac_Q` | `float64` | 117,657 | 0.00% |
| `aac_G` | `float64` | 117,657 | 0.00% |
| `aac_H` | `float64` | 117,657 | 0.00% |
| `aac_I` | `float64` | 117,657 | 0.00% |
| `aac_L` | `float64` | 117,657 | 0.00% |
| `aac_K` | `float64` | 117,657 | 0.00% |
| `aac_M` | `float64` | 117,657 | 0.00% |
| `aac_F` | `float64` | 117,657 | 0.00% |
| `aac_P` | `float64` | 117,657 | 0.00% |
| `aac_S` | `float64` | 117,657 | 0.00% |
| `aac_T` | `float64` | 117,657 | 0.00% |
| `aac_W` | `float64` | 117,657 | 0.00% |
| `aac_Y` | `float64` | 117,657 | 0.00% |
| `aac_V` | `float64` | 117,657 | 0.00% |
| `paac_APAAC1` | `float64` | 117,657 | 0.00% |
| `paac_APAAC2` | `float64` | 117,657 | 0.00% |
| `paac_APAAC3` | `float64` | 117,657 | 0.00% |
| `paac_APAAC4` | `float64` | 117,657 | 0.00% |
| `paac_APAAC5` | `float64` | 117,657 | 0.00% |
| `paac_APAAC6` | `float64` | 117,657 | 0.00% |
| `paac_APAAC7` | `float64` | 117,657 | 0.00% |
| `paac_APAAC8` | `float64` | 117,657 | 0.00% |
| `paac_APAAC9` | `float64` | 117,657 | 0.00% |
| `paac_APAAC10` | `float64` | 117,657 | 0.00% |
| `paac_APAAC11` | `float64` | 117,657 | 0.00% |
| `paac_APAAC12` | `float64` | 117,657 | 0.00% |
| `paac_APAAC13` | `float64` | 117,657 | 0.00% |
| `paac_APAAC14` | `float64` | 117,657 | 0.00% |
| `paac_APAAC15` | `float64` | 117,657 | 0.00% |
| `paac_APAAC16` | `float64` | 117,657 | 0.00% |
| `paac_APAAC17` | `float64` | 117,657 | 0.00% |
| `paac_APAAC18` | `float64` | 117,657 | 0.00% |
| `paac_APAAC19` | `float64` | 117,657 | 0.00% |
| `paac_APAAC20` | `float64` | 117,657 | 0.00% |
| `paac_APAAC21` | `float64` | 117,657 | 0.00% |
| `paac_APAAC22` | `float64` | 117,657 | 0.00% |
| `paac_APAAC23` | `float64` | 117,657 | 0.00% |
| `paac_APAAC24` | `float64` | 117,657 | 0.00% |
| `paac_APAAC25` | `float64` | 117,657 | 0.00% |
| `paac_APAAC26` | `float64` | 117,657 | 0.00% |
| `paac_APAAC27` | `float64` | 117,657 | 0.00% |
| `paac_APAAC28` | `float64` | 117,657 | 0.00% |
| … | … | … | (159 more columns) |

## ID and mapping columns

| map_error | Rows |
|-----------|-----:|
| `None` | 117,657 |

## `affinity_label` (unchanged from raw)

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

## UniProt metadata highlights (rows with valid `uniprot_id`)

- **sequence_length:** min 215, median 629, max 4128
- **molecular_weight:** median 71628 Da
- **pdb_count:** median 12, max 498

## Descriptor summaries (numeric)

### AAC (amino acid composition)

| Feature | count | mean | std | min | median | max |
|---------|------:|-----:|----:|----:|-------:|----:|
| `aac_A` | 117657 | 6.072 | 1.304 | 2.703 | 5.941 | 11.2 |
| `aac_C` | 117657 | 2.024 | 0.8513 | 0.337 | 1.917 | 4.959 |
| `aac_D` | 117657 | 5.373 | 1.095 | 2.73 | 5.179 | 8.446 |
| `aac_E` | 117657 | 7.26 | 1.619 | 3.583 | 7.172 | 14.41 |
| `aac_F` | 117657 | 3.904 | 1.068 | 2.102 | 3.799 | 7.123 |
| `aac_G` | 117657 | 6.349 | 1.552 | 2.996 | 6.212 | 13.89 |
| `aac_H` | 117657 | 2.868 | 0.9123 | 1.367 | 2.708 | 7.9 |
| `aac_I` | 117657 | 4.97 | 1.134 | 2.17 | 5.034 | 7.778 |
| `aac_K` | 117657 | 6.406 | 1.754 | 1.857 | 6.604 | 10.38 |
| `aac_L` | 117657 | 9.813 | 1.557 | 6.54 | 9.506 | 14.45 |
| `aac_M` | 117657 | 2.421 | 0.7138 | 0.92 | 2.37 | 4.888 |
| `aac_N` | 117657 | 3.749 | 1.11 | 0.307 | 3.726 | 6.555 |
| `aac_P` | 117657 | 5.861 | 1.67 | 2.511 | 5.556 | 13.01 |
| `aac_Q` | 117657 | 4.201 | 1.142 | 1.553 | 4.052 | 9.287 |
| `aac_R` | 117657 | 5.883 | 1.514 | 2.795 | 5.618 | 14.43 |
| `aac_S` | 117657 | 7.226 | 1.625 | 4.335 | 7.131 | 12.05 |
| `aac_T` | 117657 | 4.958 | 1.083 | 1.935 | 4.953 | 9.265 |
| `aac_V` | 117657 | 6.058 | 1.079 | 3.561 | 6.04 | 10.88 |
| `aac_W` | 117657 | 1.264 | 0.4738 | 0.348 | 1.237 | 2.882 |
| `aac_Y` | 117657 | 3.341 | 0.946 | 1.048 | 3.321 | 6.571 |

### PAAC (pseudo amino acid composition)

| Feature | count | mean | std | min | median | max |
|---------|------:|-----:|----:|----:|-------:|----:|
| `paac_APAAC1` | 117657 | 5.975 | 1.335 | 2.374 | 5.815 | 11.42 |
| `paac_APAAC10` | 117657 | 4.885 | 1.148 | 2.153 | 4.897 | 8.01 |
| `paac_APAAC11` | 117657 | 9.656 | 1.667 | 5.775 | 9.372 | 14.42 |
| `paac_APAAC12` | 117657 | 6.277 | 1.679 | 1.839 | 6.502 | 10.05 |
| `paac_APAAC13` | 117657 | 2.378 | 0.7028 | 0.925 | 2.324 | 4.677 |
| `paac_APAAC14` | 117657 | 3.844 | 1.089 | 1.91 | 3.748 | 7.117 |
| `paac_APAAC15` | 117657 | 5.772 | 1.682 | 2.285 | 5.514 | 13.08 |
| `paac_APAAC16` | 117657 | 7.085 | 1.554 | 4.306 | 7.009 | 11.92 |
| `paac_APAAC17` | 117657 | 4.872 | 1.089 | 1.893 | 4.812 | 9.142 |
| `paac_APAAC18` | 117657 | 1.246 | 0.4803 | 0.348 | 1.209 | 2.948 |
| `paac_APAAC19` | 117657 | 3.285 | 0.9411 | 0.928 | 3.257 | 6.726 |
| `paac_APAAC2` | 117657 | 5.755 | 1.334 | 2.722 | 5.537 | 11.88 |
| `paac_APAAC20` | 117657 | 5.961 | 1.131 | 3.482 | 5.892 | 11.17 |
| `paac_APAAC21` | 117657 | 0.04855 | 0.2726 | -0.723 | 0.054 | 1.223 |
| `paac_APAAC22` | 117657 | 0.1529 | 0.2515 | -0.646 | 0.153 | 0.882 |
| `paac_APAAC23` | 117657 | -0.2422 | 0.3154 | -1.148 | -0.231 | 1.033 |
| `paac_APAAC24` | 117657 | -0.07781 | 0.2928 | -0.784 | -0.085 | 0.692 |
| `paac_APAAC25` | 117657 | 0.1588 | 0.3293 | -0.617 | 0.161 | 1.511 |
| `paac_APAAC26` | 117657 | 0.2261 | 0.2844 | -0.547 | 0.226 | 0.972 |
| `paac_APAAC27` | 117657 | 0.0887 | 0.2501 | -0.797 | 0.089 | 1.371 |
| `paac_APAAC28` | 117657 | 0.1192 | 0.2726 | -0.59 | 0.082 | 1.018 |
| `paac_APAAC29` | 117657 | 0.04903 | 0.26 | -0.752 | 0.039 | 0.996 |
| `paac_APAAC3` | 117657 | 3.679 | 1.094 | 0.309 | 3.662 | 6.577 |
| `paac_APAAC30` | 117657 | 0.1725 | 0.2423 | -0.575 | 0.147 | 0.858 |
| `paac_APAAC31` | 117657 | 0.1205 | 0.2483 | -0.546 | 0.129 | 1.264 |
| … | | | | | | (15 more) |

### CTD (composition, transition, distribution)

| Feature | count | mean | std | min | median | max |
|---------|------:|-----:|----:|----:|-------:|----:|
| `ctd__ChargeC1` | 117657 | 0.1229 | 0.02046 | 0.078 | 0.122 | 0.192 |
| `ctd__ChargeC2` | 117657 | 0.7508 | 0.03432 | 0.645 | 0.752 | 0.855 |
| `ctd__ChargeC3` | 117657 | 0.1264 | 0.01963 | 0.068 | 0.126 | 0.202 |
| `ctd__ChargeD1001` | 117657 | 1.632 | 1.663 | 0.085 | 1.177 | 12.25 |
| `ctd__ChargeD1025` | 117657 | 23.19 | 5.33 | 12.14 | 22.84 | 40 |
| `ctd__ChargeD1050` | 117657 | 47.72 | 6.406 | 28.26 | 47.88 | 64.65 |
| `ctd__ChargeD1075` | 117657 | 72.47 | 5.475 | 54.66 | 72.66 | 85.75 |
| `ctd__ChargeD1100` | 117657 | 98.28 | 2.138 | 85.17 | 99.03 | 100 |
| `ctd__ChargeD2001` | 117657 | 0.1706 | 0.07453 | 0.024 | 0.159 | 0.465 |
| `ctd__ChargeD2025` | 117657 | 24.91 | 1.45 | 20.75 | 24.76 | 30.26 |
| `ctd__ChargeD2050` | 117657 | 49.88 | 1.511 | 46.52 | 49.72 | 54.11 |
| `ctd__ChargeD2075` | 117657 | 74.81 | 1.387 | 71 | 74.6 | 79.48 |
| `ctd__ChargeD2100` | 117657 | 99.96 | 0.1071 | 99.35 | 100 | 100 |
| `ctd__ChargeD3001` | 117657 | 1.915 | 2.009 | 0.143 | 1.453 | 26 |
| `ctd__ChargeD3025` | 117657 | 25.59 | 5.431 | 10.17 | 24.93 | 48.86 |
| `ctd__ChargeD3050` | 117657 | 50.61 | 6.089 | 27.91 | 50.8 | 70.03 |
| `ctd__ChargeD3075` | 117657 | 74.73 | 5.845 | 46.05 | 75.57 | 87.78 |
| `ctd__ChargeD3100` | 117657 | 98.24 | 2.239 | 80.47 | 98.91 | 100 |
| `ctd__ChargeT12` | 117657 | 0.1793 | 0.02474 | 0.114 | 0.18 | 0.249 |
| `ctd__ChargeT13` | 117657 | 0.03173 | 0.0111 | 0.008 | 0.031 | 0.068 |
| `ctd__ChargeT23` | 117657 | 0.1868 | 0.02333 | 0.111 | 0.187 | 0.269 |
| `ctd__HydrophobicityC1` | 117657 | 0.3287 | 0.03809 | 0.24 | 0.325 | 0.479 |
| `ctd__HydrophobicityC2` | 117657 | 0.3667 | 0.03963 | 0.263 | 0.365 | 0.491 |
| `ctd__HydrophobicityC3` | 117657 | 0.3045 | 0.02713 | 0.235 | 0.309 | 0.369 |
| `ctd__HydrophobicityD1001` | 117657 | 0.8084 | 0.6353 | 0.085 | 0.635 | 3.909 |

## Data quality notes

- **100%** mapping success; all rows have `uniprot_id` and populated features.
- Column set matches Davis/KIBA (239 columns).

## Train-ready derivative

CTD selection (`ctd_feature_selection.ipynb`) produces [`data/trainready/kiba_trainready.parquet`](../../data/trainready/kiba_trainready.parquet) with **162** columns (CTD 147 → 70). See [trainready/kiba.md](../trainready/kiba.md).
