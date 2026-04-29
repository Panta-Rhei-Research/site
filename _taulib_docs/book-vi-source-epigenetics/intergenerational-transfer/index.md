---
{
  "projection_kind": "taulib_declaration",
  "title": "IntergenerationalTransfer",
  "permalink": "/verify/taulib/docs/book-vi-source-epigenetics/intergenerational-transfer/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Source.Epigenetics`.",
  "declaration_id": "TauLib.BookVI.Source.Epigenetics::IntergenerationalTransfer",
  "declaration_slug": "intergenerational-transfer",
  "kind": "structure",
  "name": "IntergenerationalTransfer",
  "module_name": "TauLib.BookVI.Source.Epigenetics",
  "module_url": "/verify/taulib/docs/book-vi-source-epigenetics/",
  "source_line_start": 166,
  "source_line_end": 175,
  "registry_ids": [
    "VI.D82"
  ],
  "related_registry_items": [
    {
      "id": "VI.D82",
      "title": "Intergenerational Transfer",
      "url": "/registry/object/VI.D82/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L166-L175",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L166-L175",
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
- Source path: [`TauLib/BookVI/Source/Epigenetics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L166-L175)
- Source range: L166-L175
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D82` — Intergenerational Transfer

## Immediate Comment / Docstring

```lean
/-- [VI.D82] Intergenerational Transfer.
    Partial inheritance of epigenetic marks through cell division.
    Unlike DNA replication (high fidelity), epigenetic mark copying is lossy:
    DNMT1 copies methylation with ~95% fidelity per CpG per division.
    This is SelfDesc closure (VI.T03) with inherent transmission loss.
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
structure IntergenerationalTransfer where
  /-- Primary maintenance mechanism. -/
  maintenance_enzyme : String := "DNMT1"
  /-- Transmission is lossy (unlike DNA replication). -/
  lossy : Bool := true
  /-- Approximate fidelity per CpG per division (×100 for integer). -/
  fidelity_per_cpg_x100 : Nat := 95
  /-- Scope: τ-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
