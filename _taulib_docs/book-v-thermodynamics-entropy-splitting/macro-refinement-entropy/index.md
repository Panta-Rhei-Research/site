---
{
  "projection_kind": "taulib_declaration",
  "title": "MacroRefinementEntropy",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/macro-refinement-entropy/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.EntropySplitting`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.EntropySplitting::MacroRefinementEntropy",
  "declaration_slug": "macro-refinement-entropy",
  "kind": "structure",
  "name": "MacroRefinementEntropy",
  "module_name": "TauLib.BookV.Thermodynamics.EntropySplitting",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/",
  "source_line_start": 123,
  "source_line_end": 132,
  "registry_ids": [
    "V.D87"
  ],
  "related_registry_items": [
    {
      "id": "V.D87",
      "title": "Refinement entropy",
      "url": "/registry/object/V.D87/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L123-L132",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.EntropySplitting",
        "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L123-L132",
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

- Module: [TauLib.BookV.Thermodynamics.EntropySplitting](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/)
- Source path: [`TauLib/BookV/Thermodynamics/EntropySplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L123-L132)
- Source range: L123-L132
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D87` — Refinement entropy

## Immediate Comment / Docstring

```lean
/-- [V.D87] Refinement entropy at orbit depth n:

    S_ref(n) = lim_{r->inf} (1/r) ln P_free(n,r)

    Measures the exponential growth rate of defect-free paths.
    These exist even in the vacuum (lattice connectivity). S_ref
    grows without bound as refinement depth increases. -/
```

## Source Excerpt

```lean
structure MacroRefinementEntropy where
  /-- Orbit depth. -/
  depth : Nat
  /-- Refinement entropy numerator. -/
  s_ref_numer : Nat
  /-- Refinement entropy denominator. -/
  s_ref_denom : Nat
  /-- Denominator positive. -/
  denom_pos : s_ref_denom > 0
  deriving Repr
```
