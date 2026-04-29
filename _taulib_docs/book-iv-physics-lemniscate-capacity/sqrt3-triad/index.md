---
{
  "projection_kind": "taulib_declaration",
  "title": "Sqrt3Triad",
  "permalink": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/sqrt3-triad/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.LemniscateCapacity`.",
  "declaration_id": "TauLib.BookIV.Physics.LemniscateCapacity::Sqrt3Triad",
  "declaration_slug": "sqrt3-triad",
  "kind": "structure",
  "name": "Sqrt3Triad",
  "module_name": "TauLib.BookIV.Physics.LemniscateCapacity",
  "module_url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/",
  "source_line_start": 191,
  "source_line_end": 198,
  "registry_ids": [
    "IV.R11"
  ],
  "related_registry_items": [
    {
      "id": "IV.R11",
      "title": "√3 Triad",
      "url": "/registry/object/IV.R11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/LemniscateCapacity.lean#L191-L198",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.LemniscateCapacity",
        "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/LemniscateCapacity.lean#L191-L198",
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

- Module: [TauLib.BookIV.Physics.LemniscateCapacity](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/)
- Source path: [`TauLib/BookIV/Physics/LemniscateCapacity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/LemniscateCapacity.lean#L191-L198)
- Source range: L191-L198
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R11` — √3 Triad

## Immediate Comment / Docstring

```lean
/-- [IV.R11] The √3 triad: three independent physical formulas
    sharing the same √3 from the lemniscate three-fold.

    1. R correction:  R₀ = ι_τ^(-7) − √3·ι_τ^(-2)
    2. δ_A:          δ_A/m_n = (√3/2)·ι_τ⁶
    3. α_G:          α_G = α¹⁸·√3·κ  (if κ_n = 2√3)

    This universality is CONJECTURAL: the R correction √3 is
    tau-effective (Sprint 1), but δ_A and α_G await full derivation. -/
```

## Source Excerpt

```lean
structure Sqrt3Triad where
  /-- Name of the formula. -/
  name : String
  /-- Where √3 appears. -/
  role : String
  /-- Scope: tau-effective or conjectural. -/
  scope : String
  deriving Repr
```
