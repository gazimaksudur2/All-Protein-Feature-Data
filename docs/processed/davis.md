# Processed (enriched) dataset: davis

**Source file:** `data/processed/davis_enriched.parquet`  
**Raw reference:** `data/raw/davis.parquet`  
**Generated:** 2026-05-17 09:37 UTC

## Overview

| Metric | Value |
|--------|------:|
| Rows | 25,772 |
| Total columns | 239 |
| Raw / ID columns | 7 |
| UniProt metadata columns | 25 |
| AAC columns | 20 |
| PAAC columns | 40 |
| CTD columns | 147 |
| Rows with `uniprot_id` | 23,256 (90.24%) |
| Rows missing all protein features | 2,516 |
| Mean null rate across feature cols (rows with UniProt) | 2.06% |

## Parquet schema (all columns)

| Column | Dtype | Non-null | Null % |
|--------|-------|----------|--------|
| `Drug_ID` | `int64` | 25,772 | 0.00% |
| `drug_smiles` | `object` | 25,772 | 0.00% |
| `Target_ID` | `object` | 25,772 | 0.00% |
| `target_sequence` | `object` | 25,772 | 0.00% |
| `affinity_label` | `float64` | 25,772 | 0.00% |
| `uniprot_id` | `object` | 23,256 | 9.76% |
| `map_error` | `object` | 2,516 | 90.24% |
| `sequence_length` | `float64` | 23,256 | 9.76% |
| `sequence_checksum` | `object` | 0 | 100.00% |
| `molecular_weight` | `float64` | 23,256 | 9.76% |
| `recommended_name` | `object` | 23,256 | 9.76% |
| `ec_numbers` | `object` | 22,780 | 11.61% |
| `go_terms` | `object` | 23,256 | 9.76% |
| `keywords` | `object` | 23,256 | 9.76% |
| `reactome` | `object` | 16,660 | 35.36% |
| `subcellular_location` | `object` | 21,284 | 17.41% |
| `function` | `object` | 22,168 | 13.98% |
| `pathway` | `object` | 340 | 98.68% |
| `enzyme_regulation` | `object` | 0 | 100.00% |
| `tissue_specificity` | `object` | 18,700 | 27.44% |
| `developmental_stage` | `object` | 1,292 | 94.99% |
| `isoform_count` | `float64` | 23,256 | 9.76% |
| `ft_transmem_count` | `float64` | 23,256 | 9.76% |
| `ft_topo_dom_count` | `float64` | 23,256 | 9.76% |
| `ft_domain_count` | `float64` | 23,256 | 9.76% |
| `ft_region_count` | `float64` | 23,256 | 9.76% |
| `ft_binding_count` | `float64` | 23,256 | 9.76% |
| `ft_ptm_count` | `float64` | 23,256 | 9.76% |
| `ft_variant_count` | `float64` | 23,256 | 9.76% |
| `ft_mutagen_count` | `float64` | 23,256 | 9.76% |
| `pdb_count` | `float64` | 23,256 | 9.76% |
| `pdb_ids` | `object` | 18,428 | 28.50% |
| `aac_A` | `float64` | 23,256 | 9.76% |
| `aac_R` | `float64` | 23,256 | 9.76% |
| `aac_N` | `float64` | 23,256 | 9.76% |
| `aac_D` | `float64` | 23,256 | 9.76% |
| `aac_C` | `float64` | 23,256 | 9.76% |
| `aac_E` | `float64` | 23,256 | 9.76% |
| `aac_Q` | `float64` | 23,256 | 9.76% |
| `aac_G` | `float64` | 23,256 | 9.76% |
| `aac_H` | `float64` | 23,256 | 9.76% |
| `aac_I` | `float64` | 23,256 | 9.76% |
| `aac_L` | `float64` | 23,256 | 9.76% |
| `aac_K` | `float64` | 23,256 | 9.76% |
| `aac_M` | `float64` | 23,256 | 9.76% |
| `aac_F` | `float64` | 23,256 | 9.76% |
| `aac_P` | `float64` | 23,256 | 9.76% |
| `aac_S` | `float64` | 23,256 | 9.76% |
| `aac_T` | `float64` | 23,256 | 9.76% |
| `aac_W` | `float64` | 23,256 | 9.76% |
| `aac_Y` | `float64` | 23,256 | 9.76% |
| `aac_V` | `float64` | 23,256 | 9.76% |
| `paac_APAAC1` | `float64` | 23,256 | 9.76% |
| `paac_APAAC2` | `float64` | 23,256 | 9.76% |
| `paac_APAAC3` | `float64` | 23,256 | 9.76% |
| `paac_APAAC4` | `float64` | 23,256 | 9.76% |
| `paac_APAAC5` | `float64` | 23,256 | 9.76% |
| `paac_APAAC6` | `float64` | 23,256 | 9.76% |
| `paac_APAAC7` | `float64` | 23,256 | 9.76% |
| `paac_APAAC8` | `float64` | 23,256 | 9.76% |
| `paac_APAAC9` | `float64` | 23,256 | 9.76% |
| `paac_APAAC10` | `float64` | 23,256 | 9.76% |
| `paac_APAAC11` | `float64` | 23,256 | 9.76% |
| `paac_APAAC12` | `float64` | 23,256 | 9.76% |
| `paac_APAAC13` | `float64` | 23,256 | 9.76% |
| `paac_APAAC14` | `float64` | 23,256 | 9.76% |
| `paac_APAAC15` | `float64` | 23,256 | 9.76% |
| `paac_APAAC16` | `float64` | 23,256 | 9.76% |
| `paac_APAAC17` | `float64` | 23,256 | 9.76% |
| `paac_APAAC18` | `float64` | 23,256 | 9.76% |
| `paac_APAAC19` | `float64` | 23,256 | 9.76% |
| `paac_APAAC20` | `float64` | 23,256 | 9.76% |
| `paac_APAAC21` | `float64` | 23,256 | 9.76% |
| `paac_APAAC22` | `float64` | 23,256 | 9.76% |
| `paac_APAAC23` | `float64` | 23,256 | 9.76% |
| `paac_APAAC24` | `float64` | 23,256 | 9.76% |
| `paac_APAAC25` | `float64` | 23,256 | 9.76% |
| `paac_APAAC26` | `float64` | 23,256 | 9.76% |
| `paac_APAAC27` | `float64` | 23,256 | 9.76% |
| `paac_APAAC28` | `float64` | 23,256 | 9.76% |
| … | … | … | (159 more columns) |

