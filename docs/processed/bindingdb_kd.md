# Processed (enriched) dataset: bindingdb_kd

**Source file:** `data/processed/bindingdb_kd_enriched.parquet`  
**Raw reference:** `data/raw/bindingdb_kd.parquet`  
**Generated:** 2026-05-17 09:37 UTC

## Overview

| Metric | Value |
|--------|------:|
| Rows | 52,274 |
| Total columns | 271 |
| Raw / ID columns | 7 |
| UniProt metadata columns | 25 |
| AAC columns | 20 |
| PAAC columns | 72 |
| CTD columns | 147 |
| Rows with `uniprot_id` | 47,941 (91.71%) |
| Rows missing all protein features | 4,333 |
| Mean null rate across feature cols (rows with UniProt) | 13.96% |

## Parquet schema (all columns)

| Column | Dtype | Non-null | Null % |
|--------|-------|----------|--------|
| `Drug_ID` | `float64` | 52,274 | 0.00% |
| `drug_smiles` | `object` | 52,274 | 0.00% |
| `Target_ID` | `object` | 47,941 | 8.29% |
| `target_sequence` | `object` | 52,274 | 0.00% |
| `affinity_label` | `float64` | 52,274 | 0.00% |
| `uniprot_id` | `object` | 47,941 | 8.29% |
| `map_error` | `object` | 4,333 | 91.71% |
| `sequence_length` | `float64` | 47,939 | 8.29% |
| `sequence_checksum` | `object` | 0 | 100.00% |
| `molecular_weight` | `float64` | 47,926 | 8.32% |
| `recommended_name` | `object` | 47,939 | 8.29% |
| `ec_numbers` | `object` | 38,732 | 25.91% |
| `go_terms` | `object` | 47,929 | 8.31% |
| `keywords` | `object` | 47,939 | 8.29% |
| `reactome` | `object` | 37,833 | 27.63% |
| `subcellular_location` | `object` | 44,736 | 14.42% |
| `function` | `object` | 46,788 | 10.49% |
| `pathway` | `object` | 1,718 | 96.71% |
| `enzyme_regulation` | `object` | 0 | 100.00% |
| `tissue_specificity` | `object` | 35,903 | 31.32% |
| `developmental_stage` | `object` | 2,126 | 95.93% |
| `isoform_count` | `float64` | 47,939 | 8.29% |
| `ft_transmem_count` | `float64` | 47,939 | 8.29% |
| `ft_topo_dom_count` | `float64` | 47,939 | 8.29% |
| `ft_domain_count` | `float64` | 47,939 | 8.29% |
| `ft_region_count` | `float64` | 47,939 | 8.29% |
| `ft_binding_count` | `float64` | 47,939 | 8.29% |
| `ft_ptm_count` | `float64` | 47,939 | 8.29% |
| `ft_variant_count` | `float64` | 47,939 | 8.29% |
| `ft_mutagen_count` | `float64` | 47,939 | 8.29% |
| `pdb_count` | `float64` | 47,939 | 8.29% |
| `pdb_ids` | `object` | 39,104 | 25.19% |
| `aac_A` | `float64` | 47,939 | 8.29% |
| `aac_R` | `float64` | 47,939 | 8.29% |
| `aac_N` | `float64` | 47,939 | 8.29% |
| `aac_D` | `float64` | 47,939 | 8.29% |
| `aac_C` | `float64` | 47,939 | 8.29% |
| `aac_E` | `float64` | 47,939 | 8.29% |
| `aac_Q` | `float64` | 47,939 | 8.29% |
| `aac_G` | `float64` | 47,939 | 8.29% |
| `aac_H` | `float64` | 47,939 | 8.29% |
| `aac_I` | `float64` | 47,939 | 8.29% |
| `aac_L` | `float64` | 47,939 | 8.29% |
| `aac_K` | `float64` | 47,939 | 8.29% |
| `aac_M` | `float64` | 47,939 | 8.29% |
| `aac_F` | `float64` | 47,939 | 8.29% |
| `aac_P` | `float64` | 47,939 | 8.29% |
| `aac_S` | `float64` | 47,939 | 8.29% |
| `aac_T` | `float64` | 47,939 | 8.29% |
| `aac_W` | `float64` | 47,939 | 8.29% |
| `aac_Y` | `float64` | 47,939 | 8.29% |
| `aac_V` | `float64` | 47,939 | 8.29% |
| `paac_APAAC1` | `float64` | 47,926 | 8.32% |
| `paac_APAAC2` | `float64` | 47,926 | 8.32% |
| `paac_APAAC3` | `float64` | 47,926 | 8.32% |
| `paac_APAAC4` | `float64` | 47,926 | 8.32% |
| `paac_APAAC5` | `float64` | 47,926 | 8.32% |
| `paac_APAAC6` | `float64` | 47,926 | 8.32% |
| `paac_APAAC7` | `float64` | 47,926 | 8.32% |
| `paac_APAAC8` | `float64` | 47,926 | 8.32% |
| `paac_APAAC9` | `float64` | 47,926 | 8.32% |
| `paac_APAAC10` | `float64` | 47,926 | 8.32% |
| `paac_APAAC11` | `float64` | 47,926 | 8.32% |
| `paac_APAAC12` | `float64` | 47,926 | 8.32% |
| `paac_APAAC13` | `float64` | 47,926 | 8.32% |
| `paac_APAAC14` | `float64` | 47,926 | 8.32% |
| `paac_APAAC15` | `float64` | 47,926 | 8.32% |
| `paac_APAAC16` | `float64` | 47,926 | 8.32% |
| `paac_APAAC17` | `float64` | 47,926 | 8.32% |
| `paac_APAAC18` | `float64` | 47,926 | 8.32% |
| `paac_APAAC19` | `float64` | 47,926 | 8.32% |
| `paac_APAAC20` | `float64` | 47,926 | 8.32% |
| `paac_APAAC21` | `float64` | 47,926 | 8.32% |
| `paac_APAAC22` | `float64` | 47,926 | 8.32% |
| `paac_APAAC23` | `float64` | 47,926 | 8.32% |
| `paac_APAAC24` | `float64` | 47,926 | 8.32% |
| `paac_APAAC25` | `float64` | 47,926 | 8.32% |
| `paac_APAAC26` | `float64` | 47,926 | 8.32% |
| `paac_APAAC27` | `float64` | 47,926 | 8.32% |
| `paac_APAAC28` | `float64` | 47,926 | 8.32% |
| … | … | … | (191 more columns) |

