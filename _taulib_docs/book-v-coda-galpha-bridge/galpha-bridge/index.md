---
{
  "projection_kind": "taulib_declaration",
  "title": "GAlphaBridge",
  "permalink": "/verify/taulib/docs/book-v-coda-galpha-bridge/galpha-bridge/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Coda.GAlphaBridge`.",
  "declaration_id": "TauLib.BookV.Coda.GAlphaBridge::GAlphaBridge",
  "declaration_slug": "galpha-bridge",
  "kind": "structure",
  "name": "GAlphaBridge",
  "module_name": "TauLib.BookV.Coda.GAlphaBridge",
  "module_url": "/verify/taulib/docs/book-v-coda-galpha-bridge/",
  "source_line_start": 57,
  "source_line_end": 72,
  "registry_ids": [
    "V.T154"
  ],
  "related_registry_items": [
    {
      "id": "V.T154",
      "title": "The G-alpha Bridge",
      "url": "/registry/object/V.T154/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/GAlphaBridge.lean#L57-L72",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.GAlphaBridge",
        "url": "/verify/taulib/docs/book-v-coda-galpha-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/GAlphaBridge.lean#L57-L72",
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

- Module: [TauLib.BookV.Coda.GAlphaBridge](/verify/taulib/docs/book-v-coda-galpha-bridge/)
- Source path: [`TauLib/BookV/Coda/GAlphaBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/GAlphaBridge.lean#L57-L72)
- Source range: L57-L72
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T154` — The G-alpha Bridge

## Immediate Comment / Docstring

```lean
/-- [V.T154] The G-α bridge identity:
    α_G = α¹⁸ · √3 · (1 − (3/π)·α)

    - Holonomy exponent 18 = 2 × 9 = 2 × (3²) from double-lobe winding
    - √3 from triangular calibration vertex
    - (1 − (3/π)·α) radiative correction from EM self-energy
    - Every factor has geometric origin in the τ³ fibration -/
```

## Source Excerpt

```lean
structure GAlphaBridge where
  /-- Holonomy exponent. -/
  holonomy_exp : Nat
  /-- Exponent is 18. -/
  exp_eq : holonomy_exp = 18
  /-- Exponent decomposes as 2 × 9. -/
  exp_decomp : holonomy_exp = 2 * 9
  /-- Number of lobes on the lemniscate. -/
  lobes : Nat := 2
  /-- Number of axioms (K0-K6). -/
  axioms_count : Nat := 9
  /-- √3 correction present. -/
  sqrt3_correction : Bool := true
  /-- Radiative correction present. -/
  radiative_correction : Bool := true
  deriving Repr
```
