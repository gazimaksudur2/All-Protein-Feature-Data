"""Generate docs/ analytics markdown from data/raw and data/processed."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
RAW_DIR = ROOT / "data" / "raw"
PROC_DIR = ROOT / "data" / "processed"
DOCS_DIR = ROOT / "docs"

DATASETS = ["davis", "kiba", "bindingdb_kd"]

RAW_COLS = ["Drug_ID", "drug_smiles", "Target_ID", "target_sequence", "affinity_label"]
ID_COLS = RAW_COLS + ["uniprot_id", "map_error"]

METADATA_COLS = [
    "sequence_length",
    "sequence_checksum",
    "molecular_weight",
    "recommended_name",
    "ec_numbers",
    "go_terms",
    "keywords",
    "reactome",
    "subcellular_location",
    "function",
    "pathway",
    "enzyme_regulation",
    "tissue_specificity",
    "developmental_stage",
    "isoform_count",
    "ft_transmem_count",
    "ft_topo_dom_count",
    "ft_domain_count",
    "ft_region_count",
    "ft_binding_count",
    "ft_ptm_count",
    "ft_variant_count",
    "ft_mutagen_count",
    "pdb_count",
    "pdb_ids",
]

METADATA_DESCRIPTIONS = {
    "sequence_length": "Amino acid length from UniProt sequence record.",
    "sequence_checksum": "CRC64 checksum of UniProt sequence.",
    "molecular_weight": "Computed molecular weight (Da) via BioPython ProteinAnalysis.",
    "recommended_name": "UniProt recommended full protein name.",
    "ec_numbers": "EC numbers (semicolon-separated).",
    "go_terms": "Gene Ontology cross-reference IDs (semicolon-separated).",
    "keywords": "UniProt keyword IDs (semicolon-separated).",
    "reactome": "Reactome pathway IDs (semicolon-separated).",
    "subcellular_location": "Subcellular location text from UniProt comments.",
    "function": "FUNCTION comment text(s), space-joined.",
    "pathway": "PATHWAY comment text(s), space-joined.",
    "enzyme_regulation": "ENZYME REGULATION comment text(s).",
    "tissue_specificity": "TISSUE SPECIFICITY comment text(s).",
    "developmental_stage": "DEVELOPMENTAL STAGE comment text(s).",
    "isoform_count": "Count of isoforms in ALTERNATIVE PRODUCTS comments.",
    "ft_transmem_count": "Count of TRANSMEM features in UniProt feature table.",
    "ft_topo_dom_count": "Count of TOPO_DOM features.",
    "ft_domain_count": "Count of DOMAIN features.",
    "ft_region_count": "Count of REGION features.",
    "ft_binding_count": "Count of BINDING features.",
    "ft_ptm_count": "Count of MOD_RES + CARBOHYD features.",
    "ft_variant_count": "Count of VARIANT features.",
    "ft_mutagen_count": "Count of MUTAGEN features.",
    "pdb_count": "Number of PDB cross-references.",
    "pdb_ids": "PDB IDs (semicolon-separated).",
}


def col_groups(columns) -> dict:
    cols = list(columns)
    aac = sorted(c for c in cols if c.startswith("aac_"))
    paac = sorted(c for c in cols if c.startswith("paac_"))
    ctd = sorted(c for c in cols if c.startswith("ctd_"))
    meta = sorted(
        c for c in cols if c not in ID_COLS and c not in aac and c not in paac and c not in ctd
    )
    return {"meta": meta, "aac": aac, "paac": paac, "ctd": ctd}


def df_schema_table(df: pd.DataFrame, max_rows: int = 50) -> str:
    lines = [
        "| Column | Dtype | Non-null | Null % |",
        "|--------|-------|----------|--------|",
    ]
    n = len(df)
    for col in df.columns[:max_rows]:
        nn = df[col].notna().sum()
        lines.append(f"| `{col}` | `{df[col].dtype}` | {nn:,} | {100*(n-nn)/n:.2f}% |")
    if len(df.columns) > max_rows:
        lines.append(f"| … | … | … | ({len(df.columns) - max_rows} more columns) |")
    return "\n".join(lines)


def numeric_summary(df: pd.DataFrame, cols: list[str]) -> str:
    sub = df[cols].select_dtypes(include=[np.number])
    if sub.empty:
        return "_No numeric columns._"
    desc = sub.describe().T
    desc = desc[["count", "mean", "std", "min", "50%", "max"]]
    desc.columns = ["count", "mean", "std", "min", "median", "max"]
    lines = [
        "| Feature | count | mean | std | min | median | max |",
        "|---------|------:|-----:|----:|----:|-------:|----:|",
    ]
    for idx, row in desc.head(25).iterrows():
        lines.append(
            f"| `{idx}` | {row['count']:.0f} | {row['mean']:.4g} | {row['std']:.4g} | "
            f"{row['min']:.4g} | {row['median']:.4g} | {row['max']:.4g} |"
        )
    if len(desc) > 25:
        lines.append(f"| … | | | | | | ({len(desc)-25} more) |")
    return "\n".join(lines)


def analyze_raw(name: str) -> str:
    df = pd.read_parquet(RAW_DIR / f"{name}.parquet")
    n = len(df)
    lines = [
        f"# Raw dataset: {name}",
        "",
        f"**Source file:** `data/raw/{name}.parquet`  ",
        f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "## Overview",
        "",
        f"| Metric | Value |",
        f"|--------|------:|",
        f"| Rows | {n:,} |",
        f"| Columns | {len(df.columns)} |",
        f"| Unique drugs (`Drug_ID`) | {df['Drug_ID'].nunique():,} |",
        f"| Unique targets (`Target_ID`) | {df['Target_ID'].nunique():,} |",
        f"| Null `Target_ID` | {df['Target_ID'].isna().sum():,} ({100*df['Target_ID'].isna().mean():.2f}%) |",
        f"| Duplicate rows | {df.duplicated().sum():,} |",
        "",
        "## Parquet schema",
        "",
        df_schema_table(df),
        "",
        "## Column descriptions",
        "",
        "| Column | Dtype | Description |",
        "|--------|-------|-------------|",
        "| `Drug_ID` | object/numeric | Compound identifier (dataset-specific format). |",
        "| `drug_smiles` | string | SMILES representation of the compound. |",
        "| `Target_ID` | string | Protein identifier (gene symbol for Davis; UniProt for KIBA/BindingDB). |",
        "| `target_sequence` | string | Target amino acid sequence bundled with the benchmark row. |",
        "| `affinity_label` | float | Affinity or activity label (scale differs by dataset). |",
        "",
        "## `affinity_label` distribution",
        "",
        "```",
        df["affinity_label"].describe().to_string(),
        "```",
        "",
        "## Text field lengths (median / max)",
        "",
        f"| Field | Median length | Max length |",
        f"|-------|-------------:|-----------:|",
        f"| `drug_smiles` | {df['drug_smiles'].astype(str).str.len().median():.0f} | {df['drug_smiles'].astype(str).str.len().max()} |",
        f"| `target_sequence` | {df['target_sequence'].astype(str).str.len().median():.0f} | {df['target_sequence'].astype(str).str.len().max()} |",
        "",
    ]
    if name == "davis":
        lines += [
            "## Target ID notes (Davis)",
            "",
            "- `Target_ID` values are **human kinase gene symbols** (e.g. `AAK1`, `ABL1p`), not UniProt accessions.",
            "- Trailing `p` denotes phosphatase-related naming in the benchmark (stripped during UniProt mapping).",
            "- Complex names (e.g. `BRAF(V600E)`, `JAK2(JH1domain-catalytic)`) often fail automated gene lookup.",
            "",
        ]
    elif name == "kiba":
        lines += [
            "## Target ID notes (KIBA)",
            "",
            "- `Target_ID` values are **UniProt accessions** (e.g. `O00141`, `P00533`).",
            "- No gene-symbol mapping is required before UniProt fetch.",
            "",
        ]
    else:
        lines += [
            "## Target ID notes (BindingDB-KD)",
            "",
            "- `Target_ID` is mostly UniProt accessions; **null** targets occur on a subset of rows.",
            "- Some rows may use composite or non-standard IDs that fail UniProt REST lookup.",
            "",
        ]
    top_targets = df["Target_ID"].value_counts().head(10)
    lines += ["## Top 10 targets by row count", "", "| Target_ID | Rows |", "|-----------|-----:|"]
    for tid, cnt in top_targets.items():
        lines.append(f"| `{tid}` | {cnt:,} |")
    lines.append("")
    return "\n".join(lines)


def analyze_processed(name: str) -> str:
    df = pd.read_parquet(PROC_DIR / f"{name}_enriched.parquet")
    raw = pd.read_parquet(RAW_DIR / f"{name}.parquet")
    groups = col_groups(df.columns)
    n = len(df)
    has_uid = df["uniprot_id"].notna()
    feat_cols = groups["meta"] + groups["aac"] + groups["paac"] + groups["ctd"]

    lines = [
        f"# Processed (enriched) dataset: {name}",
        "",
        f"**Source file:** `data/processed/{name}_enriched.parquet`  ",
        f"**Raw reference:** `data/raw/{name}.parquet`  ",
        f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "## Overview",
        "",
        "| Metric | Value |",
        "|--------|------:|",
        f"| Rows | {n:,} |",
        f"| Total columns | {len(df.columns)} |",
        f"| Raw / ID columns | {len([c for c in df.columns if c in ID_COLS])} |",
        f"| UniProt metadata columns | {len(groups['meta'])} |",
        f"| AAC columns | {len(groups['aac'])} |",
        f"| PAAC columns | {len(groups['paac'])} |",
        f"| CTD columns | {len(groups['ctd'])} |",
        f"| Rows with `uniprot_id` | {has_uid.sum():,} ({100*has_uid.mean():.2f}%) |",
        f"| Rows missing all protein features | {(~has_uid).sum():,} |",
        f"| Mean null rate across feature cols (rows with UniProt) | {100*df.loc[has_uid, feat_cols].isna().mean().mean():.2f}% |",
        "",
        "## Parquet schema (all columns)",
        "",
        df_schema_table(df, max_rows=80),
        "",
        "## ID and mapping columns",
        "",
    ]
    if "map_error" in df.columns:
        mc = df["map_error"].value_counts(dropna=False)
        lines += ["| map_error | Rows |", "|-----------|-----:|"]
        for k, v in mc.items():
            lines.append(f"| `{k}` | {v:,} |")
        lines.append("")

    fail_path = PROC_DIR / f"{name}_fetch_failures.parquet"
    if fail_path.exists():
        ff = pd.read_parquet(fail_path)
        lines += [
            f"## Fetch / mapping failures (`{name}_fetch_failures.parquet`)",
            "",
            f"- Failure log rows: **{len(ff):,}**",
            "",
        ]
        if "error" in ff.columns:
            lines += ["| error | Count |", "|-------|------:|"]
            for k, v in ff["error"].value_counts().items():
                lines.append(f"| `{k}` | {v:,} |")
            lines.append("")

    lines += [
        "## `affinity_label` (unchanged from raw)",
        "",
        "```",
        df["affinity_label"].describe().to_string(),
        "```",
        "",
        "## UniProt metadata highlights (rows with valid `uniprot_id`)",
        "",
    ]
    sub = df.loc[has_uid]
    if "sequence_length" in sub.columns:
        sl = sub["sequence_length"].dropna()
        lines += [
            f"- **sequence_length:** min {sl.min():.0f}, median {sl.median():.0f}, max {sl.max():.0f}",
        ]
    if "molecular_weight" in sub.columns:
        mw = sub["molecular_weight"].dropna()
        lines += [f"- **molecular_weight:** median {mw.median():.0f} Da"]
    if "pdb_count" in sub.columns:
        lines += [f"- **pdb_count:** median {sub['pdb_count'].median():.0f}, max {sub['pdb_count'].max():.0f}"]
    lines += [
        "",
        "## Descriptor summaries (numeric)",
        "",
        "### AAC (amino acid composition)",
        "",
        numeric_summary(sub, groups["aac"]),
        "",
        "### PAAC (pseudo amino acid composition)",
        "",
        numeric_summary(sub, groups["paac"]),
        "",
        "### CTD (composition, transition, distribution)",
        "",
        numeric_summary(sub, groups["ctd"][:25]),
        "",
        "## Data quality notes",
        "",
    ]
    if name == "davis":
        n_fail_tgt = df.loc[df["map_error"] == "mapping_failed", "Target_ID"].nunique()
        lines += [
            f"- **{100*(~has_uid).mean():.2f}%** of rows ({(~has_uid).sum():,}) have `mapping_failed` (no `uniprot_id`).",
            f"- **{n_fail_tgt}** unique targets (of {df['Target_ID'].nunique()}) failed mapping; **{df.loc[has_uid, 'Target_ID'].nunique()}** mapped successfully.",
            "- Failed targets include mutant isoform names and kinase domain qualifiers not resolved by gene search.",
            "",
            "### Unmapped Davis `Target_ID` values (unique)",
            "",
        ]
        failed_ids = sorted(df.loc[df["map_error"] == "mapping_failed", "Target_ID"].unique())
        for tid in failed_ids:
            lines.append(f"- `{tid}`")
    elif name == "bindingdb_kd":
        core = ["sequence_length", "molecular_weight", "aac_A", "paac_APAAC1"]
        core_null = int((sub[core].isna().any(axis=1)).sum()) if len(sub) else 0
        lines += [
            "- **8.29%** of rows have null `Target_ID` / `uniprot_id` (`null_target_id`).",
            "- Extra PAAC columns (`paac_A`, `paac_C`, …) appear when propy fallback AAC columns differ across proteins (271 vs 239 columns).",
            "- High global null rate on all 232 feature columns is driven by **sparse extra `paac_{AA}` columns**; core descriptors are >99.9% populated for mapped rows.",
            f"- Rows with UniProt but any null in core features (`sequence_length`, `molecular_weight`, `aac_A`, `paac_APAAC1`): **{core_null:,}**.",
            "- One composite UniProt lookup (`P0DP25,P0DP24,P0DP23`) failed HTTP 400.",
        ]
    else:
        lines += [
            "- **100%** mapping success; all rows have `uniprot_id` and populated features.",
            "- Column set matches Davis/KIBA (239 columns).",
        ]
    lines.append("")
    return "\n".join(lines)


def feature_catalog() -> str:
    lines = [
        "# Protein feature catalog",
        "",
        "Features appended during enrichment come from **UniProt REST JSON** and **sequence descriptors** (propy3).",
        "",
        "## Column groups",
        "",
        "| Group | Prefix / names | Count (typical) | Type |",
        "|-------|----------------|----------------:|------|",
        "| Raw DTI fields | `Drug_ID`, `drug_smiles`, … | 5 | unchanged |",
        "| Resolved ID | `uniprot_id`, `map_error` | 2 | string |",
        "| UniProt metadata | see table below | 25 | mixed |",
        "| AAC | `aac_*` | 20 | float |",
        "| PAAC | `paac_APAAC*` or `paac_{AA}` | 40–72 | float |",
        "| CTD | `ctd_*` | 147 | float |",
        "",
        "## UniProt metadata columns",
        "",
        "| Column | Type | Description |",
        "|--------|------|-------------|",
    ]
    for col in METADATA_COLS:
        lines.append(f"| `{col}` | mixed | {METADATA_DESCRIPTIONS[col]} |")
    lines += [
        "",
        "## AAC (`aac_A` … `aac_Y`)",
        "",
        "- **Meaning:** Normalized frequency of each standard amino acid in the UniProt sequence.",
        "- **Source:** `propy.AAComposition.CalculateAAComposition` (fallback: count/length).",
        "- **Range:** [0, 1]; sums to ~1 across 20 letters.",
        "",
        "## PAAC (`paac_APAAC1` … `paac_APAAC40`)",
        "",
        "- **Meaning:** Pseudo amino acid composition capturing sequence order with hydrophobicity/hydrophilicity matrices.",
        "- **Source:** `propy.PseudoAAC.GetAPseudoAAC(sequence, lamda=10, weight=0.05)`.",
        "- **Note:** BindingDB merge may add `paac_A`, `paac_C`, … from fallback paths for some proteins.",
        "",
        "## CTD (`ctd_*`)",
        "",
        "- **Meaning:** Composition (C), transition (T), and distribution (D) descriptors for seven physicochemical properties (hydrophobicity, polarity, side-chain volume, etc.).",
        "- **Source:** `propy.CTD.CalculateCTD` (~147 numeric features).",
        "- **Naming:** `ctd__{Property}{C|T|D}{group}{percentile}` (propy naming with double underscores).",
        "",
    ]
    return "\n".join(lines)


def processed_overview(stats: dict) -> str:
    lines = [
        "# Processed datasets — cross-dataset overview",
        "",
        f"**Directory:** `data/processed/`  ",
        f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "## File inventory",
        "",
        "| File | Rows | Columns | Size (approx.) |",
        "|------|-----:|--------:|----------------:|",
    ]
    for name, s in stats.items():
        lines.append(
            f"| `{name}_enriched.parquet` | {s['rows']:,} | {s['cols']} | {s['size_mb']:.2f} MB |"
        )
    lines += [
        "",
        "## Comparison",
        "",
        "| Dataset | Rows | Cols | % with UniProt | Unique drugs | Unique targets | Affinity (median) |",
        "|---------|-----:|-----:|---------------:|-------------:|-----------------:|------------------:|",
    ]
    for name, s in stats.items():
        aff = s["aff_median"]
        aff_s = f"{aff:.4g}" if aff == aff else "—"
        lines.append(
            f"| **{name}** | {s['rows']:,} | {s['cols']} | {s['pct_uniprot']:.1f}% | "
            f"{s['drugs']:,} | {s['targets']:,} | {aff_s} |"
        )
    lines += [
        "",
        "## Shared vs dataset-specific columns",
        "",
        "- **Davis** and **KIBA** share the same **239** enriched columns.",
        "- **BindingDB-KD** has **271** columns (32 extra `paac_{AA}` fallback columns from heterogeneous descriptor computation).",
        "- **239** columns are common across all three files.",
        "",
        "## Per-dataset documentation",
        "",
        "| Dataset | Raw analytics | Processed analytics |",
        "|---------|---------------|---------------------|",
        "| Davis | [raw/davis.md](raw/davis.md) | [processed/davis.md](processed/davis.md) |",
        "| KIBA | [raw/kiba.md](raw/kiba.md) | [processed/kiba.md](processed/kiba.md) |",
        "| BindingDB-KD | [raw/bindingdb_kd.md](raw/bindingdb_kd.md) | [processed/bindingdb_kd.md](processed/bindingdb_kd.md) |",
        "",
        "See also: [feature_catalog.md](feature_catalog.md)",
        "",
    ]
    return "\n".join(lines)


def write_full_schema(df: pd.DataFrame, path: Path, title: str) -> None:
    rows = []
    n = len(df)
    for col in df.columns:
        rows.append(
            {
                "column": col,
                "dtype": str(df[col].dtype),
                "non_null": int(df[col].notna().sum()),
                "null_pct": round(100 * (n - df[col].notna().sum()) / n, 4),
            }
        )
    schema_df = pd.DataFrame(rows)
    lines = [
        f"# {title}",
        "",
        f"**Rows:** {n:,}  ",
        f"**Columns:** {len(df.columns)}",
        "",
        "| # | Column | Dtype | Non-null | Null % |",
        "|--:|--------|-------|----------|-------:|",
    ]
    for i, r in schema_df.iterrows():
        lines.append(
            f"| {i+1} | `{r['column']}` | `{r['dtype']}` | {r['non_null']:,} | {r['null_pct']:.2f}% |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    (DOCS_DIR / "raw").mkdir(parents=True, exist_ok=True)
    (DOCS_DIR / "processed").mkdir(parents=True, exist_ok=True)
    (DOCS_DIR / "schemas").mkdir(parents=True, exist_ok=True)

    stats = {}
    for name in DATASETS:
        p = PROC_DIR / f"{name}_enriched.parquet"
        df = pd.read_parquet(p)
        stats[name] = {
            "rows": len(df),
            "cols": len(df.columns),
            "size_mb": p.stat().st_size / 1e6,
            "pct_uniprot": 100 * df["uniprot_id"].notna().mean(),
            "drugs": df["Drug_ID"].nunique(),
            "targets": df["Target_ID"].nunique(),
            "aff_median": df["affinity_label"].median(),
        }
        raw_df = pd.read_parquet(RAW_DIR / f"{name}.parquet")
        (DOCS_DIR / "raw" / f"{name}.md").write_text(analyze_raw(name), encoding="utf-8")
        (DOCS_DIR / "processed" / f"{name}.md").write_text(analyze_processed(name), encoding="utf-8")
        write_full_schema(
            raw_df,
            DOCS_DIR / "schemas" / f"raw_{name}_schema.md",
            f"Parquet schema: raw/{name}.parquet",
        )
        write_full_schema(
            df,
            DOCS_DIR / "schemas" / f"processed_{name}_schema.md",
            f"Parquet schema: processed/{name}_enriched.parquet",
        )

    (DOCS_DIR / "feature_catalog.md").write_text(feature_catalog(), encoding="utf-8")
    (DOCS_DIR / "processed" / "overview.md").write_text(processed_overview(stats), encoding="utf-8")

    index = [
        "# Dataset documentation",
        "",
        "Analytics and schema reference for DTI parquet files in this repository.",
        "",
        "## Contents",
        "",
        "- [Feature catalog](feature_catalog.md) — all protein feature groups and column meanings",
        "- [Processed overview](processed/overview.md) — cross-dataset comparison of enriched files",
        "",
        "### Raw inputs (`data/raw/`)",
        "",
        "- [davis.md](raw/davis.md)",
        "- [kiba.md](raw/kiba.md)",
        "- [bindingdb_kd.md](raw/bindingdb_kd.md)",
        "",
        "### Enriched outputs (`data/processed/`)",
        "",
        "- [davis.md](processed/davis.md)",
        "- [kiba.md](processed/kiba.md)",
        "- [bindingdb_kd.md](processed/bindingdb_kd.md)",
        "",
        "### Full parquet schemas (all columns)",
        "",
        "| Dataset | Raw | Processed |",
        "|---------|-----|-----------|",
        "| Davis | [schemas/raw_davis_schema.md](schemas/raw_davis_schema.md) | [schemas/processed_davis_schema.md](schemas/processed_davis_schema.md) |",
        "| KIBA | [schemas/raw_kiba_schema.md](schemas/raw_kiba_schema.md) | [schemas/processed_kiba_schema.md](schemas/processed_kiba_schema.md) |",
        "| BindingDB-KD | [schemas/raw_bindingdb_kd_schema.md](schemas/raw_bindingdb_kd_schema.md) | [schemas/processed_bindingdb_kd_schema.md](schemas/processed_bindingdb_kd_schema.md) |",
        "",
        "Regenerate analytics: `python _generate_docs.py`",
        "",
    ]
    (DOCS_DIR / "README.md").write_text("\n".join(index), encoding="utf-8")
    print("Wrote docs to", DOCS_DIR)


if __name__ == "__main__":
    main()