## ID and mapping columns

| map_error | Rows |
|-----------|-----:|
| `None` | 47,941 |
| `null_target_id` | 4,333 |

## Fetch / mapping failures (`bindingdb_kd_fetch_failures.parquet`)

- Failure log rows: **4,334**

| error | Count |
|-------|------:|
| `null_target_id` | 4,333 |
| `http_400` | 1 |

## `affinity_label` (unchanged from raw)

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

## UniProt metadata highlights (rows with valid `uniprot_id`)

- **sequence_length:** min 86, median 609, max 3969
- **molecular_weight:** median 67795 Da
- **pdb_count:** median 9, max 1151

## Descriptor summaries (numeric)

### AAC (amino acid composition)

| Feature | count | mean | std | min | median | max |
|---------|------:|-----:|----:|----:|-------:|----:|
| `aac_A` | 47939 | 6.631 | 1.85 | 0.758 | 6.286 | 17.66 |
| `aac_C` | 47939 | 2.084 | 1.009 | 0 | 1.882 | 9.922 |
| `aac_D` | 47939 | 4.968 | 1.215 | 0.995 | 5.042 | 11.41 |
| `aac_E` | 47939 | 6.901 | 2.046 | 0 | 6.823 | 17.39 |
| `aac_F` | 47939 | 3.922 | 1.18 | 0 | 3.766 | 9.357 |
| `aac_G` | 47939 | 6.533 | 1.769 | 1.01 | 6.433 | 25 |
| `aac_H` | 47939 | 2.682 | 0.9508 | 0 | 2.601 | 7.9 |
| `aac_I` | 47939 | 4.906 | 1.462 | 0.279 | 5.034 | 12.03 |
| `aac_K` | 47939 | 6.025 | 2.089 | 0 | 6.015 | 20 |
| `aac_L` | 47939 | 9.93 | 1.936 | 1.86 | 9.688 | 18.33 |
| `aac_M` | 47939 | 2.404 | 0.7721 | 0.299 | 2.385 | 6.711 |
| `aac_N` | 47939 | 3.749 | 1.219 | 0.307 | 3.602 | 10.73 |
| `aac_P` | 47939 | 6.017 | 2 | 0 | 5.672 | 17.33 |
| `aac_Q` | 47939 | 4.145 | 1.332 | 0 | 3.981 | 11.65 |
| `aac_R` | 47939 | 5.701 | 1.571 | 0.716 | 5.489 | 14.43 |
| `aac_S` | 47939 | 7.677 | 1.803 | 2.128 | 7.599 | 16.07 |
| `aac_T` | 47939 | 5.008 | 1.16 | 1.471 | 5.021 | 14.29 |
| `aac_V` | 47939 | 6.271 | 1.455 | 0 | 6.116 | 12.88 |
| `aac_W` | 47939 | 1.334 | 0.6473 | 0 | 1.238 | 7.692 |
| `aac_Y` | 47939 | 3.112 | 0.9977 | 0 | 3.052 | 7.552 |

