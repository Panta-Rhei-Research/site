---
{
  "projection_kind": "taulib_declaration",
  "title": "FinitenessDecidability",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-vacuum/finiteness-decidability/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongVacuum`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongVacuum::FinitenessDecidability",
  "declaration_slug": "finiteness-decidability",
  "kind": "structure",
  "name": "FinitenessDecidability",
  "module_name": "TauLib.BookIV.Strong.StrongVacuum",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/",
  "source_line_start": 131,
  "source_line_end": 138,
  "registry_ids": [
    "IV.P81"
  ],
  "related_registry_items": [
    {
      "id": "IV.P81",
      "title": "Finiteness and decidability",
      "url": "/registry/object/IV.P81/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L131-L138",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L131-L138",
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
- Source path: [`TauLib/BookIV/Strong/StrongVacuum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L131-L138)
- Source range: L131-L138
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P81` — Finiteness and decidability

## Immediate Comment / Docstring

```lean
/-- [IV.P81] For each n >= 3, L_s[n] is finite and membership
    is decidable from the boundary holonomy data. -/
```

## Source Excerpt

```lean
structure FinitenessDecidability where
  /-- Finiteness holds at all stages >= 3. -/
  finite_all_stages : Bool := true
  /-- Membership is decidable. -/
  decidable : Bool := true
  /-- Source: inherited from finite-dimensionality of H_partial[n]. -/
  source : String := "finite-dimensionality of H_partial[n]"
  deriving Repr
```
