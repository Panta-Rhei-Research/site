---
{
  "projection_kind": "taulib_declaration",
  "title": "CoherenceFunctionalLevel",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/coherence-functional-level/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::CoherenceFunctionalLevel",
  "declaration_slug": "coherence-functional-level",
  "kind": "structure",
  "name": "CoherenceFunctionalLevel",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 522,
  "source_line_end": 533,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L522-L533",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauHiggs2",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L522-L533",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs2](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L522-L533)
- Source range: L522-L533
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [IV.P199 upgrade] The coherence functional V_n at tower level n
    samples the lemniscate and sector structure. The physical level
    n = 2·|lobes| + |sectors| = 7 is the unique candidate with
    structural support.

    The Hessian eigenvalue λ₁ at level n gives m_H = √(2λ₁)·v.
    The n=7 formula achieves +8.0 ppm from PDG 125.20 GeV.

    Three candidate decompositions all yield n=7:
    (A) 2·lobes + sectors = 2·2 + 3 = 7 (CANONICAL)
    (B) generators + 2 = 5 + 2 = 7
    (C) b₁(τ³) + b₂(τ³) + 1 = 3 + 3 + 1 = 7 -/
```

## Source Excerpt

```lean
structure CoherenceFunctionalLevel where
  /-- Tower level n. -/
  n_level : Nat := 7
  /-- n = 2·lobes + sectors. -/
  decomp_canonical : n_level = 2 * 2 + 3
  /-- n = generators + 2. -/
  decomp_generators : n_level = 5 + 2
  /-- n = b₁ + b₂ + 1. -/
  decomp_betti : n_level = 3 + 3 + 1
  /-- Canonical decomposition is preferred. -/
  canonical_preferred : Bool := true
  deriving Repr
```