### PAAC (pseudo amino acid composition)

| Feature | count | mean | std | min | median | max |
|---------|------:|-----:|----:|----:|-------:|----:|
| `paac_A` | 13 | 0.05759 | 0.01901 | 0.04981 | 0.04981 | 0.1004 |
| `paac_APAAC1` | 47926 | 6.445 | 1.778 | 0.775 | 6.11 | 17.1 |
| `paac_APAAC10` | 47926 | 4.769 | 1.405 | 0.271 | 4.853 | 10.98 |
| `paac_APAAC11` | 47926 | 9.667 | 1.946 | 1.349 | 9.463 | 18.07 |
| `paac_APAAC12` | 47926 | 5.855 | 1.999 | 0 | 5.866 | 14.51 |
| `paac_APAAC13` | 47926 | 2.338 | 0.7513 | 0.302 | 2.317 | 6.38 |
| `paac_APAAC14` | 47926 | 3.816 | 1.148 | 0 | 3.718 | 9.127 |
| `paac_APAAC15` | 47926 | 5.859 | 1.953 | 0 | 5.548 | 15.49 |
| `paac_APAAC16` | 47926 | 7.454 | 1.728 | 2.198 | 7.37 | 15.6 |
| `paac_APAAC17` | 47926 | 4.87 | 1.138 | 1.511 | 4.938 | 14.44 |
| `paac_APAAC18` | 47926 | 1.297 | 0.626 | 0 | 1.208 | 7 |
| `paac_APAAC19` | 47926 | 3.032 | 0.9939 | 0 | 2.99 | 7.591 |
| `paac_APAAC2` | 47926 | 5.532 | 1.444 | 0.707 | 5.41 | 13.16 |
| `paac_APAAC20` | 47926 | 6.101 | 1.418 | 0 | 5.99 | 12.31 |
| `paac_APAAC21` | 47926 | 0.1028 | 0.3486 | -1.516 | 0.073 | 1.5 |
| `paac_APAAC22` | 47926 | 0.1987 | 0.3107 | -1.006 | 0.174 | 2.358 |
| `paac_APAAC23` | 47926 | -0.1009 | 0.3855 | -1.515 | -0.121 | 1.661 |
| `paac_APAAC24` | 47926 | 0.01336 | 0.3129 | -0.865 | -0.01 | 2.699 |
| `paac_APAAC25` | 47926 | 0.2058 | 0.3474 | -1.068 | 0.161 | 1.511 |
| `paac_APAAC26` | 47926 | 0.2549 | 0.3152 | -0.742 | 0.242 | 2.452 |
| `paac_APAAC27` | 47926 | 0.1579 | 0.3129 | -1.454 | 0.136 | 1.371 |
| `paac_APAAC28` | 47926 | 0.2053 | 0.3033 | -0.77 | 0.176 | 2.964 |
| `paac_APAAC29` | 47926 | 0.1065 | 0.303 | -1.078 | 0.087 | 1.825 |
| `paac_APAAC3` | 47926 | 3.648 | 1.2 | 0.309 | 3.504 | 10.84 |
| `paac_APAAC30` | 47926 | 0.18 | 0.2856 | -1.037 | 0.171 | 2.01 |
| … | | | | | | (47 more) |

### CTD (composition, transition, distribution)

