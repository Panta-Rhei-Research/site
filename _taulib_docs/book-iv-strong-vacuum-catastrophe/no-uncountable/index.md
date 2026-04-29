---
{
  "projection_kind": "taulib_declaration",
  "title": "NoUncountable",
  "permalink": "/verify/taulib/docs/book-iv-strong-vacuum-catastrophe/no-uncountable/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.VacuumCatastrophe`.",
  "declaration_id": "TauLib.BookIV.Strong.VacuumCatastrophe::NoUncountable",
  "declaration_slug": "no-uncountable",
  "kind": "structure",
  "name": "NoUncountable",
  "module_name": "TauLib.BookIV.Strong.VacuumCatastrophe",
  "module_url": "/verify/taulib/docs/book-iv-strong-vacuum-catastrophe/",
  "source_line_start": 80,
  "source_line_end": 89,
  "registry_ids": [
    "IV.P119"
  ],
  "related_registry_items": [
    {
      "id": "IV.P119",
      "title": "No uncountable factorization",
      "url": "/registry/object/IV.P119/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L80-L89",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.VacuumCatastrophe",
        "url": "/verify/taulib/docs/book-iv-strong-vacuum-catastrophe/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L80-L89",
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

- Module: [TauLib.BookIV.Strong.VacuumCatastrophe](/verify/taulib/docs/book-iv-strong-vacuum-catastrophe/)
- Source path: [`TauLib/BookIV/Strong/VacuumCatastrophe.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L80-L89)
- Source range: L80-L89
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P119` — No uncountable factorization

## Immediate Comment / Docstring

```lean
/-- [IV.P119] No uncountable factorization: boundary-first normalized
    quantities involve only:
    - Finite sums at each stage
    - The profinite omega-germ limit
    - Evaluation in tau-Idx

    No uncountable sums, integrals over continua, or infinite-dimensional
    functional integrals appear. This is the structural reason the
    vacuum catastrophe does not arise. -/
```

## Source Excerpt

```lean
structure NoUncountable where
  /-- Only finite sums at each stage. -/
  finite_sums : Bool := true
  /-- No continuum integrals. -/
  no_continuum : Bool := true
  /-- No infinite-dimensional path integrals. -/
  no_path_integrals : Bool := true
  /-- Consequence: vacuum energy is automatically finite. -/
  vacuum_finite : Bool := true
  deriving Repr
```
