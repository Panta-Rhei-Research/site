---
{
  "projection_kind": "taulib_declaration",
  "title": "ProblemMapClassificationScheme",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/problem-map-classification-scheme/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::ProblemMapClassificationScheme",
  "declaration_slug": "problem-map-classification-scheme",
  "kind": "structure",
  "name": "ProblemMapClassificationScheme",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 898,
  "source_line_end": 905,
  "registry_ids": [
    "VII.D38"
  ],
  "related_registry_items": [
    {
      "id": "VII.D38",
      "title": "Problem Map Classification Scheme",
      "url": "/registry/object/VII.D38/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L898-L905",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Registers",
        "url": "/verify/taulib/docs/book-vii-meta-registers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L898-L905",
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

- Module: [TauLib.BookVII.Meta.Registers](/verify/taulib/docs/book-vii-meta-registers/)
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L898-L905)
- Source range: L898-L905
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D38` — Problem Map Classification Scheme

## Immediate Comment / Docstring

```lean
/-- [VII.D38] Problem Map Classification Scheme (ch30). 17 classical
    philosophical problems classified by their register-type and
    τ-resolution status: dissolved (structure reveals pseudo-problem),
    resolved (τ-answer), or bounded (methodological boundary). -/
```

## Source Excerpt

```lean
structure ProblemMapClassificationScheme where
  /-- 17 problems classified. -/
  problem_count : Nat := 17
  /-- Three resolution types: dissolved/resolved/bounded. -/
  resolution_types : Nat := 3
  /-- Classification is structural. -/
  structural : Bool := true
  deriving Repr
```
