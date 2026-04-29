---
{
  "projection_kind": "taulib_declaration",
  "title": "ChromatinPartition",
  "permalink": "/verify/taulib/docs/book-vi-source-epigenetics/chromatin-partition/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Source.Epigenetics`.",
  "declaration_id": "TauLib.BookVI.Source.Epigenetics::ChromatinPartition",
  "declaration_slug": "chromatin-partition",
  "kind": "structure",
  "name": "ChromatinPartition",
  "module_name": "TauLib.BookVI.Source.Epigenetics",
  "module_url": "/verify/taulib/docs/book-vi-source-epigenetics/",
  "source_line_start": 52,
  "source_line_end": 61,
  "registry_ids": [
    "VI.D78"
  ],
  "related_registry_items": [
    {
      "id": "VI.D78",
      "title": "Chromatin Partition",
      "url": "/registry/object/VI.D78/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L52-L61",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Source.Epigenetics",
        "url": "/verify/taulib/docs/book-vi-source-epigenetics/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L52-L61",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookVI.Source.Epigenetics](/verify/taulib/docs/book-vi-source-epigenetics/)
- Source path: [`TauLib/BookVI/Source/Epigenetics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L52-L61)
- Source range: L52-L61
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D78` — Chromatin Partition

## Immediate Comment / Docstring

```lean
/-- [VI.D78] Chromatin Partition.
    Distinction clopen boundary at chromatin level: genome partitioned into
    euchromatin (active, D⁻¹(+)) and heterochromatin (silenced, D⁻¹(−)).
    The partition is a biological instance of VI.D04 (Distinction clopen boundary).
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
structure ChromatinPartition where
  /-- Fraction of genome in euchromatin (active, open chromatin). -/
  euchromatin_fraction : String := "D_inv_plus"
  /-- Fraction of genome in heterochromatin (silenced, condensed). -/
  heterochromatin_fraction : String := "D_inv_minus"
  /-- Disjoint union covers entire genome (clopen property). -/
  clopen : Bool := true
  /-- Scope: τ-effective (chromatin partition is a Distinction instance). -/
  scope : String := "tau-effective"
  deriving Repr
```
