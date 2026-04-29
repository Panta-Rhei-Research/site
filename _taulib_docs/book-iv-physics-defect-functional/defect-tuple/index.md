---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectTuple",
  "permalink": "/verify/taulib/docs/book-iv-physics-defect-functional/defect-tuple/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.DefectFunctional`.",
  "declaration_id": "TauLib.BookIV.Physics.DefectFunctional::DefectTuple",
  "declaration_slug": "defect-tuple",
  "kind": "structure",
  "name": "DefectTuple",
  "module_name": "TauLib.BookIV.Physics.DefectFunctional",
  "module_url": "/verify/taulib/docs/book-iv-physics-defect-functional/",
  "source_line_start": 79,
  "source_line_end": 88,
  "registry_ids": [
    "IV.D17"
  ],
  "related_registry_items": [
    {
      "id": "IV.D17",
      "title": "Defect Tuple",
      "url": "/registry/object/IV.D17/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/DefectFunctional.lean#L79-L88",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.DefectFunctional",
        "url": "/verify/taulib/docs/book-iv-physics-defect-functional/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/DefectFunctional.lean#L79-L88",
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

- Module: [TauLib.BookIV.Physics.DefectFunctional](/verify/taulib/docs/book-iv-physics-defect-functional/)
- Source path: [`TauLib/BookIV/Physics/DefectFunctional.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/DefectFunctional.lean#L79-L88)
- Source range: L79-L88
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D17` — Defect Tuple

## Immediate Comment / Docstring

```lean
/-- [IV.D17] Defect tuple: the 4-component functional that classifies
    fluid states and drives regularity.

    All components are non-negative scaled integers (representing
    defect magnitudes computed on finite clopen lattices). -/
```

## Source Excerpt

```lean
structure DefectTuple where
  /-- Mobility defect value (scaled). -/
  mobility : Nat
  /-- Vorticity defect value (scaled). -/
  vorticity : Nat
  /-- Compression defect value (scaled). -/
  compression : Nat
  /-- Topological defect value (scaled). -/
  topological : Nat
  deriving Repr, DecidableEq, BEq
```
