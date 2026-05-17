# Train-ready dataset: davis

**File:** `data/trainready/davis_trainready.parquet`  
**Source:** `data/processed/davis_enriched.parquet`  
**Generated:** 2026-05-17 16:38 UTC

## Overview

| Metric | Processed | Train-ready |
|--------|----------:|------------:|
| Rows | 25,772 | 23,256 |
| Total columns | 239 | 157 |
| CTD columns | 147 | 65 |

## Row filter (preprocessing)

- Rows before filter: **25,772**
- Rows dropped (unmapped): **2,516**
- Rows after filter: **23,256**

## CTD selection

| Stage | Dropped |
|-------|--------:|
| 1 — variance ≤ 0.01 | 50 |
| 2 — \|r\| > 0.85 | 28 |
| **Final kept** | **69** |

## Schema (first 40 columns)

| Column | Dtype | Non-null | Null % |
|--------|-------|----------|--------|
| `Drug_ID` | `int64` | 23,256 | 0.00% |
| `drug_smiles` | `object` | 23,256 | 0.00% |
| `Target_ID` | `object` | 23,256 | 0.00% |
| `target_sequence` | `object` | 23,256 | 0.00% |
| `affinity_label` | `float64` | 23,256 | 0.00% |
| `uniprot_id` | `object` | 23,256 | 0.00% |
| `map_error` | `object` | 0 | 100.00% |
| `sequence_length` | `float64` | 23,256 | 0.00% |
| `sequence_checksum` | `object` | 0 | 100.00% |
| `molecular_weight` | `float64` | 23,256 | 0.00% |
| `recommended_name` | `object` | 23,256 | 0.00% |
| `ec_numbers` | `object` | 22,780 | 2.05% |
| `go_terms` | `object` | 23,256 | 0.00% |
| `keywords` | `object` | 23,256 | 0.00% |
| `reactome` | `object` | 16,660 | 28.36% |
| `subcellular_location` | `object` | 21,284 | 8.48% |
| `function` | `object` | 22,168 | 4.68% |
| `pathway` | `object` | 340 | 98.54% |
| `enzyme_regulation` | `object` | 0 | 100.00% |
| `tissue_specificity` | `object` | 18,700 | 19.59% |
| `developmental_stage` | `object` | 1,292 | 94.44% |
| `isoform_count` | `float64` | 23,256 | 0.00% |
| `ft_transmem_count` | `float64` | 23,256 | 0.00% |
| `ft_topo_dom_count` | `float64` | 23,256 | 0.00% |
| `ft_domain_count` | `float64` | 23,256 | 0.00% |
| `ft_region_count` | `float64` | 23,256 | 0.00% |
| `ft_binding_count` | `float64` | 23,256 | 0.00% |
| `ft_ptm_count` | `float64` | 23,256 | 0.00% |
| `ft_variant_count` | `float64` | 23,256 | 0.00% |
| `ft_mutagen_count` | `float64` | 23,256 | 0.00% |
| `pdb_count` | `float64` | 23,256 | 0.00% |
| `pdb_ids` | `object` | 18,428 | 20.76% |
| `aac_A` | `float64` | 23,256 | 0.00% |
| `aac_R` | `float64` | 23,256 | 0.00% |
| `aac_N` | `float64` | 23,256 | 0.00% |
| `aac_D` | `float64` | 23,256 | 0.00% |
| `aac_C` | `float64` | 23,256 | 0.00% |
| `aac_E` | `float64` | 23,256 | 0.00% |
| `aac_Q` | `float64` | 23,256 | 0.00% |
| `aac_G` | `float64` | 23,256 | 0.00% |
| … | … | … | (117 more columns) |

Full schema: [schemas/trainready_davis_schema.md](../schemas/trainready_davis_schema.md)

Methodology: [ctd_feature_selection.md](ctd_feature_selection.md)
