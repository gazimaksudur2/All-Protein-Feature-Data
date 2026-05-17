# Train-ready dataset: kiba

**File:** `data/trainready/kiba_trainready.parquet`  
**Source:** `data/processed/kiba_enriched.parquet`  
**Generated:** 2026-05-17 09:37 UTC

## Overview

| Metric | Processed | Train-ready |
|--------|----------:|------------:|
| Rows | 117,657 | 117,657 |
| Total columns | 239 | 157 |
| CTD columns | 147 | 65 |

## CTD selection

| Stage | Dropped |
|-------|--------:|
| 1 — variance ≤ 0.01 | 49 |
| 2 — \|r\| > 0.85 | 28 |
| **Final kept** | **70** |

## Schema (first 40 columns)

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
| … | … | … | (117 more columns) |

Full schema: [schemas/trainready_kiba_schema.md](../schemas/trainready_kiba_schema.md)

Methodology: [ctd_feature_selection.md](ctd_feature_selection.md)
