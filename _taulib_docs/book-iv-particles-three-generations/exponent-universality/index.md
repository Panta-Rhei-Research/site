---
{
  "projection_kind": "taulib_declaration",
  "title": "ExponentUniversality",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/exponent-universality/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::ExponentUniversality",
  "declaration_slug": "exponent-universality",
  "kind": "structure",
  "name": "ExponentUniversality",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2696,
  "source_line_end": 2707,
  "registry_ids": [
    "IV.R431"
  ],
  "related_registry_items": [
    {
      "id": "IV.R431",
      "title": "Exponent Universality: All Ratios from W",
      "url": "/registry/object/IV.R431/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2696-L2707",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2696-L2707",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2696-L2707)
- Source range: L2696-L2707
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R431` — Exponent Universality: All Ratios from W

## Immediate Comment / Docstring

```lean
/-- [IV.R431] Exponent universality: all ratios from winding matrix W.
    7/7 exponents now derived from first principles (updated Wave 45). -/
```

## Source Excerpt

```lean
structure ExponentUniversality where
  /-- Total quark mass ratios. -/
  total_ratios : Nat := 7
  /-- Ratios derived from first principles. -/
  derived_ratios : Nat := 6
  /-- Ratios with structural decomposition. -/
  decomposed_ratios : Nat := 0
  /-- Input ratios. -/
  input_ratios : Nat := 1
  /-- All accounted for. -/
  complete : total_ratios = derived_ratios + decomposed_ratios + input_ratios
  deriving Repr
```
