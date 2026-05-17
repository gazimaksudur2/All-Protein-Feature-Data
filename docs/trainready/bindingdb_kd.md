# Train-ready dataset: bindingdb_kd

**File:** `data/trainready/bindingdb_kd_trainready.parquet`  
**Source:** `data/processed/bindingdb_kd_enriched.parquet`  
**Generated:** 2026-05-17 09:37 UTC

## Overview

| Metric | Processed | Train-ready |
|--------|----------:|------------:|
| Rows | 52,274 | 52,274 |
| Total columns | 271 | 157 |
| CTD columns | 147 | 65 |

## CTD selection

| Stage | Dropped |
|-------|--------:|
| 1 — variance ≤ 0.01 | 42 |
| 2 — \|r\| > 0.85 | 34 |
| **Final kept** | **71** |

## Schema (first 40 columns)

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
| … | … | … | (117 more columns) |

Full schema: [schemas/trainready_bindingdb_kd_schema.md](../schemas/trainready_bindingdb_kd_schema.md)

Methodology: [ctd_feature_selection.md](ctd_feature_selection.md)
