---
{
  "projection_kind": "taulib_declaration",
  "title": "MacroEntropySplitThm",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/macro-entropy-split-thm/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Thermodynamics.EntropySplitting`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.EntropySplitting::MacroEntropySplitThm",
  "declaration_slug": "macro-entropy-split-thm",
  "kind": "structure",
  "name": "MacroEntropySplitThm",
  "module_name": "TauLib.BookV.Thermodynamics.EntropySplitting",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/",
  "source_line_start": 150,
  "source_line_end": 163,
  "registry_ids": [
    "V.T56"
  ],
  "related_registry_items": [
    {
      "id": "V.T56",
      "title": "Entropy splitting",
      "url": "/registry/object/V.T56/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L150-L163",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L150-L163",
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
- Source path: [`TauLib/BookV/Thermodynamics/EntropySplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L150-L163)
- Source range: L150-L163
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T56` — Entropy splitting

## Immediate Comment / Docstring

```lean
/-- [V.T56] Entropy splitting theorem: total holomorphic entropy
    decomposes as S(n) = S_def(n) + S_ref(n) + epsilon(n), where
    the cross-term epsilon >= 0 satisfies epsilon <= S_def.

    When S_def = 0, the total entropy is purely refinement entropy.

    This captures the macroscopic decomposition on base tau^1,
    distinct from BookIV.Physics.EntropySplitting (microscopic). -/
```

## Source Excerpt

```lean
structure MacroEntropySplitThm where
  /-- Defect entropy component. -/
  defect : MacroDefectEntropy
  /-- Refinement entropy component. -/
  refinement : MacroRefinementEntropy
  /-- Cross-term numerator (epsilon >= 0). -/
  cross_numer : Nat
  /-- Cross-term denominator. -/
  cross_denom : Nat
  /-- Cross-term denominator positive. -/
  cross_denom_pos : cross_denom > 0
  /-- Both components at the same depth. -/
  same_depth : defect.depth = refinement.depth
  deriving Repr
```
