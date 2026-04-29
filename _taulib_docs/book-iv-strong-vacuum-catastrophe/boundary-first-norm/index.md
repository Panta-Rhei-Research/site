---
{
  "projection_kind": "taulib_declaration",
  "title": "BoundaryFirstNorm",
  "permalink": "/verify/taulib/docs/book-iv-strong-vacuum-catastrophe/boundary-first-norm/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.VacuumCatastrophe`.",
  "declaration_id": "TauLib.BookIV.Strong.VacuumCatastrophe::BoundaryFirstNorm",
  "declaration_slug": "boundary-first-norm",
  "kind": "structure",
  "name": "BoundaryFirstNorm",
  "module_name": "TauLib.BookIV.Strong.VacuumCatastrophe",
  "module_url": "/verify/taulib/docs/book-iv-strong-vacuum-catastrophe/",
  "source_line_start": 54,
  "source_line_end": 63,
  "registry_ids": [
    "IV.D192"
  ],
  "related_registry_items": [
    {
      "id": "IV.D192",
      "title": "Boundary-first normalization",
      "url": "/registry/object/IV.D192/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L54-L63",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L54-L63",
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
- Source path: [`TauLib/BookIV/Strong/VacuumCatastrophe.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L54-L63)
- Source range: L54-L63
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D192` — Boundary-first normalization

## Immediate Comment / Docstring

```lean
/-- [IV.D192] A physical quantity Q satisfies boundary-first normalization
    if Q = eval o chi o omega-germ, factoring through:
    1. The profinite omega-germ limit
    2. A boundary character (tail-invariant)
    3. Evaluation in tau-Idx

    This ensures no uncountable intermediaries appear. -/
```

## Source Excerpt

```lean
structure BoundaryFirstNorm where
  /-- Factorization: eval o chi o omega-germ. -/
  factorization : String := "eval composed chi composed omega-germ"
  /-- Step 1: omega-germ (profinite limit). -/
  step1_omega_germ : Bool := true
  /-- Step 2: boundary character (tail-invariant). -/
  step2_boundary_char : Bool := true
  /-- Step 3: evaluation in tau-Idx. -/
  step3_evaluation : Bool := true
  deriving Repr
```
