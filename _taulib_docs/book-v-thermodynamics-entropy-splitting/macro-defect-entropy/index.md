---
{
  "projection_kind": "taulib_declaration",
  "title": "MacroDefectEntropy",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/macro-defect-entropy/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.EntropySplitting`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.EntropySplitting::MacroDefectEntropy",
  "declaration_slug": "macro-defect-entropy",
  "kind": "structure",
  "name": "MacroDefectEntropy",
  "module_name": "TauLib.BookV.Thermodynamics.EntropySplitting",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/",
  "source_line_start": 97,
  "source_line_end": 106,
  "registry_ids": [
    "V.D86"
  ],
  "related_registry_items": [
    {
      "id": "V.D86",
      "title": "Defect entropy",
      "url": "/registry/object/V.D86/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L97-L106",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L97-L106",
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
- Source path: [`TauLib/BookV/Thermodynamics/EntropySplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L97-L106)
- Source range: L97-L106
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D86` — Defect entropy

## Immediate Comment / Docstring

```lean
/-- [V.D86] Defect entropy at orbit depth n:

    S_def(n) = lim_{r->inf} (1/r) ln(1 + P_def(n,r))

    Measures the exponential growth rate of defect-traversing paths.
    The +1 ensures S_def = 0 when P_def = 0.

    Stored as rational approximation (numer/denom). -/
```

## Source Excerpt

```lean
structure MacroDefectEntropy where
  /-- Orbit depth. -/
  depth : Nat
  /-- Defect entropy numerator (non-negative). -/
  s_def_numer : Nat
  /-- Defect entropy denominator. -/
  s_def_denom : Nat
  /-- Denominator positive. -/
  denom_pos : s_def_denom > 0
  deriving Repr
```