## ID and mapping columns

| map_error | Rows |
|-----------|-----:|
| `None` | 23,256 |
| `mapping_failed` | 2,516 |

## Fetch / mapping failures (`davis_fetch_failures.parquet`)

- Failure log rows: **2,516**

| error | Count |
|-------|------:|
| `mapping_failed` | 2,516 |

## `affinity_label` (unchanged from raw)

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

## UniProt metadata highlights (rows with valid `uniprot_id`)

- **sequence_length:** min 266, median 646, max 2549
- **molecular_weight:** median 72148 Da
- **pdb_count:** median 4, max 498

## Descriptor summaries (numeric)

### AAC (amino acid composition)

| Feature | count | mean | std | min | median | max |
|---------|------:|-----:|----:|----:|-------:|----:|
| `aac_A` | 23256 | 6.382 | 1.601 | 2.703 | 6.066 | 13.86 |
| `aac_C` | 23256 | 2.01 | 0.922 | 0.377 | 1.808 | 9.922 |
| `aac_D` | 23256 | 5.159 | 1.002 | 2.467 | 5.095 | 9.507 |
| `aac_E` | 23256 | 7.365 | 1.806 | 3.306 | 7.098 | 16.99 |
| `aac_F` | 23256 | 3.578 | 0.9034 | 1.862 | 3.513 | 6.855 |
| `aac_G` | 23256 | 6.454 | 1.524 | 2.895 | 6.316 | 13.89 |
| `aac_H` | 23256 | 2.856 | 0.9471 | 1.179 | 2.742 | 7.9 |
| `aac_I` | 23256 | 4.812 | 1.237 | 0.279 | 4.903 | 8.333 |
| `aac_K` | 23256 | 6.232 | 1.886 | 1.671 | 6.324 | 10.71 |
| `aac_L` | 23256 | 9.829 | 1.713 | 5.841 | 9.585 | 16.88 |
| `aac_M` | 23256 | 2.41 | 0.7242 | 0.557 | 2.385 | 4.888 |
| `aac_N` | 23256 | 3.621 | 1.133 | 0.307 | 3.579 | 6.555 |
| `aac_P` | 23256 | 6.191 | 1.932 | 2.511 | 5.827 | 14.54 |
| `aac_Q` | 23256 | 4.38 | 1.312 | 2.156 | 4.107 | 11.65 |
| `aac_R` | 23256 | 5.975 | 1.494 | 2.885 | 5.841 | 14.43 |
| `aac_S` | 23256 | 7.672 | 1.786 | 4.202 | 7.46 | 13.54 |
| `aac_T` | 23256 | 4.884 | 1.085 | 1.935 | 4.796 | 9.265 |
| `aac_V` | 23256 | 5.902 | 1.147 | 3.16 | 5.807 | 10.14 |
| `aac_W` | 23256 | 1.208 | 0.5087 | 0.178 | 1.156 | 2.882 |
| `aac_Y` | 23256 | 3.081 | 0.99 | 1.048 | 2.977 | 6.571 |

