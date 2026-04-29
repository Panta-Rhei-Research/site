---
{
  "projection_kind": "taulib_declaration",
  "title": "WindowUniversalityAll7Data",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/window-universality-all7-data/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::WindowUniversalityAll7Data",
  "declaration_slug": "window-universality-all7-data",
  "kind": "structure",
  "name": "WindowUniversalityAll7Data",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2187,
  "source_line_end": 2196,
  "registry_ids": [
    "IV.P205"
  ],
  "related_registry_items": [
    {
      "id": "IV.P205",
      "title": "Window Universality for All 7 NNLO Exponents",
      "url": "/registry/object/IV.P205/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2187-L2196",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/verify/taulib/docs/book-iv-particles-three-generations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2187-L2196",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2187-L2196)
- Source range: L2187-L2196
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P205` — Window Universality for All 7 NNLO Exponents

## Immediate Comment / Docstring

```lean
/-- [IV.P205] Window universality for all 7 NNLO exponents (formalized). -/
```

## Source Excerpt

```lean
structure WindowUniversalityAll7Data where
  /-- Number of NNLO exponents. -/
  n_exponents : Nat := 7
  /-- Number of exponents containing W₃(4) = 5 (all 7). -/
  n_with_w3_4 : Nat := 7
  /-- Exponent difference numerator: 1. -/
  k_diff_numer : Nat := 1
  /-- Exponent difference denominator: 6 = lobes × sectors. -/
  k_diff_denom : Nat := 6
  deriving Repr
```
