---
{
  "projection_kind": "taulib_declaration",
  "title": "StrongDefectFunctional",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-vacuum/strong-defect-functional/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongVacuum`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongVacuum::StrongDefectFunctional",
  "declaration_slug": "strong-defect-functional",
  "kind": "structure",
  "name": "StrongDefectFunctional",
  "module_name": "TauLib.BookIV.Strong.StrongVacuum",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/",
  "source_line_start": 176,
  "source_line_end": 187,
  "registry_ids": [
    "IV.D147"
  ],
  "related_registry_items": [
    {
      "id": "IV.D147",
      "title": "Strong defect functional",
      "url": "/registry/object/IV.D147/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L176-L187",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.StrongVacuum",
        "url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L176-L187",
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

- Module: [TauLib.BookIV.Strong.StrongVacuum](/verify/taulib/docs/book-iv-strong-strong-vacuum/)
- Source path: [`TauLib/BookIV/Strong/StrongVacuum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L176-L187)
- Source range: L176-L187
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D147` — Strong defect functional

## Immediate Comment / Docstring

```lean
/-- [IV.D147] The strong defect functional Delta_n^s(f):
    NFMin-aggregated minimum of holonomy defects over all gap loops. -/
```

## Source Excerpt

```lean
structure StrongDefectFunctional where
  /-- Stage n. -/
  stage : Nat
  /-- Aggregation method: NFMin. -/
  aggregation : String := "NFMin over L_s[n]"
  /-- Non-negative valued. -/
  nonneg : Bool := true
  /-- Vanishes on identity. -/
  vanishes_on_id : Bool := true
  /-- Refinement monotone. -/
  refinement_monotone : Bool := true
  deriving Repr
```
