---
{
  "projection_kind": "taulib_declaration",
  "title": "MagneticOrders",
  "permalink": "/verify/taulib/docs/book-iv-many-body-magnetism/magnetic-orders/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.Magnetism`.",
  "declaration_id": "TauLib.BookIV.ManyBody.Magnetism::MagneticOrders",
  "declaration_slug": "magnetic-orders",
  "kind": "structure",
  "name": "MagneticOrders",
  "module_name": "TauLib.BookIV.ManyBody.Magnetism",
  "module_url": "/verify/taulib/docs/book-iv-many-body-magnetism/",
  "source_line_start": 235,
  "source_line_end": 244,
  "registry_ids": [
    "IV.P228"
  ],
  "related_registry_items": [
    {
      "id": "IV.P228",
      "title": "Magnetic Orders as Defect-Tuple Signatures",
      "url": "/registry/object/IV.P228/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L235-L244",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.Magnetism",
        "url": "/verify/taulib/docs/book-iv-many-body-magnetism/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L235-L244",
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

- Module: [TauLib.BookIV.ManyBody.Magnetism](/verify/taulib/docs/book-iv-many-body-magnetism/)
- Source path: [`TauLib/BookIV/ManyBody/Magnetism.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L235-L244)
- Source range: L235-L244
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P228` — Magnetic Orders as Defect-Tuple Signatures

## Immediate Comment / Docstring

```lean
/-- [IV.P228] Five magnetic orders as defect-tuple d₄ signatures:
    1. Diamagnetic: all d₄ paired, M ≤ 0
    2. Paramagnetic: random d₄, M → 0 at h=0
    3. Ferromagnetic: global d₄ alignment, M > 0
    4. Antiferromagnetic: alternating d₄ sublattices, M = 0
    5. Ferrimagnetic: unequal sublattice alignment, 0 < M < M_ferro -/
```

## Source Excerpt

```lean
structure MagneticOrders where
  /-- Five fundamental orders. -/
  num_orders : Nat := 5
  /-- Order names. -/
  orders : List String :=
    ["Diamagnetic", "Paramagnetic", "Ferromagnetic",
     "Antiferromagnetic", "Ferrimagnetic"]
  /-- All classified by d₄ pattern. -/
  all_from_d4 : Bool := true
  deriving Repr
```
