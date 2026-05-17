# Train-ready dataset: bindingdb_kd

**File:** `data/trainready/bindingdb_kd_trainready.parquet`  
**Source:** `data/processed/bindingdb_kd_enriched.parquet`  
**Generated:** 2026-05-17 16:38 UTC

## Overview

| Metric | Processed | Train-ready |
|--------|----------:|------------:|
| Rows | 52,274 | 47,941 |
| Total columns | 271 | 157 |
| CTD columns | 147 | 65 |

## Row filter (preprocessing)

- Rows before filter: **52,274**
- Rows dropped (unmapped): **4,333**
- Rows after filter: **47,941**

## CTD selection

| Stage | Dropped |
|-------|--------:|
| 1 — variance ≤ 0.01 | 42 |
| 2 — \|r\| > 0.85 | 34 |
| **Final kept** | **71** |

## Schema (first 40 columns)

| Column | Dtype | Non-null | Null % |
|--------|-------|----------|--------|
| `Drug_ID` | `float64` | 47,941 | 0.00% |
| `drug_smiles` | `object` | 47,941 | 0.00% |
| `Target_ID` | `object` | 47,941 | 0.00% |
| `target_sequence` | `object` | 47,941 | 0.00% |
| `affinity_label` | `float64` | 47,941 | 0.00% |
| `uniprot_id` | `object` | 47,941 | 0.00% |
| `map_error` | `object` | 0 | 100.00% |
| `sequence_length` | `float64` | 47,939 | 0.00% |
| `sequence_checksum` | `object` | 0 | 100.00% |
| `molecular_weight` | `float64` | 47,926 | 0.03% |
| `recommended_name` | `object` | 47,939 | 0.00% |
| `ec_numbers` | `object` | 38,732 | 19.21% |
| `go_terms` | `object` | 47,929 | 0.03% |
| `keywords` | `object` | 47,939 | 0.00% |
| `reactome` | `object` | 37,833 | 21.08% |
| `subcellular_location` | `object` | 44,736 | 6.69% |
| `function` | `object` | 46,788 | 2.41% |
| `pathway` | `object` | 1,718 | 96.42% |
| `enzyme_regulation` | `object` | 0 | 100.00% |
| `tissue_specificity` | `object` | 35,903 | 25.11% |
| `developmental_stage` | `object` | 2,126 | 95.57% |
| `isoform_count` | `float64` | 47,939 | 0.00% |
| `ft_transmem_count` | `float64` | 47,939 | 0.00% |
| `ft_topo_dom_count` | `float64` | 47,939 | 0.00% |
| `ft_domain_count` | `float64` | 47,939 | 0.00% |
| `ft_region_count` | `float64` | 47,939 | 0.00% |
| `ft_binding_count` | `float64` | 47,939 | 0.00% |
| `ft_ptm_count` | `float64` | 47,939 | 0.00% |
| `ft_variant_count` | `float64` | 47,939 | 0.00% |
| `ft_mutagen_count` | `float64` | 47,939 | 0.00% |
| `pdb_count` | `float64` | 47,939 | 0.00% |
| `pdb_ids` | `object` | 39,104 | 18.43% |
| `aac_A` | `float64` | 47,939 | 0.00% |
| `aac_R` | `float64` | 47,939 | 0.00% |
| `aac_N` | `float64` | 47,939 | 0.00% |
| `aac_D` | `float64` | 47,939 | 0.00% |
| `aac_C` | `float64` | 47,939 | 0.00% |
| `aac_E` | `float64` | 47,939 | 0.00% |
| `aac_Q` | `float64` | 47,939 | 0.00% |
| `aac_G` | `float64` | 47,939 | 0.00% |
| … | … | … | (117 more columns) |

Full schema: [schemas/trainready_bindingdb_kd_schema.md](../schemas/trainready_bindingdb_kd_schema.md)

Methodology: [ctd_feature_selection.md](ctd_feature_selection.md)
