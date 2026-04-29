---
{
  "projection_kind": "taulib_declaration",
  "title": "FiberSpinDecomposition",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/fiber-spin-decomposition/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauHiggs`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs::FiberSpinDecomposition",
  "declaration_slug": "fiber-spin-decomposition",
  "kind": "structure",
  "name": "FiberSpinDecomposition",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/",
  "source_line_start": 198,
  "source_line_end": 207,
  "registry_ids": [
    "IV.L06"
  ],
  "related_registry_items": [
    {
      "id": "IV.L06",
      "title": "Crossing-Point Mode Classification",
      "url": "/registry/object/IV.L06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L198-L207",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauHiggs",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L198-L207",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs](/verify/taulib/docs/book-iv-electroweak-tau-higgs/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L198-L207)
- Source range: L198-L207
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.L06` — Crossing-Point Mode Classification

## Immediate Comment / Docstring

```lean
/-- [IV.L06] Fiber excitations on T² decompose by spin at the
    crossing point:
    - Spin 0: scalar (survives as Higgs)
    - Spin 1: vector (eaten as longitudinal W/Z modes = Goldstones)

    This decomposition is forced by the SO(2) symmetry of the
    crossing-point tangent space. -/
```

## Source Excerpt

```lean
structure FiberSpinDecomposition where
  /-- Number of spin-0 modes at crossing. -/
  spin0_count : Nat := 1
  /-- Number of spin-1 modes at crossing. -/
  spin1_count : Nat := 3
  /-- Total excitation count. -/
  total : Nat := 4
  /-- Total equals spin-0 + spin-1. -/
  total_check : total = spin0_count + spin1_count := by omega
  deriving Repr
```
