---
{
  "projection_kind": "taulib_declaration",
  "title": "StrongHolonomyDefect",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-vacuum/strong-holonomy-defect/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongVacuum`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongVacuum::StrongHolonomyDefect",
  "declaration_slug": "strong-holonomy-defect",
  "kind": "structure",
  "name": "StrongHolonomyDefect",
  "module_name": "TauLib.BookIV.Strong.StrongVacuum",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/",
  "source_line_start": 161,
  "source_line_end": 168,
  "registry_ids": [
    "IV.D146"
  ],
  "related_registry_items": [
    {
      "id": "IV.D146",
      "title": "Strong holonomy defect",
      "url": "/registry/object/IV.D146/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L161-L168",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L161-L168",
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
- Source path: [`TauLib/BookIV/Strong/StrongVacuum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L161-L168)
- Source range: L161-L168
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D146` — Strong holonomy defect

## Immediate Comment / Docstring

```lean
/-- [IV.D146] The strong holonomy defect HolDef_{s,n}(f; ell)
    measures the norm difference between holonomy of f composed
    with a gap loop ell and holonomy of ell alone. -/
```

## Source Excerpt

```lean
structure StrongHolonomyDefect where
  /-- Stage n. -/
  stage : Nat
  /-- The defect is non-negative. -/
  nonneg : Bool := true
  /-- Vanishes when f preserves the gap loop holonomy exactly. -/
  vanishes_on_preservation : Bool := true
  deriving Repr
```
