# Train-ready dataset: davis

**File:** `data/trainready/davis_trainready.parquet`  
**Source:** `data/processed/davis_enriched.parquet`  
**Generated:** 2026-05-17 09:37 UTC

## Overview

| Metric | Processed | Train-ready |
|--------|----------:|------------:|
| Rows | 25,772 | 25,772 |
| Total columns | 239 | 157 |
| CTD columns | 147 | 65 |

## CTD selection

| Stage | Dropped |
|-------|--------:|
| 1 — variance ≤ 0.01 | 50 |
| 2 — \|r\| > 0.85 | 28 |
| **Final kept** | **69** |

## Schema (first 40 columns)

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
| … | … | … | (117 more columns) |

Full schema: [schemas/trainready_davis_schema.md](../schemas/trainready_davis_schema.md)

Methodology: [ctd_feature_selection.md](ctd_feature_selection.md)
