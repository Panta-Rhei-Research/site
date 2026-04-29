---
{
  "projection_kind": "taulib_declaration",
  "title": "FiniteLineageCarrier",
  "permalink": "/verify/taulib/docs/book-vi-life-core-distinction/finite-lineage-carrier/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.LifeCore.Distinction`.",
  "declaration_id": "TauLib.BookVI.LifeCore.Distinction::FiniteLineageCarrier",
  "declaration_slug": "finite-lineage-carrier",
  "kind": "structure",
  "name": "FiniteLineageCarrier",
  "module_name": "TauLib.BookVI.LifeCore.Distinction",
  "module_url": "/verify/taulib/docs/book-vi-life-core-distinction/",
  "source_line_start": 43,
  "source_line_end": 48,
  "registry_ids": [
    "VI.D05"
  ],
  "related_registry_items": [
    {
      "id": "VI.D05",
      "title": "Finite-Lineage Carrier",
      "url": "/registry/object/VI.D05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/Distinction.lean#L43-L48",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.LifeCore.Distinction",
        "url": "/verify/taulib/docs/book-vi-life-core-distinction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/Distinction.lean#L43-L48",
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

- Module: [TauLib.BookVI.LifeCore.Distinction](/verify/taulib/docs/book-vi-life-core-distinction/)
- Source path: [`TauLib/BookVI/LifeCore/Distinction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/LifeCore/Distinction.lean#L43-L48)
- Source range: L43-L48
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D05` — Finite-Lineage Carrier

## Immediate Comment / Docstring

```lean
/-- [VI.D05] Finite-lineage carrier: biological carrier with L-boundary,
    mortality, genotype-inheritable distinction. -/
```

## Source Excerpt

```lean
structure FiniteLineageCarrier where
  has_l_boundary : Bool := true
  is_mortal : Bool := true
  has_genotype : Bool := true
  carrier_type : String := "finite-lineage"
  deriving Repr
```