### PAAC (pseudo amino acid composition)

| Feature | count | mean | std | min | median | max |
|---------|------:|-----:|----:|----:|-------:|----:|
| `paac_APAAC1` | 23256 | 6.241 | 1.608 | 2.374 | 5.963 | 13.24 |
| `paac_APAAC10` | 23256 | 4.704 | 1.241 | 0.271 | 4.761 | 8.04 |
| `paac_APAAC11` | 23256 | 9.616 | 1.808 | 5.578 | 9.346 | 16.56 |
| `paac_APAAC12` | 23256 | 6.064 | 1.781 | 1.624 | 6.186 | 10.32 |
| `paac_APAAC13` | 23256 | 2.355 | 0.7151 | 0.541 | 2.324 | 4.624 |
| `paac_APAAC14` | 23256 | 3.502 | 0.9156 | 1.709 | 3.43 | 6.699 |
| `paac_APAAC15` | 23256 | 6.055 | 1.916 | 2.285 | 5.707 | 14.45 |
| `paac_APAAC16` | 23256 | 7.481 | 1.725 | 4.153 | 7.296 | 13.11 |
| `paac_APAAC17` | 23256 | 4.773 | 1.093 | 1.893 | 4.721 | 9.142 |
| `paac_APAAC18` | 23256 | 1.184 | 0.5106 | 0.177 | 1.114 | 2.948 |
| `paac_APAAC19` | 23256 | 3.015 | 0.9946 | 0.928 | 2.912 | 6.726 |
| `paac_APAAC2` | 23256 | 5.813 | 1.347 | 2.783 | 5.719 | 11.88 |
| `paac_APAAC20` | 23256 | 5.777 | 1.2 | 2.798 | 5.726 | 9.77 |
| `paac_APAAC21` | 23256 | 0.07863 | 0.2679 | -0.676 | 0.058 | 1.223 |
| `paac_APAAC22` | 23256 | 0.1962 | 0.2762 | -0.646 | 0.175 | 1.783 |
| `paac_APAAC23` | 23256 | -0.1787 | 0.2965 | -1.002 | -0.1695 | 1.033 |
| `paac_APAAC24` | 23256 | -0.01968 | 0.2985 | -0.865 | -0.0445 | 1.509 |
| `paac_APAAC25` | 23256 | 0.1749 | 0.3095 | -0.617 | 0.1495 | 1.511 |
| `paac_APAAC26` | 23256 | 0.246 | 0.2961 | -0.547 | 0.226 | 1.783 |
| `paac_APAAC27` | 23256 | 0.09751 | 0.2379 | -0.797 | 0.1 | 1.371 |
| `paac_APAAC28` | 23256 | 0.1772 | 0.284 | -0.744 | 0.1475 | 1.568 |
| `paac_APAAC29` | 23256 | 0.1049 | 0.2583 | -0.752 | 0.0895 | 1.097 |
| `paac_APAAC3` | 23256 | 3.535 | 1.108 | 0.309 | 3.522 | 6.577 |
| `paac_APAAC30` | 23256 | 0.2056 | 0.2718 | -0.409 | 0.171 | 1.609 |
| `paac_APAAC31` | 23256 | 0.1084 | 0.2486 | -0.546 | 0.0905 | 1.264 |
| … | | | | | | (15 more) |

### CTD (composition, transition, distribution)