| Feature | count | mean | std | min | median | max |
|---------|------:|-----:|----:|----:|-------:|----:|
| `ctd__ChargeC1` | 47939 | 0.1172 | 0.02225 | 0.043 | 0.117 | 0.249 |
| `ctd__ChargeC2` | 47939 | 0.7641 | 0.04386 | 0.502 | 0.762 | 0.91 |
| `ctd__ChargeC3` | 47939 | 0.1187 | 0.02694 | 0.022 | 0.12 | 0.26 |
| `ctd__ChargeD1001` | 47939 | 2.59 | 4.333 | 0.066 | 1.221 | 54.17 |
| `ctd__ChargeD1025` | 47939 | 24.89 | 7.073 | 3.279 | 24.12 | 62.12 |
| `ctd__ChargeD1050` | 47939 | 49.26 | 7.609 | 23.66 | 49.46 | 81.01 |
| `ctd__ChargeD1075` | 47939 | 73.3 | 6.214 | 32.61 | 73.61 | 92.88 |
| `ctd__ChargeD1100` | 47939 | 98.49 | 1.932 | 60.87 | 99.11 | 100 |
| `ctd__ChargeD2001` | 47939 | 0.1862 | 0.1146 | 0.025 | 0.164 | 1.163 |
| `ctd__ChargeD2025` | 47939 | 24.74 | 1.549 | 19.01 | 24.64 | 34.87 |
| `ctd__ChargeD2050` | 47939 | 49.73 | 1.818 | 39.17 | 49.65 | 61.43 |
| `ctd__ChargeD2075` | 47939 | 74.74 | 1.459 | 61.4 | 74.73 | 80.44 |
| `ctd__ChargeD2100` | 47939 | 99.94 | 0.1634 | 84.19 | 100 | 100 |
| `ctd__ChargeD3001` | 47939 | 2.166 | 2.736 | 0.092 | 1.268 | 48.45 |
| `ctd__ChargeD3025` | 47939 | 25.12 | 6.523 | 0.667 | 24.42 | 59.2 |
| `ctd__ChargeD3050` | 47939 | 50.22 | 6.829 | 5.814 | 50 | 86.98 |
| `ctd__ChargeD3075` | 47939 | 74.06 | 6.753 | 10.46 | 74.44 | 97.24 |
| `ctd__ChargeD3100` | 47939 | 98.11 | 2.531 | 58.33 | 98.97 | 100 |
| `ctd__ChargeT12` | 47939 | 0.1725 | 0.02761 | 0.068 | 0.173 | 0.315 |
| `ctd__ChargeT13` | 47939 | 0.02928 | 0.01176 | 0 | 0.029 | 0.116 |
| `ctd__ChargeT23` | 47939 | 0.1752 | 0.03456 | 0.042 | 0.178 | 0.407 |
| `ctd__HydrophobicityC1` | 47939 | 0.3149 | 0.04731 | 0.137 | 0.316 | 0.526 |
| `ctd__HydrophobicityC2` | 47939 | 0.3766 | 0.04343 | 0.237 | 0.373 | 0.557 |
| `ctd__HydrophobicityC3` | 47939 | 0.3085 | 0.04195 | 0.153 | 0.309 | 0.498 |
| `ctd__HydrophobicityD1001` | 47939 | 0.9141 | 1.001 | 0.066 | 0.595 | 14.2 |

## Data quality notes

- **8.29%** of rows have null `Target_ID` / `uniprot_id` (`null_target_id`).
- Extra PAAC columns (`paac_A`, `paac_C`, …) appear when propy fallback AAC columns differ across proteins (271 vs 239 columns).
- High global null rate on all 232 feature columns is driven by **sparse extra `paac_{AA}` columns**; core descriptors are >99.9% populated for mapped rows.
- Rows with UniProt but any null in core features (`sequence_length`, `molecular_weight`, `aac_A`, `paac_APAAC1`): **15**.
- One composite UniProt lookup (`P0DP25,P0DP24,P0DP23`) failed HTTP 400.

## Train-ready derivative

CTD selection (`ctd_feature_selection.ipynb`) produces [`data/trainready/bindingdb_kd_trainready.parquet`](../../data/trainready/bindingdb_kd_trainready.parquet) with **157** columns (CTD 147 → 65). See [trainready/bindingdb_kd.md](../trainready/bindingdb_kd.md).
