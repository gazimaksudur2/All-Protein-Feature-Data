# Protein feature catalog

Features appended during enrichment come from **UniProt REST JSON** and **sequence descriptors** (propy3).

## Column groups

| Group | Prefix / names | Count (typical) | Type |
|-------|----------------|----------------:|------|
| Raw DTI fields | `Drug_ID`, `drug_smiles`, … | 5 | unchanged |
| Resolved ID | `uniprot_id`, `map_error` | 2 | string |
| UniProt metadata | see table below | 25 | mixed |
| AAC | `aac_*` | 20 | float |
| PAAC | `paac_APAAC*` or `paac_{AA}` | 40–72 | float |
| CTD | `ctd_*` | 147 | float |

## UniProt metadata columns

| Column | Type | Description |
|--------|------|-------------|
| `sequence_length` | mixed | Amino acid length from UniProt sequence record. |
| `sequence_checksum` | mixed | CRC64 checksum of UniProt sequence. |
| `molecular_weight` | mixed | Computed molecular weight (Da) via BioPython ProteinAnalysis. |
| `recommended_name` | mixed | UniProt recommended full protein name. |
| `ec_numbers` | mixed | EC numbers (semicolon-separated). |
| `go_terms` | mixed | Gene Ontology cross-reference IDs (semicolon-separated). |
| `keywords` | mixed | UniProt keyword IDs (semicolon-separated). |
| `reactome` | mixed | Reactome pathway IDs (semicolon-separated). |
| `subcellular_location` | mixed | Subcellular location text from UniProt comments. |
| `function` | mixed | FUNCTION comment text(s), space-joined. |
| `pathway` | mixed | PATHWAY comment text(s), space-joined. |
| `enzyme_regulation` | mixed | ENZYME REGULATION comment text(s). |
| `tissue_specificity` | mixed | TISSUE SPECIFICITY comment text(s). |
| `developmental_stage` | mixed | DEVELOPMENTAL STAGE comment text(s). |
| `isoform_count` | mixed | Count of isoforms in ALTERNATIVE PRODUCTS comments. |
| `ft_transmem_count` | mixed | Count of TRANSMEM features in UniProt feature table. |
| `ft_topo_dom_count` | mixed | Count of TOPO_DOM features. |
| `ft_domain_count` | mixed | Count of DOMAIN features. |
| `ft_region_count` | mixed | Count of REGION features. |
| `ft_binding_count` | mixed | Count of BINDING features. |
| `ft_ptm_count` | mixed | Count of MOD_RES + CARBOHYD features. |
| `ft_variant_count` | mixed | Count of VARIANT features. |
| `ft_mutagen_count` | mixed | Count of MUTAGEN features. |
| `pdb_count` | mixed | Number of PDB cross-references. |
| `pdb_ids` | mixed | PDB IDs (semicolon-separated). |

## AAC (`aac_A` … `aac_Y`)

- **Meaning:** Normalized frequency of each standard amino acid in the UniProt sequence.
- **Source:** `propy.AAComposition.CalculateAAComposition` (fallback: count/length).
- **Range:** [0, 1]; sums to ~1 across 20 letters.

## PAAC (`paac_APAAC1` … `paac_APAAC40`)

- **Meaning:** Pseudo amino acid composition capturing sequence order with hydrophobicity/hydrophilicity matrices.
- **Source:** `propy.PseudoAAC.GetAPseudoAAC(sequence, lamda=10, weight=0.05)`.
- **Note:** BindingDB merge may add `paac_A`, `paac_C`, … from fallback paths for some proteins.

## CTD (`ctd_*`)

- **Meaning:** Composition (C), transition (T), and distribution (D) descriptors for seven physicochemical properties (hydrophobicity, polarity, side-chain volume, etc.).
- **Source:** `propy.CTD.CalculateCTD` (~147 numeric features in `data/processed/`).
- **Naming:** `ctd__{Property}{C|T|D}{group}{percentile}` (propy naming with double underscores).
- **Train-ready subset:** After two-stage selection in `data/trainready/`, **69–71** CTD columns remain per dataset (see [trainready/ctd_feature_selection.md](trainready/ctd_feature_selection.md)).
