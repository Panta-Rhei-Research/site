---
{
  "projection_kind": "taulib_declaration",
  "title": "SignLevel",
  "permalink": "/verify/taulib/docs/book-ii-mirror-sign-classification/sign-level/",
  "summary_short": "`inductive` declaration in `TauLib.BookII.Mirror.SignClassification`.",
  "declaration_id": "TauLib.BookII.Mirror.SignClassification::SignLevel",
  "declaration_slug": "sign-level",
  "kind": "inductive",
  "name": "SignLevel",
  "module_name": "TauLib.BookII.Mirror.SignClassification",
  "module_url": "/verify/taulib/docs/book-ii-mirror-sign-classification/",
  "source_line_start": 47,
  "source_line_end": 62,
  "registry_ids": [
    "II.D68"
  ],
  "related_registry_items": [
    {
      "id": "II.D68",
      "title": "Structural Sign Classification",
      "url": "/registry/object/II.D68/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean#L47-L62",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Mirror.SignClassification",
        "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean#L47-L62",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookII.Mirror.SignClassification](/verify/taulib/docs/book-ii-mirror-sign-classification/)
- Source path: [`TauLib/BookII/Mirror/SignClassification.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean#L47-L62)
- Source range: L47-L62
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `II.D68` — Structural Sign Classification

## Immediate Comment / Docstring

```lean
/-- [II.D68] The 12 structural sign levels.
    Each level represents a feature where orthodox and tau approaches
    make different structural choices. -/
```

## Source Excerpt

```lean
inductive SignLevel where
  | ScalarAlgebra     -- j^2 = -1 (orthodox) vs j^2 = +1 (tau)
  | HolomorphyPDE     -- elliptic CR (orthodox) vs hyperbolic split-CR (tau)
  | BoundaryInterior   -- interior determines boundary vs boundary determines interior
  | Infinity           -- Cantor hierarchy vs unique omega
  | Cardinality        -- uncountable reals vs countable tau-reals
  | Topology           -- Hausdorff + second countable vs Stone space (profinite)
  | Geometry           -- Riemannian vs betweenness-first (earned from order)
  | Compactness        -- locally compact vs profinitely compact
  | Idempotents        -- no nontrivial (C) vs nontrivial e+, e- (H_tau)
  | Liouville          -- bounded entire => constant vs bounded hol => sector-balanced
  | Gluing             -- sheaf on opens vs sheaf on clopens (Stone topology)
  | Spectrum           -- Gelfand spectrum vs primorial spectrum
  deriving DecidableEq, Repr

open SignLevel
```
