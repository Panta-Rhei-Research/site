---
{
  "projection_kind": "taulib_declaration",
  "title": "EntropySplitting",
  "permalink": "/verify/taulib/docs/book-iv-physics-thermodynamics/entropy-splitting/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.Thermodynamics`.",
  "declaration_id": "TauLib.BookIV.Physics.Thermodynamics::EntropySplitting",
  "declaration_slug": "entropy-splitting",
  "kind": "structure",
  "name": "EntropySplitting",
  "module_name": "TauLib.BookIV.Physics.Thermodynamics",
  "module_url": "/verify/taulib/docs/book-iv-physics-thermodynamics/",
  "source_line_start": 76,
  "source_line_end": 89,
  "registry_ids": [
    "IV.D24"
  ],
  "related_registry_items": [
    {
      "id": "IV.D24",
      "title": "Entropy Splitting",
      "url": "/registry/object/IV.D24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean#L76-L89",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.Thermodynamics",
        "url": "/verify/taulib/docs/book-iv-physics-thermodynamics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean#L76-L89",
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

- Module: [TauLib.BookIV.Physics.Thermodynamics](/verify/taulib/docs/book-iv-physics-thermodynamics/)
- Source path: [`TauLib/BookIV/Physics/Thermodynamics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/Thermodynamics.lean#L76-L89)
- Source range: L76-L89
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D24` — Entropy Splitting

## Immediate Comment / Docstring

```lean
/-- [IV.D24] Entropy splitting: S = S_def + S_ref.

    - S_def (defect entropy): coherence measure of defect novelty.
      Reaches zero at the coherence horizon.
    - S_ref (refinement entropy): measure of refinement depth.
      Grows unboundedly (refinement never terminates).

    The Second-Law Inversion: S_def reverses at the horizon,
    creating a novel thermodynamic asymmetry. -/
```

## Source Excerpt

```lean
structure EntropySplitting where
  /-- Defect entropy numerator (→ 0 at coherence horizon). -/
  s_def_numer : Nat
  /-- Defect entropy denominator. -/
  s_def_denom : Nat
  /-- Refinement entropy numerator (unbounded growth). -/
  s_ref_numer : Nat
  /-- Refinement entropy denominator. -/
  s_ref_denom : Nat
  /-- Defect entropy denominator positive. -/
  denom_pos_def : s_def_denom > 0
  /-- Refinement entropy denominator positive. -/
  denom_pos_ref : s_ref_denom > 0
  deriving Repr
```
