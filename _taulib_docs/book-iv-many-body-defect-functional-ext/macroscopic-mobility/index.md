---
{
  "projection_kind": "taulib_declaration",
  "title": "MacroscopicMobility",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/macroscopic-mobility/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt::MacroscopicMobility",
  "declaration_slug": "macroscopic-mobility",
  "kind": "structure",
  "name": "MacroscopicMobility",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext/",
  "source_line_start": 136,
  "source_line_end": 141,
  "registry_ids": [
    "IV.D211"
  ],
  "related_registry_items": [
    {
      "id": "IV.D211",
      "title": "Macroscopic mobility",
      "url": "/registry/object/IV.D211/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L136-L141",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L136-L141",
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
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt.lean#L136-L141)
- Source range: L136-L141
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D211` — Macroscopic mobility

## Immediate Comment / Docstring

```lean
/-- [IV.D211] Macroscopic mobility: mu^macro(C) = (1/N) sum_i mu(d_i) + mu_int(C).
    The interaction term encodes collective resistance or facilitation
    of base-direction flow. -/
```

## Source Excerpt

```lean
structure MacroscopicMobility where
  /-- Average single-particle mobility (scaled). -/
  average_mobility : Nat
  /-- Interaction correction. -/
  interaction : Int
  deriving Repr
```
