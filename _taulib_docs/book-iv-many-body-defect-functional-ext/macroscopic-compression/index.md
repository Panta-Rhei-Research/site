---
{
  "projection_kind": "taulib_declaration",
  "title": "MacroscopicCompression",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/macroscopic-compression/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt::MacroscopicCompression",
  "declaration_slug": "macroscopic-compression",
  "kind": "structure",
  "name": "MacroscopicCompression",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/",
  "source_line_start": 158,
  "source_line_end": 165,
  "registry_ids": [
    "IV.D213"
  ],
  "related_registry_items": [
    {
      "id": "IV.D213",
      "title": "Macroscopic compression",
      "url": "/registry/object/IV.D213/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L158-L165",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
        "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L158-L165",
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

- Module: [TauLib.BookIV.ManyBody.DefectFunctionalExt](/verify/taulib/docs/book-iv-many-body-defect-functional-ext/)
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L158-L165)
- Source range: L158-L165
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D213` — Macroscopic compression

## Immediate Comment / Docstring

```lean
/-- [IV.D213] Macroscopic compression: kappa^macro(C) = (1/N) sum_i kappa(d_i) + kappa_int(C).
    In a crystal, kappa^macro ~ 0 because the lattice enforces fixed density.
    In a gas, kappa^macro fluctuates freely. -/
```

## Source Excerpt

```lean
structure MacroscopicCompression where
  /-- Average single-particle compression (scaled). -/
  average_compression : Nat
  /-- Interaction correction. -/
  interaction : Int
  /-- In crystal: near zero. -/
  crystal_suppressed : Bool
  deriving Repr
```