| Feature | count | mean | std | min | median | max |
|---------|------:|-----:|----:|----:|-------:|----:|
| `ctd__ChargeC1` | 23256 | 0.122 | 0.02057 | 0.073 | 0.1215 | 0.192 |
| `ctd__ChargeC2` | 23256 | 0.7527 | 0.03632 | 0.592 | 0.753 | 0.861 |
| `ctd__ChargeC3` | 23256 | 0.1252 | 0.02153 | 0.066 | 0.124 | 0.225 |
| `ctd__ChargeD1001` | 23256 | 1.702 | 1.757 | 0.085 | 1.153 | 12.25 |
| `ctd__ChargeD1025` | 23256 | 23.45 | 5.744 | 12.14 | 23.02 | 50 |
| `ctd__ChargeD1050` | 23256 | 47.85 | 7.224 | 23.66 | 48.59 | 66.92 |
| `ctd__ChargeD1075` | 23256 | 72.39 | 5.977 | 49.18 | 72.66 | 86.8 |
| `ctd__ChargeD1100` | 23256 | 98.6 | 1.736 | 85.17 | 99.18 | 100 |
| `ctd__ChargeD2001` | 23256 | 0.1616 | 0.06771 | 0.039 | 0.155 | 0.376 |
| `ctd__ChargeD2025` | 23256 | 25.04 | 1.59 | 20.3 | 24.91 | 35.09 |
| `ctd__ChargeD2050` | 23256 | 49.98 | 1.927 | 42.48 | 49.77 | 61.51 |
| `ctd__ChargeD2075` | 23256 | 74.96 | 1.458 | 70.3 | 74.91 | 80.13 |
| `ctd__ChargeD2100` | 23256 | 99.96 | 0.09648 | 99.38 | 100 | 100 |
| `ctd__ChargeD3001` | 23256 | 1.889 | 2.541 | 0.129 | 1.106 | 26 |
| `ctd__ChargeD3025` | 23256 | 24.98 | 5.3 | 11.8 | 24.19 | 44.36 |
| `ctd__ChargeD3050` | 23256 | 49.95 | 6.15 | 33.22 | 49.48 | 71.9 |
| `ctd__ChargeD3075` | 23256 | 73.91 | 5.977 | 52.23 | 74.46 | 89.72 |
| `ctd__ChargeD3100` | 23256 | 98.21 | 2.15 | 84.4 | 98.91 | 100 |
| `ctd__ChargeT12` | 23256 | 0.1772 | 0.02407 | 0.11 | 0.176 | 0.246 |
| `ctd__ChargeT13` | 23256 | 0.03134 | 0.01192 | 0.007 | 0.03 | 0.099 |
| `ctd__ChargeT23` | 23256 | 0.1843 | 0.02421 | 0.098 | 0.183 | 0.269 |
| `ctd__HydrophobicityC1` | 23256 | 0.3273 | 0.03921 | 0.24 | 0.325 | 0.479 |
| `ctd__HydrophobicityC2` | 23256 | 0.3752 | 0.04164 | 0.263 | 0.374 | 0.491 |
| `ctd__HydrophobicityC3` | 23256 | 0.2975 | 0.02982 | 0.201 | 0.301 | 0.369 |
| `ctd__HydrophobicityD1001` | 23256 | 0.789 | 0.857 | 0.085 | 0.5475 | 9.524 |

## Data quality notes

- **9.76%** of rows (2,516) have `mapping_failed` (no `uniprot_id`).
- **37** unique targets (of 379) failed mapping; **342** mapped successfully.
- Failed targets include mutant isoform names and kinase domain qualifiers not resolved by gene search.

### Unmapped Davis `Target_ID` values (unique)

- `AMPK-alpha1`
- `AMPK-alpha2`
- `BRAF(V600E)`
- `CDK4-cyclinD3`
- `FGFR3(G697C)`
- `FLT3(R834Q)`
- `GCN2(KinDom2S808G)`
- `IKK-alpha`
- `IKK-beta`
- `IKK-epsilon`
- `JAK1(JH2domain-pseudokinase)`
- `JAK2(JH1domain-catalytic)`
- `JAK3(JH1domain-catalytic)`
- `KIT(V559D-V654A)`
- `MET(Y1235D)`
- `MRCKA`
- `MRCKB`
- `PFCDPK1(Pfalciparum)`
- `PFPK5(Pfalciparum)`
- `PFTAIRE2`
- `PIK3CA(Q546K)`
- `PKAC-alpha`
- `PKAC-beta`
- `PKNB(Mtuberculosis)`
- `RET(V804M)`
- `RPS6KA4(KinDom.2-C-terminal)`
- `RPS6KA5(KinDom.2-C-terminal)`
- `RSK1(KinDom.2-C-terminal)`
- `RSK2(KinDom.1-N-terminal)`
- `RSK3(KinDom.2-C-terminal)`
- `RSK4(KinDom.2-C-terminal)`
- `S6K1`
- `TYK2(JH2domain-pseudokinase)`
- `p38-alpha`
- `p38-beta`
- `p38-delta`
- `p38-gamma`

## Train-ready derivative

CTD selection (`ctd_feature_selection.ipynb`) produces [`data/trainready/davis_trainready.parquet`](../../data/trainready/davis_trainready.parquet) with **157** columns (CTD 147 → 65). See [trainready/davis.md](../trainready/davis.md).
